 CEO Assistant AI

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

```
ceo-assistant-ai/
├── .env                # API key (not committed to GitHub)
├── README.md
├── app.py              # Main application file (entry point)
├── assets/             # Audio files, logos, etc.
│   ├── logo.png
│   └── test_meeting.mp3
├── email_handler.py
├── meeting_transcriber.py
├── report_generator.py
├── task_manager.py
├── requirements.txt
├── tasks.db            # SQLite database (should be gitignored)
└── utils/
    ├── db_utils.py
    └── gpt_chain.py
```

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **OpenAI GPT-3.5 / GPT-4 API**
- **SQLite** for local task storage
- **python-dotenv** for environment variable management

---

## ▶️ How to Run

1. **Clone the Repository**
```bash
git clone https://github.com/Vsandeep-ai-dev/ceo-assistant-ai.git
cd ceo-assistant-ai
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up your `.env` file**
Create a file named `.env` in the root directory and add:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

⚠️ Do **NOT** commit `.env` to GitHub.

5. **Run the app**
```bash
python app.py
```

6. **Run Task Manager Example**
This will test GPT integration and SQLite task saving.
```bash
python task_manager.py
```

---

## ✅ Remove Database from Version Control

```bash
git rm --cached tasks.db
echo "tasks.db" >> .gitignore
git commit -m "Remove tasks.db from version control"
git push origin main
```

---

## ✅ Add `.env.example`

Create a file `.env.example` with:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

Then commit it:
```bash
git add .env.example
git commit -m "Add .env.example"
git push origin main
```

---

## 📸 Optional: Add Project Demo

Create a `screenshots/` folder and add images/GIFs. Then embed them like:

```markdown
![Demo Screenshot](screenshots/demo.png)
```

---

## 🧠 Planned Enhancements

- 🔗 Integration with executive email (Gmail, Outlook)
- 🖥 Web dashboard for non-technical use
- 🔐 Authentication for SaaS setup
- 📝 Editable meeting summaries

---

## 🧪 Testing & Output

All modules are designed to be testable independently. When the API subscription is active, the full GPT response output will be visible.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📝 License

This project is licensed under the MIT License.
