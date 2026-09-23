# Ai p.py testing
from src.ai import generate_sql

sql = generate_sql("How many patients do we have?")
print(sql)

# assistant.py testing
from src.assistant import process_question
response = process_question(
    "How many patients do we have?"
)
print(response)
