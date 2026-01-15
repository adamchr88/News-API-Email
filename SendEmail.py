# Sends latest NewsAPI articles to your Gmail inbox
# Install: pip install requests

import os
import requests
import smtplib
import ssl

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GMAIL_USER = os.getenv("GMAIL_USER")
GMAIL_APP_PASSWORD = (os.getenv("GMAIL_APP_PASSWORD") or "").replace(" ", "")

RECEIVER_EMAIL = GMAIL_USER  # send to yourself


def send_email(subject: str, body: str):
    if not GMAIL_USER or not GMAIL_APP_PASSWORD:
        raise RuntimeError("Missing GMAIL_USER or GMAIL_APP_PASSWORD environment variables.")

    host = "smtp.gmail.com"
    port = 465

    message = (
        f"Subject: {subject}\n"
        f"To: {RECEIVER_EMAIL}\n"
        f"From: {GMAIL_USER}\n\n"
        f"{body}"
    )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_USER, RECEIVER_EMAIL, message)


def get_news(query: str, from_date: str):
    if not NEWS_API_KEY:
        raise RuntimeError("Missing NEWS_API_KEY environment variable.")

    url = (
        "https://newsapi.org/v2/everything"
        f"?q={query}"
        f"&from={from_date}"
        "&sortBy=publishedAt"
        f"&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url, timeout=20)
    data = response.json()

    if data.get("status") != "ok":
        raise RuntimeError(f"NewsAPI error: {data.get('message', 'Unknown error')}")

    return data.get("articles", [])


def build_email_body(articles):
    if not articles:
        return "No articles found."

    parts = []
    for article in articles[:10]:
        title = article.get("title") or ""
        desc = article.get("description") or ""
        link = article.get("url") or ""

        if title.strip():
            parts.append(title)
            if desc.strip():
                parts.append(desc)
            if link.strip():
                parts.append(link)
            parts.append("")

    return "\n".join(parts).strip()


def main():
    query = "tesla"
    from_date = "2025-12-15"

    articles = get_news(query, from_date)
    body = build_email_body(articles)

    send_email(subject=f"News Update: {query}", body=body)
    print("Email sent successfully")


if __name__ == "__main__":
    main()
