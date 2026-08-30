import sqlite3
import pandas as pd
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
Groq_api_key=os.getenv("GROQ_API_KEY")
Client=Groq(
    api_key=Groq_api_key
)


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

# AI assistant Function
def ask_ai(prompt):
    completion = Client.chat.completions.create(
        model="qwen/qwen3.6-27b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content

# Schema Function
def get_table_schema(table_name):
    query=f"""
     PRAGMA table_info({table_name});
     """
    return run_query(query)

# SQL generation Function
def generate_sql(prompt, schema):

    completion = Client.chat.completions.create(

        model="qwen/qwen3.6-27b",

        messages=[
            {
                "role": "system",
                "content": f"""
You are a SQL assistant for a hospital management system.

Generate SQLite SQL queries using only the provided database schema.

Database schema:
{schema}

Rules:
- Return ONLY the SQL query.
- Do not use markdown.
- Do not explain the query.
- Do not invent tables or columns.
- Only generate SELECT queries.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    sql = completion.choices[0].message.content.strip()

    if "<think>" in sql:
        sql = sql.split("</think>")[-1].strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()

# DataBase exection function
def execute_sql(query):

    return run_query(query)

# Data Base Scehma
DATABASE_SCHEMA = """
patients:
...
doctors:
...
appointments:
...
treatments:
...
billing:
...
"""

# Validate Function
def validate_sql(query):
    query = query.strip().lower()
    if not query.startswith("select"):
        return False
    forbidden_keywords = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "create",
        "replace",
        "truncate"
    ]
    for keyword in forbidden_keywords:
        if keyword in query:
            return False
    return True
