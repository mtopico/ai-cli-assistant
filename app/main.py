from ollama import chat, Client
from dotenv import load_dotenv
import os

load_dotenv()

client = Client(os.getenv("ollama_host", "http://ollama:11434"))
model = os.getenv("ollama_model", "llama3")
messages = [{
    "role": "system",
    "content": "You are a helpful and friendly assistant. Always provide clear and concise answers to the user's questions."
}]

print("-----------------------------")
print("AI Assistant using Ollama")
print("Type 'exit' to quit")
print("-----------------------------")

personality_input = input("Set the AI persona: ")

if personality_input.strip() and personality_input.strip().lower() != "exit":
    messages[0]["content"] = f"You are a {personality_input} assistant"

if personality_input.strip().lower() == "exit":
    print("-----------------------------")
    print("Exiting the AI Assistant. Goodbye!")
    print("-----------------------------")
    exit()

while True:
    
    user_input = input("Tell me something or exit: ")

    messages.append({
        'role': 'user',
        'content': user_input
    })

    if user_input.lower() == "exit":
        print("-----------------------------")
        print("Exiting the AI Assistant. Goodbye!")
        print("-----------------------------")
        break

    response = client.chat(
        model=model,
        messages= messages
    )

    print("AI Response: " + response["message"]["content"].strip())
