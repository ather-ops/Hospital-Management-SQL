import sqlite3
import pandas as pd
DATABASE_PATH="database/hospital.db"

# Connection Function
def get_connection():
    return sqlite3.connect(DATABASE_PATH)

# Query run function
def run_query(query):
    connection=get_connection()
    try:
        result=pd.read_sql_query(query,connection)
        return result
    finally:
        connection.close()


