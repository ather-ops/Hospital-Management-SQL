import sqlite3
import pandas as pd
import os

from groq import Groq
from dotenv import load_dotenv


DATABASE_PATH = "database/hospital.db"

# Connection Function
def get_connection():
    return sqlite3.connect(DATABASE_PATH)

# Query run function
def run_query(query):
    connection = get_connection()
    try:
        result = pd.read_sql_query(query, connection)
        return result
    finally:
        connection.close()


# Schema Function
def get_table_schema(table_name):
    query = f"PRAGMA table_info({table_name});"
    return run_query(query)


# Validate Function
def validate_sql(query):
    query = query.strip().lower()
    if not query.startswith("select"):
        return False
    forbidden = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "create",
        "replace",
        "truncate"
    ]
    return not any(word in query for word in forbidden)

def execute_sql(query):
    if not query or not isinstance(query, str):
        return None, "Query is empty or invalid."
    if not validate_sql(query):
        return None, "Only SELECT queries are allowed."
    try:
        result = run_query(query)
        if result.empty:
            return result, "Query returned no results."
        return result, None
    except Exception as e:
        return None, f"Database error: {e}"

# Simple Query Fallback
def get_simple_query(question):
    q = question.lower()
    if "patient" in q and ("count" in q or "how many" in q):
        return "SELECT COUNT(*) AS total_patients FROM patients;"
    if "doctor" in q and ("count" in q or "how many" in q):
        return "SELECT COUNT(*) AS total_doctors FROM doctors;"
    if "appointment" in q and ("count" in q or "how many" in q):
        return "SELECT COUNT(*) AS total_appointments FROM appointments;"
    if "treatment" in q and ("count" in q or "how many" in q):
        return "SELECT COUNT(*) AS total_treatments FROM treatments;"
    if "revenue" in q or "billing" in q:
        return "SELECT ROUND(SUM(amount), 2) AS total_revenue FROM billing;"
    return None
