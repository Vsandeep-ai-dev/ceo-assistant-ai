import os
from dotenv import load_dotenv
import sqlite3
from datetime import datetime
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
print("API Key Loaded:", bool(openai.api_key))


# ----------------------
# INITIALIZE DATABASE
# ----------------------
def init_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            source TEXT,
            status TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ----------------------
# ADD TASK TO DB
# ----------------------
def add_task(description, source="meeting", status="pending"):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (description, source, status, created_at)
        VALUES (?, ?, ?, ?)
    ''', (description, source, status, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# ----------------------
# EXTRACT TASKS USING GPT
# ----------------------
def extract_tasks_from_summary(summary_text):
    prompt = f"""
Extract clear, concise task action items from this meeting summary:

\"\"\"{summary_text}\"\"\"

List only the actual tasks as bullet points.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You extract action items from summaries."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )

    result = response.choices[0].message.content.strip()
    task_list = [line.strip("-• ").strip() for line in result.split("\n") if line.strip()]
    return task_list

# ----------------------
# MAIN TEST (Optional)
# ----------------------
if __name__ == "__main__":
    init_db()
    sample_summary = """
    In today’s meeting, we decided to launch the beta version by next Friday. Rahul will handle the UI updates. 
    Priya is responsible for marketing content. Schedule a team check-in on Tuesday.
    """
    tasks = extract_tasks_from_summary(sample_summary)
    for task in tasks:
        print("Saving task:", task)
        add_task(task)
