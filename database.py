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


# Data Base Scehma
DATABASE_SCHEMA = """

DATABASE SCHEMA:

Table: doctors
Columns:
- doctor_id TEXT PRIMARY KEY
- first_name TEXT
- last_name TEXT
- hospital_branch TEXT
- phone_number INT
- year_of_experince INT
- specialization TEXT
- email TEXT

Table: patients
Columns:
- patient_id TEXT PRIMARY KEY
- first_name TEXT
- last_name TEXT
- gender TEXT
- date_of_birth DATE
- contact_number TEXT
- address TEXT
- registration_date DATE
- insurance_provider TEXT
- insurance_number TEXT
- email TEXT

Table: appointments
Columns:
- appointment_id TEXT PRIMARY KEY
- patient_id TEXT
- doctor_id TEXT
- appointment_date DATE
- appointment_time TIME
- reason_for_visit TEXT
- status TEXT

Table: treatments
Columns:
- treatment_id TEXT PRIMARY KEY
- patient_id TEXT
- doctor_id TEXT
- treatment_type TEXT
- treatment_date DATE
- cost REAL

Table: billing
Columns:
- billing_id TEXT PRIMARY KEY
- patient_id TEXT
- treatment_id TEXT
- amount REAL
- payment_status TEXT
- billing_date DATE


RELATIONSHIPS:

- appointments.doctor_id = doctors.doctor_id
- appointments.patient_id = patients.patient_id
- treatments.patient_id = patients.patient_id
- treatments.doctor_id = doctors.doctor_id
- billing.patient_id = patients.patient_id
- billing.treatment_id = treatments.treatment_id


IMPORTANT RULES:

1. Doctors do NOT have a column called name.
2. Patients do NOT have a column called name.
3. Doctors use doctor_id as their identifier.
4. Patients use patient_id as their identifier.
5. Appointments use appointment_id as their identifier.
6. Use doctors.first_name and doctors.last_name for doctor names.
7. Use patients.first_name and patients.last_name for patient names.
8. Do NOT use doctors.id.
9. Do NOT use patients.id.
10. Do NOT use appointments.id.
11. Use only columns that exist in the schema above.
12. Use JOINs only through the relationships listed above.
13. For a full doctor name, use:
   doctors.first_name || ' ' || doctors.last_name
14. For a full patient name, use:
   patients.first_name || ' ' || patients.last_name

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

# Execute SQL Function
def execute_sql(query):
    if not validate_sql(query):
        return None
    return run_query(query)

# Clean function
def clean_ai_response(response):
    if "<think>" in response:
        response = response.split("</think>")[-1].strip()
    response = response.replace("```", "")
    return response.strip()


# Generate Answer Function
def generate_answer(prompt, result):
    completion = Client.chat.completions.create(
        model="qwen/qwen3.6-27b",
        messages=[
            {
                "role": "system",
                "content": """
You are a hospital analytics assistant.
Answer the user's question using only the database result provided.

Rules:
- Do not invent information.
- Do not make up numbers.
- Keep the answer clear and concise.
- Explain the result in natural language.
"""
            },
            {
                "role": "user",
                "content": f"""
User question:
{prompt}
Database result:
{result}
"""
            }
        ]

    )
    response = completion.choices[0].message.content.strip()
    return clean_ai_response(response)
