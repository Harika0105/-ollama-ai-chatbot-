import ollama

print("🤖 Ollama AI Chatbot")
print("Type 'exit' or 'stop' to end the conversation.\n")

messages = []

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "stop"]:
        print("AI: Goodbye! 👋")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="llama3.2",
        messages=messages
    )

    ai_reply = response["message"]["content"]

    print("AI:", ai_reply)

    messages.append({
        "role": "assistant",
        "content": ai_reply
    })