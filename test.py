from DatabaseLogger import DatabaseLogger
from datetime import datetime
import sqlite3
import pandas as pd

def load_data():
    conn = sqlite3.connect("sql/logging.db")
    df = pd.read_sql_query(f"SELECT timestamp, distance_mm FROM ultrasound_log WHERE timestamp >= '{(datetime.now() - pd.Timedelta(seconds=10)).isoformat(timespec='milliseconds')}'", conn)
    conn.close()
    return df

databaseLogger = DatabaseLogger()
databaseLogger._create_tables()
databaseLogger.log_ultrasound_data(
    sensor_name="TestSensor",
    distance_mm=100,
    timestamp=datetime.now()
)

print(load_data())