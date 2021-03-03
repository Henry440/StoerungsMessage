import sqlite3

from confs import DB_NAME

class db():

    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def startentrys(self, title, status, val1, val2):
        ts = self._get_ts()
        self.c.execute(f"INSERT INTO startentrys VALUES(null, {ts}, )")

    def _save(self):
        self.conn.commit()

    def _get_ts(self):
        return 42