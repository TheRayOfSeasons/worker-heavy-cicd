import importlib

from configurations.settings import DATABASE

from .loggers import logger


class Connection:
    """
    Creates and returns a connection to the database.
    """

    def __init__(
            self, engine, database, user, password,\
            host, port, *args, **kwargs):
        engine_module = importlib.import_module(engine)
        self._engine = engine_module
        try:
            connection = engine_module.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
        except Exception as e:
            logger.error('Failed to connect to database.')
            raise e
        self._connection = connection

    @property
    def engine(self):
        """
        Returns the connection's database engine.
        """
        return self.engine

    @property
    def connection(self):
        """
        Returns the database connection instance.
        """
        return self._connection

    def get_cursor(self):
        """
        Returns a new connection cursor.
        """
        return self.connection.cursor()

    def execute_query(self, query_string, *args, **kwargs):
        """
        Accepts an SQL string, then executes it into the database.
        """
        cursor = self.get_cursor()
        cursor.execute(query_string)
        try:
            result = cursor.fetchall()
        except Exception:
            result = None
        cursor.close()
        return result


CONNECTION = Connection(
    engine=DATABASE['ENGINE'],
    database=DATABASE['NAME'],
    user=DATABASE['USER'],
    password=DATABASE['PASSWORD'],
    host=DATABASE['HOST'],
    port=DATABASE['PORT']
)
