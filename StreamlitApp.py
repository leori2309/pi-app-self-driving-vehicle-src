import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

def load_data():
    conn = sqlite3.connect("sql/logging.db")
    df = pd.read_sql_query(
        f"""
        SELECT timestamp, distance_mm 
        FROM ultrasound_log 
        WHERE timestamp >= '{(datetime.now() - pd.Timedelta(seconds=10)).isoformat(timespec='milliseconds')}'
        """, 
        conn
    )
    conn.close()
    return df

# App UI
st.title("Live Line Chart (Last 10 Seconds Only)")

if st.button("Refresh"):
    df = load_data()
    st.line_chart(df.set_index("timestamp"))
    st.caption(f"Showing {len(df)} records from the last 10 seconds.")
else:
    st.caption("Click 'Refresh' to load the latest data.")
