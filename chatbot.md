GPT-OSS-120B Chatbot using Groq API
Project Overview

This project is a simple AI-powered chatbot built using Python and the Groq API. The chatbot interacts with users through the command line and generates intelligent responses using the GPT-OSS-120B language model.

The application continuously accepts user input, sends it to the Groq API, and displays AI-generated responses in real time.

Features
Interactive command-line chatbot
Uses GPT-OSS-120B model
Real-time AI responses
Simple and lightweight implementation
Easy to customize and extend
Exit command to terminate the conversation
Technologies Used
Python 3.x
Groq API
GPT-OSS-120B Large Language Model
Project Structure
project_folder/
│
├── chatbot.py
├── requirements.txt
└── README.md
Prerequisites

Before running the project, ensure the following are installed:

Python 3.8 or above
Internet connection
Groq API Key
Installation
Step 1: Clone the Repository
git clone <repository-url>
cd <repository-folder>
Step 2: Create a Virtual Environment (Optional)

Windows:

python -m venv venv
venv\Scripts\activate

Linux/Mac:

python3 -m venv venv
source venv/bin/activate
Step 3: Install Required Libraries
pip install groq

or

pip install -r requirements.txt
Obtaining a Groq API Key
Visit the Groq Developer Console.
Create an account or log in.
Generate an API key.
Copy the API key.

Replace:

api_key=""

with

api_key="YOUR_GROQ_API_KEY"
Code Explanation
Importing the Library
from groq import Groq

Imports the Groq Python SDK.

Creating the Client
client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)

Authenticates the application using your API key.

Chatbot Header
print("GPT-OSS-120B Chatbot")
print("Type 'exit' to quit\n")

Displays chatbot information when the program starts.

Continuous Chat Loop
while True:

Runs the chatbot continuously until the user exits.

Taking User Input
user_input = input("You: ")

Reads input from the user.

Exit Condition
if user_input.lower() == "exit":
    break

Terminates the chatbot when the user types:

exit
Sending Request to the Model
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "user", "content": user_input}
    ],
    temperature=0.7,
    max_completion_tokens=1024
)
Parameters
Parameter	Description
model	GPT-OSS-120B model
messages	User conversation input
temperature	Controls creativity of responses
max_completion_tokens	Maximum response length
Displaying the Response
print("\nAI:", response.choices[0].message.content)

Extracts and prints the AI-generated response.

Running the Application

Execute:

python chatbot.py
Example Output
GPT-OSS-120B Chatbot
Type 'exit' to quit

You: Hello

AI: Hello! How can I assist you today?

You: What is Artificial Intelligence?

AI: Artificial Intelligence (AI) is the simulation of human intelligence by machines...
Advantages
Fast response generation
Simple implementation
Easy to understand for beginners
Can be expanded into larger AI applications
Future Enhancements
GUI using Tkinter
Web application using Flask
Voice-based chatbot
Chat history storage
User authentication
Multiple AI model support
Database integration
Context-aware conversations
Applications
Educational assistant
Customer support bot
Personal AI assistant
Information retrieval system
Learning and experimentation with LLMs
Troubleshooting
Invalid API Key

Error:

Authentication Error

Solution:

Verify the API key.
Ensure the key is active.
Module Not Found

Error:

ModuleNotFoundError: No module named 'groq'

Solution:

pip install groq
Internet Connection Error

Ensure the system has an active internet connection.

Conclusion

This project demonstrates how to build a basic AI chatbot using Python and the Groq API with the GPT-OSS-120B model. It provides a foundation for developing more advanced conversational AI applications and integrating large language models into real-world software systems.

Author

Developed using Python and Groq GPT-OSS-120B.
