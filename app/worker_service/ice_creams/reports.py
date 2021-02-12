from core.sheets import ExcelReport


class FlavorsReport(ExcelReport):
    """
    Prints all flavors in an excel file.
    """

    headers = [
        {
            'text': 'Name',
        },
        {
            'text': 'Description'
        }
    ]
    row_data = [
        ['Rocky Road', 'WOW'],
        ['Cookies and Cream', 'XD']
    ]
