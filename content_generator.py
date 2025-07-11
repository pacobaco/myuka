# content_generator.py
import os, openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_content():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    prompt = (
        "Generate a short HTML snippet that includes:\n"
        f"- A header 'Rotating Onion Site'\n"
        f"- A timestamp '{now}'\n"
        "- A brief fictional news update\n"
    )
    resp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}],
        max_tokens=150
    )
    return resp.choices[0].message.content