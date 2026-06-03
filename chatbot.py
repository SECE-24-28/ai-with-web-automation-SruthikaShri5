from groq import Groq

client = Groq(
    api_key="api_key"
)

print("GPT-OSS-120B Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_completion_tokens=1024
    )

    print("\nAI:", response.choices[0].message.content)
    print()
