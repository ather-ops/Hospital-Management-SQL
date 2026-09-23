from src.ai import generate_sql , generate_answer
from src.database import execute_sql

def process_question(question):
    sql=generate_sql(question)
    if not sql:
        return f"I could not generate sql for that sorry"
    result,error=execute_sql(sql)
    if error:
        return f"I couldn't answer that question. {error}"
    return generate_answer(question,result,sql)
