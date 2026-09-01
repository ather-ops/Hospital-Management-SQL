import sqlite3
import pandas as pd
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
Groq_api_key = os.getenv("GROQ_API_KEY")
Client = Groq(api_key=Groq_api_key)

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

# AI assistant Function
def ask_ai(prompt):
    completion = Client.chat.completions.create(
        model="qwen/qwen3.6-27b",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content

# Schema Function
def get_table_schema(table_name):
    query = f"PRAGMA table_info({table_name});"
    return run_query(query)

# Generate SQL Function
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

EXAMPLES - USE THESE EXACT PATTERNS:
1. "Total revenue" → SELECT ROUND(SUM(amount), 2) FROM billing;
2. "Revenue by payment method" → SELECT payment_status AS "Payment Status", ROUND(SUM(amount), 2) AS Revenue FROM billing GROUP BY payment_status ORDER BY Revenue DESC;
3. "Monthly revenue trend" → SELECT strftime('%Y-%m', bill_date) AS Month, ROUND(SUM(amount), 2) AS Revenue FROM billing GROUP BY strftime('%Y-%m', bill_date) ORDER BY Month DESC;
4. "Doctor generates most revenue" → SELECT d.first_name || ' ' || d.last_name AS doctor_name, ROUND(SUM(t.cost), 2) AS total_revenue FROM doctors d JOIN appointments a ON d.doctor_id = a.doctor_id JOIN treatments t ON a.appointment_id = t.appointment_id GROUP BY d.doctor_id ORDER BY total_revenue DESC LIMIT 1;
5. "Top spending patients" → SELECT p.first_name || ' ' || p.last_name AS name, ROUND(SUM(t.cost), 2) AS total FROM patients p JOIN appointments a ON p.patient_id = a.patient_id JOIN treatments t ON a.appointment_id = t.appointment_id GROUP BY p.patient_id ORDER BY total DESC LIMIT 10;
6. "Doctor with most appointments" → SELECT d.first_name || ' ' || d.last_name AS name, COUNT(a.appointment_id) AS total FROM doctors d JOIN appointments a ON d.doctor_id = a.doctor_id GROUP BY d.doctor_id ORDER BY total DESC LIMIT 1;
7. "Patients with more than 5 appointments" → SELECT p.first_name || ' ' || p.last_name AS name, COUNT(a.appointment_id) AS appointments FROM patients p JOIN appointments a ON p.patient_id = a.patient_id GROUP BY p.patient_id HAVING COUNT(a.appointment_id) > 5 ORDER BY appointments DESC;
8. "Total revenue from completed appointments" → SELECT ROUND(SUM(t.cost), 2) AS total_revenue FROM appointments a JOIN treatments t ON a.appointment_id = t.appointment_id WHERE a.status = 'Completed';
9. "Most common treatments" → SELECT treatment_type AS "Treatment Type", COUNT(*) AS "Total Count" FROM treatments GROUP BY treatment_type ORDER BY "Total Count" DESC;
10. "Treatment generates most revenue" → SELECT treatment_type, ROUND(SUM(cost), 2) AS revenue FROM treatments GROUP BY treatment_type ORDER BY revenue DESC LIMIT 1;
11. "Patients with most appointments" → SELECT p.first_name || ' ' || p.last_name AS "Patient Name", COUNT(a.appointment_id) AS "Appointment Count" FROM patients p JOIN appointments a ON p.patient_id = a.patient_id GROUP BY p.patient_id ORDER BY "Appointment Count" DESC;
12. "Show me pending payments" → SELECT * FROM billing WHERE payment_status = 'Pending';
13. "How much failed payments" → SELECT ROUND(SUM(amount), 2) AS total_failed FROM billing WHERE payment_status = 'Failed';
14. "Patients who cancelled most" → SELECT p.first_name || ' ' || p.last_name AS patient_name, COUNT(a.appointment_id) AS cancellations FROM patients p JOIN appointments a ON p.patient_id = a.patient_id WHERE a.status = 'Cancelled' GROUP BY p.patient_id ORDER BY cancellations DESC LIMIT 1;
15. "Top 5 most expensive treatments" → SELECT treatment_type, ROUND(MAX(cost), 2) AS max_cost, ROUND(AVG(cost), 2) AS avg_cost FROM treatments GROUP BY treatment_type ORDER BY max_cost DESC LIMIT 5;
16. "Patients with no appointments" → SELECT p.first_name || ' ' || p.last_name AS patient_name FROM patients p LEFT JOIN appointments a ON p.patient_id = a.patient_id WHERE a.appointment_id IS NULL;
17. "Show me all doctors" → SELECT doctor_id, first_name, last_name, hospital_branch, specialization, email FROM doctors;
18. "Patients table with 5 rows" → SELECT patient_id, first_name, last_name, email, insurance_number FROM patients LIMIT 5;

Rules:
- Return ONLY the SQL query.
- Do not use markdown.
- Do not explain the query.
- Do not invent tables or columns.
- Only generate SELECT queries.
"""
            },
            {"role": "user", "content": prompt}
        ]
    )
    sql = completion.choices[0].message.content.strip()
    if "<think>" in sql:
        sql = sql.split("</think>")[-1].strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql

# Database Schema
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
- bill_date DATE

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
3. Use doctors.first_name || ' ' || doctors.last_name for doctor names.
4. Use patients.first_name || ' ' || patients.last_name for patient names.
5. Do NOT use doctors.id or patients.id.
6. Use only columns that exist in the schema above.
7. Use JOINs only through the relationships listed above.
"""

# Validate Function
def validate_sql(query):
    query = query.strip().lower()
    if not query.startswith("select"):
        return False
    forbidden = ["insert", "update", "delete", "drop", "alter", "create", "replace", "truncate"]
    for word in forbidden:
        if word in query:
            return False
    return True

# Execute SQL Function
def execute_sql(query):
    if not query or not isinstance(query, str):
        return None, "Query is empty or invalid."
    query = query.strip()

    if not query:
        return None, "Query is empty."
    if not validate_sql(query):
        return None, "Query validation failed. Only SELECT queries allowed."

    try:
        result = run_query(query)
        if result.empty:
            return result, "Query returned no results."
        return result, None
    except Exception as e:
        error_msg = str(e)
        if "no such column" in error_msg:
            return None, "Column not found. Please check the schema."
        elif "no such table" in error_msg:
            return None, "Table not found. Please check the schema."
        elif "syntax error" in error_msg:
            return None, "SQL syntax error. Please rephrase your question."
        else:
            return None, f"Database error: {error_msg}"

# Clean Function
def clean_ai_response(response):
    if "<think>" in response:
        response = response.split("</think>")[-1].strip()
    response = response.replace("```", "").strip()
    return response

# Generate Answer Function
def generate_answer(prompt, result, sql_used=None):
    if result is None or result.empty:
        return "I couldn't find any data matching your question. Try rephrasing or being more specific."

    if isinstance(result, pd.DataFrame):
        result_str = result.to_string()
        rows = len(result)
    else:
        result_str = str(result)
        rows = 1

    completion = Client.chat.completions.create(
        model="qwen/qwen3.6-27b",
        messages=[
            {
                "role": "system",
                "content": """
You are a hospital analytics assistant.

Rules:
- Use EXACT numbers from the result
- Present table data clearly
- Single values = state directly
- Never invent data
- Keep it concise
"""
            },
            {
                "role": "user",
                "content": f"""
Question: {prompt}
SQL: {sql_used if sql_used else 'Not available'}
Result: {result_str}
"""
            }
        ]
    )
    return clean_ai_response(completion.choices[0].message.content.strip())

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

# Main Function
def process_question(user_question):
    sql = generate_sql(user_question, DATABASE_SCHEMA)
    if not sql or "SELECT" not in sql.upper():
        return "I couldn't understand your question. Try asking about patients, doctors, appointments, treatments, or billing."

    result, error = execute_sql(sql)
    if error:
        simple_sql = get_simple_query(user_question)
        if simple_sql:
            result, error = execute_sql(simple_sql)
            if not error:
                sql = simple_sql
    if error:
        return f"Error: {error}\n\nTry: 'Show all patients' or 'Total revenue'"

    return generate_answer(user_question, result, sql)
