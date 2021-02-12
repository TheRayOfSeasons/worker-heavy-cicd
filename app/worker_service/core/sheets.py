from io import BytesIO

import xlwt


class ExcelHeader:
    """
    An interface for headers.
    """

    def __init__(self, text : str, width : int):
        self.text = text
        self.width = width

    def __dict__(self):
        return {
            'text': self.text,
            'width': self.width
        }


class ExcelReport:
    """
    A class that acts as a micro-framework for excel reports.
    """

    headers = []
    row_data = []
    available_palette_hex = 0x8
    custom_color_palette = []
    content_row_offset = 1
    filename = ''
    extension = 'xls'

    def __init__(self, *args, **kwargs):
        self.workbook = xlwt.Workbook()
        self.build_headers(*args, **kwargs)
        self.build_content(*args, **kwargs)

    def add_color(self, name, red, green, blue):
        """
        Adds a custom color in the pallette within
        the scope of the report. After adding the
        color, it also stores its name and hex code
        in the `custom_color_palette` attribute for
        reference purposes.

        NOTE: The xlwt library takes into account the binary
        significance of the values assigned to colors, hence
        the usage of hexadecimal values. For references, see:
        https://stackoverflow.com/questions/7746837/python-xlwt-set-custom-background-colour-of-a-cell

        Sample Usage:

        ```
        self.add_color('color_name', red=255, green=255, blue=255)

        style = xlwt.XFStyle()
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = xlwt.Style.colour_map['color_name']
        style.pattern = pattern
        return style
        ```
        """
        hex_value = self.available_palette_hex

        # xlwt only allows hexes equivalent to 8-63 as colors.
        # This is to protect the integrity of the library usage.
        if not (0x8 <= hex_value <= 0x3f):
            raise ValueError(
                'For integrity purposes, a color may only '
                'have a hex value of 8-63.'
            )

        xlwt.add_palette_colour(name, hex_value)
        self.workbook.set_colour_RGB(hex_value, red, green, blue)
        self.available_palette_hex += 0x1
        cached_value = {name: hex_value}
        self.custom_color_palette.append(cached_value)

    def get_filename(self, *args, **kwargs):
        """
        Returns the filename.
        """
        return self.filename or self.__class__.__name__

    def get_headers(self, *args, **kwargs):
        """
        A virtual method for retrieving the headers.
        """
        return self.headers

    def get_row_data(self, *args, **kwargs):
        """
        A virtual method for retrieving the row data.
        """
        return self.row_data

    def build_headers(self, *args, **kwargs):
        """
        Renders the headers into the sheet.
        """
        workbook = self.workbook
        headers = self.get_headers(*args, **kwargs)
        for col, header in enumerate(headers):
            workbook.write(0, col, header['text'])
        return workbook

    def build_content(self, *args, **kwargs):
        """
        Renders the contents into the sheet.
        """
        workbook = self.workbook
        row_data = self.get_row_data(self, *args, **kwargs)
        for row, data in enumerate(row_data):
            row += self.content_row_offset
            for col, datum in enumerate(row_data):
                workbook.write(row, col, datum)
        return workbook

    def output(self):
        """
        Returns a BytesIO object containing the report.
        """
        _output = BytesIO()
        self.workbook.save(_output)
        return _output

    def save_as_file(self, *args, **kwargs):
        """
        Writes the contents of the output into a file.
        """
        filename = self.get_filename(*args, **kwargs)
        extension = self.extension
        full_filename = f'{filename}.{extension}'
        with open(f'tmp_storage/{full_filename}', 'wb') as outfile:
            outfile.write(self.output.get_buffer())
