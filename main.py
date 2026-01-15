# https://newsapi.org/v2/everything?q=tesla&from=2025-12-15&sortBy=publishedAt&apiKey=542bb097db134d80a658ce091628e169

import os
import requests
from SendEmail import send_email

api_key = os.getenv("542bb097db134d80a658ce091628e169")  # set this in your environment
query = "tesla"
from_date = "2022-08-09"

url = (
    "https://newsapi.org/v2/everything"
    f"?q={query}"
    f"&from={from_date}"
    "&sortBy=publishedAt"
    f"&apiKey={api_key}"
)

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
