from pypika import PostgreSQLQuery
from pypika import Table

from core.database import CONNECTION
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

    def get_row_data(self, *args, **kwargs):
        row_data = super().get_row_data(*args, **kwargs)
        flavors = Table('ice_creams_flavors')
        query = (
            PostgreSQLQuery
            .from_(flavors)
            .select('name', 'description')
        )
        result = CONNECTION.execute_query(query)
        row_data.extend(result)
        return row_data
