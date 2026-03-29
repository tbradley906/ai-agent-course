import anthropic

client = anthropic.Anthropic()
conversation_history = []

def chat(user_message: str) -> str:
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=conversation_history
    )

    assistant_reply = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_reply
    })

    return assistant_reply

print(chat("My name is Alex. Remember that."))
print("---")
print(chat("What is 2 + 2?"))
print("---")
print(chat("What's my name?"))
print("---")
print(f"Total messages in history: {len(conversation_history)}")
print(f"Roles: {[m['role'] for m in conversation_history]}")
