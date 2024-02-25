import os.path
import sqlite3
from datetime import datetime
import threading


class SqlSettings:
    def __init__(self):
        self.db_filename = "/home/germinationroom/Documents/germination_room/app/database/germinationroom.db"
        self.conn = None
        self.lock = threading.Lock()
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
        self.conn = sqlite3.connect(self.db_filename)
        if self.conn is not None:
            cursor = self.conn.cursor()
            # Temperature and humidity set values created.
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS set_values(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    set_temp_min REAL,
                    set_temp_max REAL,
                    set_hum_min REAL,
                    set_hum_max REAL,
                    timestamp TEXT
                )
            ''')

            # Temperature and humidity values added.
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS add_values(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    temp_value REAL,
                    hum_value REAL,
                    timestamp TEXT
                )
            ''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS times
                            (id INTEGER PRIMARY KEY, 
                            morning_time TEXT, 
                            night_time TEXT,
                            timestamp TEXT,
                            )''')

        # Bağlantıyı kaydet ve işlemi tamamla
        self.conn.commit()
        self.conn.close()

    def insert_set_values(self, set_temp_min, set_temp_max, set_hum_min, set_hum_max):

        if self.conn is not None:
            cursor = self.conn.cursor()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''
                    INSERT INTO set_values (set_temp_min, set_temp_max, set_hum_min, set_hum_max, timestamp)
                    VALUES (?, ?, ?, ?, ? )
            ''', (set_temp_min, set_temp_max, set_hum_min, set_hum_max, timestamp))
            print("added set_value: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            self.conn.commit()
        else:
            print("add values is failed.")

    def insert_values(self, temp_value, hum_value):
        if self.conn is not None:

            cursor = self.conn.cursor()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('''
                    INSERT INTO add_values (temp_value, hum_value, timestamp)
                    VALUES (?, ?, ?)
            ''', (temp_value, hum_value, timestamp))
            print("added values: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            self.conn.commit()
            cursor.close()
        else:
            print("add values is failed.")

    def set_update_time(self, morning_time, night_time):
        if self.conn is not None:
            cursor = self.conn.cursor()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(''' 
                UPDATE times SET morning_time, night_time, timestamp)
                VALUES ( ?, ?, ?)
                ''', (morning_time, night_time, timestamp))
            print("update time: ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            # cursor.execute("UPDATE times SET night_time = ?", (night_time,))  Tekli ekleme.
            self.conn.commit()
            cursor.close()
        else:
            print("add times is failed.")

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

            cursor1.execute("SELECT * FROM add_values ORDER BY timestamp DESC LIMIT 1")

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

    def read_set_values(self):
        if not os.path.exists(self.db_filename):
            self.create_table()

        conn2 = sqlite3.connect(self.db_filename)

        try:
            if conn2 is not None:
                pass
            else:
                print("Connection is failed with database!")
            cursor2 = conn2.cursor()

            # Transaction started.
            conn2.execute("BEGIN TRANSACTION")

            cursor2.execute("SELECT * FROM set_values ORDER BY timestamp DESC LIMIT 1")

            data = cursor2.fetchall()

            # Print data to the lcd screen.
            for d in data:
                # Complete the transaction.
                self.conn.commit()
                return d

        except Exception as er:
            # Undo if there are errors during the transaction phase.
            conn2.rollback()
            print(f"read values error: {er}")

        finally:
            conn2.close()
            pass

    def read_set_update_times(self):
        if not os.path.exists(self.db_filename):
            self.create_table()

        conn3 = sqlite3.connect(self.db_filename)

        try:
            if conn3 is not None:
                pass
            else:
                print("Connection is failed with database!")
            cursor3 = conn3.cursor()

            # Transaction started.
            conn3.execute("BEGIN TRANSACTION")

            cursor3.execute("SELECT * FROM times ORDER BY timestamp DESC LIMIT 1")

            data = cursor3.fetchall()

            # Print data to the lcd screen.
            for d in data:
                # Complete the transaction.
                self.conn.commit()
                return d

        except Exception as er:
            # Undo if there are errors during the transaction phase.
            conn3.rollback()
            print(f"read values error: {er}")

        finally:
            conn3.close()
            pass
