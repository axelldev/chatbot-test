import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

conversations = dict[str, list]()


def add_message(session_id: str, role: str, content: str):
    if session_id not in conversations:
        conversations[session_id] = []
    conversations[session_id].append({"role": role, "content": content})


def get_conversation_history(session_id: str) -> list:
    if session_id not in conversations:
        return []
    return conversations[session_id]


def get_response(session_id: str) -> str:
    messages = get_conversation_history(session_id)
    response = client.chat.completions.create(model="gpt-5-mini", messages=messages)
    return response.choices[0].message.content
