
import requests
import json
import os
import datetime
import sys
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
MEMORY_FILE = "memory.json"

app = Flask(__name__)

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

def remember_info(key, value):
    memory = load_memory()
    memory[key.lower()] = value
    save_memory(memory)

def recall_info(key):
    memory = load_memory()
    return memory.get(key.lower(), "I do not remember.")

def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def chat_with_openrouter(prompt):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "openai/gpt-4o",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 200,
            })
        )
        response_data = response.json()
        if "choices" in response_data and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"].strip()
        else:
            return f"API Response Error: {response_data}"
    except Exception as e:
        return f"API Error: {str(e)}"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "").strip().lower()
    if not user_input:
        return jsonify({"response": "Please provide a message."})
    if "remember" in user_input:
        parts = user_input.split("remember", 1)
        if len(parts) > 1:
            details = parts[1].strip().split(" as ", 1)
            if len(details) == 2:
                key, value = details[0].strip(), details[1].strip()
                remember_info(key, value)
                return jsonify({"response": f"Got it! I'll remember that {key} is {value}."})
    if "what is" in user_input or "who is" in user_input or "where is" in user_input:
        key = user_input.replace("what is", "").replace("who is", "").replace("where is", "").strip()
        remembered_value = recall_info(key)
        return jsonify({"response": remembered_value})
    if "time" in user_input:
        return jsonify({"response": f"The current time is {get_current_time()}"})
    if "date" in user_input:
        return jsonify({"response": f"Today's date is {get_current_date()}"})
    response = chat_with_openrouter(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    if sys.stdin.isatty():  # Run interactive mode only if terminal is available
        print("Chatbot: Hello! How can I assist you today? (Type 'quit' to exit)")
        while True:
            try:
                user_input = input("You: ").strip().lower()
            except EOFError:
                break
            if user_input in ["quit", "exit", "bye"]:
                print("Chatbot: Goodbye!")
                break
            response = chat_with_openrouter(user_input)
            print("Chatbot:", response)
    else:
        app.run(host="0.0.0.0", port=5000)
