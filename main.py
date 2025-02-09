# import google.generativeai as genai
# import time

# # Set your Google Gemini API key
# genai.configure(api_key="AIzaSyCG5cGAvp7ScKGqTFpz9oUbT-Xnd65662I")  # Replace with your actual API key

# def chat_with_gemini(prompt):
#     try:
#         model = genai.GenerativeModel("gemini-pro")  # Use the Gemini model
#         response = model.generate_content(prompt)
#         return response.text.strip()
    
#     except Exception as e:
#         print(f"Google Gemini API Error: {e}")
#         return "An error occurred. Please try again later."

# if __name__ == "__main__":
#     print("Chatbot: Hello! How can I assist you today? (Type 'quit' to exit)")

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit", "bye"]:
#             print("Chatbot: Goodbye!")
#             break

#         response = chat_with_gemini(user_input)
#         print("Chatbot:", response)
# import google.generativeai as genai

# # Set your Google Gemini API key
# genai.configure(api_key="AIzaSyCG5cGAvp7ScKGqTFpz9oUbT-Xnd65662I")  # Replace with your actual API key

# user_memory = {}  # Dictionary to store user data

# def chat_with_gemini(prompt, context=""):
#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(f"{context}\n{prompt}")
#         return response.text.strip()
#     except Exception as e:
#         print(f"Google Gemini API Error: {e}")
#         return "An error occurred. Please try again later."

# if __name__ == "__main__":
#     print("Chatbot: Hello! How can I assist you today? (Type 'quit' to exit)")

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit", "bye"]:
#             print("Chatbot: Goodbye!")
#             break

#         # Check if the user is trying to store data
#         if "remember" in user_input.lower():
#             words = user_input.split()
#             if "number" in user_input.lower():
#                 num = words[-1]  # Assume the last word is the number
#                 user_memory["number"] = num
#                 print("Chatbot: I will remember that your number is", num)
#                 continue
#             elif "wife name" in user_input.lower():
#                 user_memory["wife_name"] = "Shruti Yadav"
#                 print("Chatbot: I will remember that your wife's name is Shruti Yadav.")
#                 continue
        
#         # Handle retrieval
#         if "what is my wife name" in user_input.lower():
#             print(f"Chatbot: Your wife's name is {user_memory.get('wife_name', 'I do not remember.')}")
#             continue
#         if "what was the number" in user_input.lower():
#             print(f"Chatbot: The number you told me was {user_memory.get('number', 'I do not remember.')}")
#             continue

#         # Pass context to API
#         context = "\n".join([f"{key}: {value}" for key, value in user_memory.items()])
#         response = chat_with_gemini(user_input, context)
#         print("Chatbot:", response)
# import google.generativeai as genai
# import json
# import os

# # Set up Google Gemini API
# genai.configure(api_key="AIzaSyCG5cGAvp7ScKGqTFpz9oUbT-Xnd65662I")  # Replace with your actual API key

# MEMORY_FILE = "memory.json"

# # Load memory from a JSON file
# def load_memory():
#     if os.path.exists(MEMORY_FILE):
#         with open(MEMORY_FILE, "r") as file:
#             return json.load(file)
#     return {}

# # Save memory to a JSON file
# def save_memory(memory):
#     with open(MEMORY_FILE, "w") as file:
#         json.dump(memory, file, indent=4)

# # Store user data in memory
# def remember_info(key, value):
#     memory = load_memory()
#     memory[key.lower()] = value  # Convert key to lowercase for consistency
#     save_memory(memory)

# # Retrieve stored data
# def recall_info(key):
#     memory = load_memory()
#     return memory.get(key.lower(), "I do not remember.")

# # Generate response using Google Gemini API
# def chat_with_gemini(prompt, context=""):
#     try:
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(f"{context}\n{prompt}")
#         return response.text.strip()
#     except Exception as e:
#         print(f"Google Gemini API Error: {e}")
#         return "An error occurred. Please try again later."

# if __name__ == "__main__":
#     print("Chatbot: Hello! How can I assist you today? (Type 'quit' to exit)")

#     while True:
#         user_input = input("You: ").strip().lower()
#         if user_input in ["quit", "exit", "bye"]:
#             print("Chatbot: Goodbye!")
#             break

#         # Check if the user wants to remember something
#         if "remember" in user_input:
#             parts = user_input.split("remember", 1)
#             if len(parts) > 1:
#                 details = parts[1].strip().split(" as ", 1)  # Prevent IndexError
#                 if len(details) == 2:
#                     key, value = details[0].strip(), details[1].strip()
#                     remember_info(key, value)
#                     print(f"Chatbot: Got it! I'll remember that {key} is {value}.")
#                 else:
#                     print("Chatbot: Please use the format 'Remember [key] as [value]'.")
#             else:
#                 print("Chatbot: Please provide information to remember, e.g., 'Remember my name as Avinash Kumar'.")
#             continue

#         # Check if the user is asking for remembered information
#         if "what is" in user_input or "who is" in user_input or "where is" in user_input:
#             key = user_input.replace("what is", "").replace("who is", "").replace("where is", "").strip()
#             remembered_value = recall_info(key)
#             print(f"Chatbot: {remembered_value}")
#             continue

#         # Pass context from memory to API for better responses
#         memory = load_memory()
#         context = "\n".join([f"{key}: {value}" for key, value in memory.items()])
#         response = chat_with_gemini(user_input, context)
#         print("Chatbot:", response)



# import requests
# import json
# import os
# import datetime

# # OpenRouter API Key
# API_KEY = "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"

# # Memory file for storing user data
# MEMORY_FILE = "memory.json"

# # Load stored memory
# def load_memory():
#     if os.path.exists(MEMORY_FILE):
#         with open(MEMORY_FILE, "r") as file:
#             return json.load(file)
#     return {}

# # Save memory to JSON file
# def save_memory(memory):
#     with open(MEMORY_FILE, "w") as file:
#         json.dump(memory, file, indent=4)

# # Store user data dynamically
# def remember_info(key, value):
#     memory = load_memory()
#     memory[key.lower()] = value  # Store in lowercase for consistency
#     save_memory(memory)

# # Retrieve stored information
# def recall_info(key):
#     memory = load_memory()
#     return memory.get(key.lower(), "I do not remember.")

# # Handle basic queries (date, time, math)
# def handle_basic_queries(user_input):
#     user_input = user_input.lower()

#     if "time" in user_input:
#         return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
    
#     if "date" in user_input or "today's date" in user_input:
#         return f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}."

#     try:
#         # Check if user input is a mathematical expression
#         if any(char.isdigit() for char in user_input):
#             result = eval(user_input)
#             return f"The answer is {result}."
#     except Exception:
#         pass  # Ignore errors and let OpenRouter handle it

#     return None  # Let AI handle it if not recognized

# # Generate chatbot response with OpenRouter API
# def chat_with_openrouter(prompt, context=""):
#     try:
#         response = requests.post(
#             url="https://openrouter.ai/api/v1/chat/completions",
#             headers={
#                 "Authorization": f"Bearer {API_KEY}",
#                 "Content-Type": "application/json"
#             },
#             data=json.dumps({
#                 "model": "openai/gpt-4o",
#                 "messages": [
#                     {"role": "system", "content": context},  # Inject stored memory
#                     {"role": "user", "content": prompt}
#                 ]
#             })
#         )
        
#         response_data = response.json()
        
#         # Debugging: Print full API response if an error occurs
#         if "choices" not in response_data:
#             print("API Response Error:", response_data)
#             return "I'm having trouble accessing my knowledge. Please try again later."

#         return response_data["choices"][0]["message"]["content"].strip()

#     except Exception as e:
#         print(f"OpenRouter API Error: {e}")
#         return "An error occurred. Please try again later."

# if __name__ == "__main__":
#     print("Chatbot: Hello! How can I assist you today? (Type 'quit' to exit)")

#     while True:
#         user_input = input("You: ").strip().lower()
#         if user_input in ["quit", "exit", "bye"]:
#             print("Chatbot: Goodbye!")
#             break

#         # Handle basic queries first (date, time, math)
#         basic_response = handle_basic_queries(user_input)
#         if basic_response:
#             print("Chatbot:", basic_response)
#             continue

#         # Check if the user wants to store information
#         if "remember" in user_input:
#             parts = user_input.split("remember", 1)
#             if len(parts) > 1:
#                 details = parts[1].strip().split(" as ", 1)
#                 if len(details) == 2:
#                     key, value = details[0].strip(), details[1].strip()
#                     remember_info(key, value)
#                     print(f"Chatbot: Got it! I'll remember that {key} is {value}.")
#                 else:
#                     print("Chatbot: Please use the format 'Remember [key] as [value]'.")
#             else:
#                 print("Chatbot: Please provide information to remember, e.g., 'Remember my name as Avinash Kumar'.")
#             continue

#         # Check if the user is recalling stored data
#         if "what is" in user_input or "who is" in user_input or "where is" in user_input:
#             key = user_input.replace("what is", "").replace("who is", "").replace("where is", "").strip()
#             remembered_value = recall_info(key)
#             print(f"Chatbot: {remembered_value}")
#             continue

#         # Load memory and pass it as context for better responses
#         memory = load_memory()
#         context = "\n".join([f"{key}: {value}" for key, value in memory.items()])
        
#         # Generate response using OpenRouter API
#         response = chat_with_openrouter(user_input, context)
#         print("Chatbot:", response)


# import requests
# import json
# import os
# import datetime

# # OpenRouter API Configuration
# API_KEY = "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"
# MEMORY_FILE = "memory.json"

# # Load memory from a JSON file
# def load_memory():
#     if os.path.exists(MEMORY_FILE):
#         with open(MEMORY_FILE, "r") as file:
#             return json.load(file)
#     return {}

# # Save memory to a JSON file
# def save_memory(memory):
#     with open(MEMORY_FILE, "w") as file:
#         json.dump(memory, file, indent=4)

# # Store user data
# def remember_info(key, value):
#     memory = load_memory()
#     memory[key.lower()] = value
#     save_memory(memory)

# # Retrieve stored data
# def recall_info(key):
#     memory = load_memory()
#     return memory.get(key.lower(), "I do not remember.")

# # Get current date and time
# def get_current_time():
#     return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def get_current_date():
#     return datetime.datetime.now().strftime("%Y-%m-%d")

# # Generate a response using OpenRouter AI
# def chat_with_openrouter(prompt):
#     try:
#         response = requests.post(
#             url="https://openrouter.ai/api/v1/chat/completions",
#             headers={
#                 "Authorization": f"Bearer {API_KEY}",
#                 "Content-Type": "application/json",
#             },
#             data=json.dumps({
#                 "model": "openai/gpt-4o",  # Switch to "mistralai/mistral-7b-instruct" if credits are low
#                 "messages": [{"role": "user", "content": prompt}],
#                 "max_tokens": 200,  # Limit token usage to avoid hitting limits
#             })
#         )

#         response_data = response.json()

#         if "choices" in response_data and len(response_data["choices"]) > 0:
#             return response_data["choices"][0]["message"]["content"].strip()
#         else:
#             return f"API Response Error: {response_data}"

#     except Exception as e:
#         return f"API Error: {str(e)}"

# # Main chatbot loop
# if __name__ == "__main__":
#     print("Chatbot: Hello! How can I assist you today? (Type 'quit' to exit)")

#     while True:
#         user_input = input("You: ").strip().lower()

#         if user_input in ["quit", "exit", "bye"]:
#             print("Chatbot: Goodbye!")
#             break

#         if "remember" in user_input:
#             parts = user_input.split("remember", 1)
#             if len(parts) > 1:
#                 details = parts[1].strip().split(" as ", 1)
#                 if len(details) == 2:
#                     key, value = details[0].strip(), details[1].strip()
#                     remember_info(key, value)
#                     print(f"Chatbot: Got it! I'll remember that {key} is {value}.")
#                 else:
#                     print("Chatbot: Please use the format 'Remember [key] as [value]'.")
#             continue

#         if "what is" in user_input or "who is" in user_input or "where is" in user_input:
#             key = user_input.replace("what is", "").replace("who is", "").replace("where is", "").strip()
#             remembered_value = recall_info(key)
#             print(f"Chatbot: {remembered_value}")
#             continue

#         if "time" in user_input:
#             print(f"Chatbot: The current time is {get_current_time()}")
#             continue

#         if "date" in user_input:
#             print(f"Chatbot: Today's date is {get_current_date()}")
#             continue

#         response = chat_with_openrouter(user_input)
#         print("Chatbot:", response)
import requests
import json
import os
import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")
MEMORY_FILE = "memory.json"


response = requests.get(
    "https://openrouter.ai/api/v1/models",
    headers={"Authorization": f"Bearer {API_KEY}"}
)

print(response.json()) 
# Load memory from a JSON file
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    return {}

# Save memory to a JSON file
def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

# Store user data
def remember_info(key, value):
    memory = load_memory()
    memory[key.lower()] = value
    save_memory(memory)

# Retrieve stored data
def recall_info(key):
    memory = load_memory()
    return memory.get(key.lower(), "I do not remember.")

# Get current date and time
def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

# Generate a response using OpenRouter AI
def chat_with_openrouter(prompt):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "openai/gpt-4o",  # Switch to "mistralai/mistral-7b-instruct" if credits are low
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 200,  # Limit token usage to avoid hitting limits
            })
        )

        response_data = response.json()

        if "choices" in response_data and len(response_data["choices"]) > 0:
            return response_data["choices"][0]["message"]["content"].strip()
        else:
            return f"API Response Error: {response_data}"

    except Exception as e:
        return f"API Error: {str(e)}"

# Main chatbot loop
if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you today? (Type 'quit' to exit)")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        if "remember" in user_input:
            parts = user_input.split("remember", 1)
            if len(parts) > 1:
                details = parts[1].strip().split(" as ", 1)
                if len(details) == 2:
                    key, value = details[0].strip(), details[1].strip()
                    remember_info(key, value)
                    print(f"Chatbot: Got it! I'll remember that {key} is {value}.")
                else:
                    print("Chatbot: Please use the format 'Remember [key] as [value]'.")
            continue

        if "what is" in user_input or "who is" in user_input or "where is" in user_input:
            key = user_input.replace("what is", "").replace("who is", "").replace("where is", "").strip()
            remembered_value = recall_info(key)
            print(f"Chatbot: {remembered_value}")
            continue

        if "time" in user_input:
            print(f"Chatbot: The current time is {get_current_time()}")
            continue

        if "date" in user_input:
            print(f"Chatbot: Today's date is {get_current_date()}")
            continue

        response = chat_with_openrouter(user_input)
        print("Chatbot:", response)
