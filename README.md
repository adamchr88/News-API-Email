# 📩 NewsAPI → Gmail Notifier (Python)

A simple Python project that fetches the latest news articles from **NewsAPI** using a keyword (example: `tesla`) and sends them to your **Gmail inbox** automatically.

---

## ✅ Features

- Fetches latest articles from NewsAPI
- Builds an email body with:
  - Title
  - Description
  - Link
- Sends the news list to your Gmail using SMTP
- Uses environment variables to keep API keys and passwords secure

---

## 🛠 Requirements

- Python 3.8+
- A **NewsAPI key**
- A **Gmail App Password**

Install the dependency:

```bash
pip install requests
```

---

## 🔐 Environment Variables

Set these environment variables before running the script:

Variable	Description
NEWS_API_KEY	Your NewsAPI key
GMAIL_USER	Your Gmail address
GMAIL_APP_PASSWORD	Your Gmail App Password

✅ Important: Gmail requires an App Password, not your normal password.

---

## ▶️ How to Run

Run your main script:

python main.py


If everything works you should see:

Email sent successfully

⚙️ Changing the Search Query

Inside main() you can change the keyword and date:

query = "tesla"
from_date = "2025-12-15"


query = what you want to search for

from_date = only returns articles after this date

---

## 📦 Suggested Project Structure
newsapi-gmail-notifier/
│
├── main.py
├── SendEmail.py
├── README.md
└── requirements.txt

---

## ⚠️ Common Mistake (Fix)

✅ Correct way to load your NewsAPI key:

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


❌ Incorrect way (this will return None):

os.getenv("547469hvj097db1462g89d58ce0916708e169")


That searches for an environment variable literally named your API key.

---

## 🚀 Future Improvements

Send emails daily using Task Scheduler / cron

Support multiple keywords

Use HTML emails for cleaner formatting

Prevent duplicate articles by storing sent links
