import sqlite3
import os
from datetime import datetime


DB_PATH = "sql/logging.db"
DDL_PATH = "sql/ddl"

class DatabaseLogger:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)

    def _submit_sql(self, sql: str) -> None:
        cursor = self.conn.cursor()
        try:
            print(f"{datetime.now().isoformat(timespec='milliseconds')}: Executing SQL: {sql}")
            cursor.execute(sql)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()

    def _create_tables(self) -> None:
        for filename in sorted(os.listdir(DDL_PATH)):
            if filename.endswith(".sql"):
                with open(os.path.join(DDL_PATH, filename), 'r') as file:
                    sql = file.read()
                    self._submit_sql(sql)


    def log_ultrasound_data(
            self, 
            sensor_name: str, 
            distance_mm: float, 
            timestamp: datetime.timestamp) -> None:
        sql = f"INSERT INTO ultrasound_log (sensor_name, timestamp, distance_mm) VALUES ('{sensor_name}', '{timestamp.isoformat(timespec='milliseconds')}', {distance_mm})"
        self._submit_sql(sql)
