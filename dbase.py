import psycopg2
import psycopg2.extras
import config
class Dbase:
    def __init__(self):
        self.database = config.database
        self.user = config.user
        self.password = config.password
        self.host = config.host
        self.port = config.port
        self.conn = psycopg2.connect(database = self.database,
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port)
        cur = self.conn.cursor()

    def getDbConnection(self):
        return self.conn
    
    def fetchAll(self, query):
        cur = self._executeQuery(query)
        data = cur.fetchall()
        return data

    def _executeQuery(self, query):
        cur = self.conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        cur.execute(query)
        return cur