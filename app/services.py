import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# This dictionary maps the session_id with the conversation_id (open ai conversation identifier)
conversations = dict[str, str]()


def create_conversation(session_id: str) -> str:
    conversation = client.conversations.create(metadata={"session_id": session_id})
    conversations[session_id] = conversation.id
    return conversation.id


def get_conversation(session_id: str) -> str:
    if session_id not in conversations:
        return create_conversation(session_id)
    return conversations[session_id]


def get_response(session_id: str, message: str) -> str:
    try:
        conversation_id = get_conversation(session_id)
        response = client.responses.create(
            model="gpt-5-mini", input=message, conversation=conversation_id
        )
        return response.output_text
    except Exception as e:
        print(e)
