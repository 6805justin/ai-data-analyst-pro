import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = "data/data.db"

def ensure_db_exists():
    Path("data").mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.close()

def save_df_to_sqlite(df: pd.DataFrame, table_name: str):
    ensure_db_exists()
    conn = sqlite3.connect(DB_PATH)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

def run_query(query: str) -> pd.DataFrame:
    ensure_db_exists()
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def get_schema(table_name: str) -> str:
    ensure_db_exists()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info('{table_name}')")
    columns = cursor.fetchall()
    conn.close()

    lines = [f"Table name: {table_name}", "Columns:"]
    for col in columns:
        lines.append(f'- "{col[1]}" ({col[2]})')
    return "\n".join(lines)