import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")

client = OpenAI(
    api_key=GEMINI_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """



"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=[
            {"role":"system", "content": SYSTEM_PROMPT},
            {"role":"user", "content": "Hey there, I'm mg"}
        ]
        #messages=message_history,
)

raw = response.choices[0].message.content
print(raw)