import sqlite3

class WorkWithDB:
    def __init__(self):
        self.conn = sqlite3.connect('dtm.db')
        self.cursor = self.conn.cursor()

    def insert_coords(self, data: list):
        my_sql = "INSERT INTO coordinates (a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y) VALUES (?, ?, ?, ?, ?, ?, ?, ?)".format(
            data
        )
        try:
            self.cursor.execute(my_sql, data)
            self.conn.commit()
            return True
        except Exception as e:
            return e

    def get_all_coords(self):
        my_sql = "SELECT id, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y FROM coordinates;"
        all_coords = self.cursor.execute(my_sql).fetchall()
        return all_coords
