import sqlite3
import pandas as pd
import os


conn = sqlite3.connect('bluestock_mf.db')

query_path = os.path.join('sql', 'queries.sql')
with open(query_path, 'r') as file:
    sql_script = file.read()

queries = [q.strip() for q in sql_script.split(';') if q.strip()]

print("EXECUTING TASK 6 QUERIES...\n" + "="*40)

for i, query in enumerate(queries, 1):
    print(f"\n--- Query {i} ---")
    try:
        df_result = pd.read_sql_query(query, conn)
        print(df_result.to_string(index=False))
    except Exception as e:
        print(f"Error executing query: {e}")

conn.close()