from config import client, MODEL, banner

banner("CHATBOT")

while True:
    question = input("You: ").strip()

    if question.lower() == "exit":
        break

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": question}
        ],
        temperature=0
    )

    print("Bot:", response.choices[0].message.content.strip())