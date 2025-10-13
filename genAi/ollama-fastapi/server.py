from fastapi import Body, FastAPI
from ollama import Client
from typing import Annotated

app = FastAPI()
client = Client(
    host="http://localhost:11434"
)

@app.get("/")
def home():
    return {"message": "Runs"}

@app.post("/")
def take_input(message: Annotated[str, Body()]):
    response = client.chat(model="gemma2:2b", messages=[{"role":"user", "content": message}])
    return {"response": response.message.content}

# response = client.chat(model="gemma2:2b", messages=[{"role":"user", "content": "Who are you"}])
# print(response.message.content)