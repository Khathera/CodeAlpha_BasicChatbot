print("Simple Chatbot")
print("Type 'bye' to end the chat.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Bot: Hi! Nice to meet you.")
    elif user_input == "how are you":
        print("Bot: I'm doing well, thank you!")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
