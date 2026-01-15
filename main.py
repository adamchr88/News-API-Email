

# https://newsapi.org/v2/everything?q=tesla&from=2025-12-15&sortBy=publishedAt&apiKey=542bb097db134d80a658ce091628e169

import os
import requests

api_key = os.getenv("secret shhhhhhh")  # set this in your environment
query = "tesla"
from_date = "2022-08-09"

url = (
    "https://newsapi.org/v2/everything"
    f"?q={query}"
    f"&from={from_date}"
    "&sortBy=publishedAt"
    f"&apiKey={api_key}"
)

response = requests.get(url)
print(response.text)
