import os.path
import sqlite3
from datetime import datetime


class SqlSettings:
    def __init__(self):
        self.db_filename = "/database/germinationroom.db"
        self.conn = None

        self.open_connection()

    def open_connection(self):
        """
            This function connects if the db_filename file exist, otherwise it creates and connects.
        """
        try:
            if not os.path.exists(self.db_filename):
                self.create_table()
            self.conn = sqlite3.connect(self.db_filename)
            if self.conn is not None:
                print("Connection is successful with database.")
            else:
                print("Connection is failed with database!")

        except sqlite3.Error as er:
            print(f"This {er} happened in the open_connection func.")
            self.conn = None

    def close_connection(self):
        """
            This function for disconnect to sql database.
        """
        try:
            if self.conn is not None:
                self.conn.close()
                print("Connection is disabled.")
        except sqlite3.Error as er:
            print(f"This {er} happened close_connection func.")

    def create_table(self):
        self.open_connection()
        if self.conn is not None:
            cursor = self.conn.cursor()
            # Temperature and humidity set values created.
            cursor.execute(''' 
                CREATE TABLE IF NOT EXIST set_values(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    set_temp_min REAL,
                    set_temp_max REAL,
                    set_hum_min REAL,
                    set_hum_max REAL,
                    timestamp TEXT,
                )
            ''')

            # Temperature and humidity values added.
            cursor.execute('''
                CREATE TABLE IF NOT EXIST add_values(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temp_value REAL,
                    hum_value REAL,
                    timestamp TEXT,
                )
            ''')

    def insert_set_values(self, set_temp_min, set_temp_max, set_hum_min, set_hum_max):

        if self.conn is not None:
            cursor = self.conn.cursor()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''
                    INSERT INTO set_values (set_temp_min, set_temp_max, set_hum_min, set_hum_max, timestamp)
                    VALUES (?, ?, ?, ?, ?)
            ''', (set_temp_min, set_temp_max, set_hum_min, set_hum_max, timestamp))
            print("added set_value: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            self.conn.commit()
        else:
            print("add set value is failed.")

    def insert_values(self, temp_value, hum_value):
        if self.conn is not None:
            cursor = self.conn.cursor()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''
                    INSERT INTO values (temp_value, hum_value, timestamp)
                    VALUES (?, ?, ?)
            ''', (temp_value, hum_value, timestamp))
            print("added values: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            self.conn.commit()
        else:
            print("add values is failed.")

    def read_values_lcd(self):
        if not os.path.exists(self.db_filename):
            self.create_table()

        conn1 = sqlite3.connect(self.db_filename)

        try:
            if conn1 is not None:
                pass
            else:
                print("Connection is failed with database!")
            cursor1 = conn1.cursor()

            # Transaction started.
            conn1.execute("BEGIN TRANSACTION")

            cursor1.execute("SELECT * FROM values ORDER BY timestamp DESC LIMIT 1")

            data = cursor1.fetchall()

            # Print data to the lcd screen.
            for d in data:
                # Complete the transaction.
                self.conn.commit()
                return d

        except Exception as er:
            # Undo if there are errors during the transaction phase.
            conn1.rollback()
            print(f"read values error: {er}")

        finally:
            conn1.close()
            pass
