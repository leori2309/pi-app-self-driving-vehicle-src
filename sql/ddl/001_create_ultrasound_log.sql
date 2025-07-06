CREATE TABLE IF NOT EXISTS ultrasound_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_name TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    distance_mm INTEGER NOT NULL
);