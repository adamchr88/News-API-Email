News-to-Email Automator 📧
A Python script that fetches the latest news articles on a specific topic (like Tesla) using the NewsAPI and automatically sends a curated digest to your Gmail inbox.

Features
Dynamic Search: Query any topic using the NewsAPI everything endpoint.

Automated Emailing: Uses Python's smtplib and SSL for secure email transmission.

Clean Formatting: Parses JSON responses into a readable text format including titles, descriptions, and direct links.

Environment Safety: Uses environment variables to keep your API keys and passwords secure.

🛠 Setup & Installation
1. Prerequisites
Python 3.x

A NewsAPI Key (Free for developers)

A Gmail account with 2-Step Verification enabled.

An App Password for Gmail (do not use your regular login password).

2. Install Dependencies
Bash

pip install requests
3. Configure Environment Variables
To keep your credentials safe, this script reads from your system's environment variables. Set them as follows:

Windows (PowerShell):

PowerShell

$env:NEWS_API_KEY="your_news_api_key_here"
$env:GMAIL_USER="yourname@gmail.com"
$env:GMAIL_APP_PASSWORD="your_16_digit_app_password"
Mac/Linux:

Bash

export NEWS_API_KEY="your_news_api_key_here"
export GMAIL_USER="yourname@gmail.com"
export GMAIL_APP_PASSWORD="your_16_digit_app_password"
🚀 How to Use
Clone the repository or copy the script to a file named main.py.

Adjust the search parameters in the main() function:

Python

query = "tesla"
from_date = "2025-12-15"
Run the script:

Bash

python main.py
📂 Project Structure
main.py: The primary script containing the logic for fetching news and sending emails.

SendEmail.py: (Optional/Legacy) Logic for the mailer if kept as a separate module.
