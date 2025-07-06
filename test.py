from DatabaseLogger import DatabaseLogger
from datetime import datetime


databaseLogger = DatabaseLogger()
databaseLogger._create_tables()
databaseLogger.log_ultrasound_data(
    sensor_name="TestSensor",
    distance_mm=123,
    timestamp=datetime.now()
)
