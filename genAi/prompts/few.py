# Few shot prompting
# Examples are provided
# Improve the output quality as well

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")

client = OpenAI(
    api_key=GEMINI_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """

You're an helpful AI assistant, You help only with coding question

OUTPUT FORMAT-
    {{
        "code":"string" | None,
        "isCodingQuestion": Boolean
    }}

Example-
    Q: what is 2+3
    A: {{
        "code": null,
        "isCodingQuestion": false,
        "message": "Sorry, i can only help you with coding questions
    }}

    Q: write a function to add two numbers
    A: {{
        "code": def addTwo(a: int, b: int):
        return a + b
        print(addTwo(2, 3)),
        "isCodingQuestion": true
    }}
    
    

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    n=1,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": "Write an essay on Seasons",
            # no o/p

            # "content": "write a function to find tsa of cube in typescript", 
            # gives o/p since coding question
        },
    ],
)

print(f"\n\n\n {response.choices[0].message.content} \n\n")

