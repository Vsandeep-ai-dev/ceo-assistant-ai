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
## ▶️ How to Run

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file:

   - Create a file named `.env`
   - Add your OpenAI key like this:

     ```
     OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     ```

4. Run the app:

   ```bash
   python app.py
   ```

---

### ✅ 4. Remove Database from Version Control

You don’t want to track your local `tasks.db` in Git. Run this:

```bash
git rm --cached tasks.db
echo "tasks.db" >> .gitignore
git commit -m "Remove tasks.db from version control"
git push origin main
```

---

### ✅ 5. Optional: Add a Project Demo (GIF / Screenshot)

📸 Add a `screenshots/` folder and include demo images or a short video showing:

- Task extraction from text
- Meeting transcription
- Auto report generation

Then embed the image in your `README.md` like this:

```markdown
![Demo Screenshot](screenshots/demo.png)
```

---

Once you do this, your project will look professional, polished, and ready for recruiters, contributors, or clients. Let me know once you're done — I’ll review it again! 🚀

🔧 What You Can Improve or Add:

Installation Instructions (Missing):
Add this section under setup Instructions
pip install -r requirements.txt
2..env Example (Optional but Recommended):
Add this so others know what variable they need to define:
# .env
OPENAI_API_KEY=your_openai_api_key_here
3.# .env
OPENAI_API_KEY=your_openai_api_key_here
python app.py

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


## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License
This project is licensed under the MIT License.



