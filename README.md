# 🤖 CEO Assistant AI

An AI-powered assistant for CEOs that transcribes meetings, extracts tasks, and generates reports using OpenAI’s GPT models. It automates the management workflow, giving leaders more time to focus on decision-making.

---

## 🚀 Features

- ✅ **Meeting Transcription** – Convert audio recordings into readable meeting summaries.
- ✅ **Task Extraction** – Automatically identify and save action items from summaries.
- ✅ **Task Storage** – Save and manage tasks in an SQLite database.
- ✅ **Report Generation** – Auto-generate reports using GPT from stored data.
- ✅ **Email Handling** – (Planned) Manage executive emails using GPT-powered summaries.
- ✅ **Modular Codebase** – Clean Python architecture for future expansion.

---

## 📁 Project Structure
ceo-assistant-ai/
├── .env # API key (not committed to GitHub)
├── README.md
├── app.py # Main application file (entry point)
├── assets/ # Audio files, logos, etc.
│ ├── logo.png
│ └── test_meeting.mp3
├── email_handler.py
├── meeting_transcriber.py
├── report_generator.py
├── task_manager.py
├── requirements.txt
├── tasks.db # SQLite database
└── utils/
├── db_utils.py
└── gpt_chain.py

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **OpenAI GPT-3.5 / GPT-4 API**
- **SQLite** for local task storage
- **python-dotenv** for environment variable management

---
🔧 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Vsandeep-ai-dev/ceo-assistant-ai.git
cd ceo-assistant-ai
2. Add API Key to .env
Create a .env file in the root of the project:

ini
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
⚠️ Important: Do NOT share your .env file or commit it to GitHub.

3. Install Dependencies
Make sure you have Python 3.11+ installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
4. Run Task Manager Example
This will test GPT integration and SQLite task saving.

bash
Copy
Edit
python task_manager.py
🧠 Planned Enhancements
🔗 Integration with executive email (Gmail, Outlook)

🖥 Web dashboard for non-technical use

🔐 Authentication for SaaS setup

📝 Editable meeting summaries

🧪 Testing & Output
All modules are designed to be testable independently. When the API subscription is active, the full GPT response output will be visible.

📜 License
This project is licensed under the MIT License.

Let me know once you've added it — or if you're ready to start Project 2 now!
