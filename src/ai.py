import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
Groq_api_key = os.getenv("GROQ_API_KEY")
Client = Groq(
    api_key=Groq_api_key
)
MODEL_NAME = "qwen/qwen3.8-27b"

# Database schema
DATABASE_SCHEMA = """
Table: doctors
Columns:
- doctor_id
- first_name
- last_name
- hospital_branch
- phone_number
- year_of_experince
- specialization
- email

Table: patients
Columns:
- patient_id
- first_name
- last_name
- gender
- date_of_birth
- contact_number
- address
- registration_date
- insurance_provider
- insurance_number
- email

Table: appointments
Columns:
- appointment_id
- patient_id
- doctor_id
- appointment_date
- appointment_time
- reason_for_visit
- status

Table: treatments
Columns:
- treatment_id
- patient_id
- doctor_id
- treatment_type
- treatment_date
- cost

Table: billing
Columns:
- billing_id
- patient_id
- treatment_id
- amount
- payment_status
- bill_date
"""
# Prompt
SQL_SYSTEM_PROMPT = f"""
You are a SQL assistant for a hospital management system.
Generate SQLite SELECT queries using only this database schema:
{DATABASE_SCHEMA}

Rules:
- Return only the SQL query.
- Only generate SELECT queries.
- Do not invent tables or columns.
- Use valid SQLite syntax.
- Use JOINs only when the required relationship exists.
- For patient names, combine first_name and last_name.
- For doctor names, combine first_name and last_name.
"""
# Aswer sytem prompt
ANSWER_SYSTEM_PROMPT = """
You are a hospital analytics assistant.

Rules:
- Use exact numbers from the database result.
- Never invent information.
- Keep the answer concise.
- If there is one value, state it directly.
- Explain table results clearly.
"""

# Clean Function
def clean_ai_response(response):
    if "<think>" in response:
        response = response.split("</think>")[-1]
    response = response.replace("```sql", "")
    response = response.replace("```", "")
    response = response.strip()
    if response.lower().startswith("sql"):
        response = response[3:].strip()
    return response

# Generate sql
def generate_sql(question):
    completion = Client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SQL_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            }
        ],
        reasoning_effort="none"
    )
    return clean_ai_response(
        completion.choices[0].message.content
    )
# Generate answer
def generate_answer(question, result, sql):
    result_text = result.to_string()
    completion = Client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": ANSWER_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
Question: {question}
SQL:
{sql}
Database result:
{result_text}
"""
            }
        ],
        reasoning_effort="none"
    )
    return clean_ai_response(
        completion.choices[0].message.content
    )
