conversations = dict[str, list]()


def add_message(session_id: str, role: str, content: str):
    if session_id not in conversations:
        conversations[session_id] = []
    conversations[session_id].append({"role": role, "content": content})


def get_conversation_history(session_id: str) -> list:
    if session_id not in conversations:
        return []
    return conversations[session_id]
