# Convert input to lowercase
# so that uppercase and lowercase work alike


print("Welcome to my chatbot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower().strip()

    # Check for greetings
    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    # Check for user's name question
    elif "your name" in user:
        print("Bot: I am a Python chatbot.")

    # Check for how are you question
    elif "how are you" in user:
        print("Bot: I am fine. Thank you!")

    # Check for thank you
    elif "thank you" in user or "thanks" in user:
        print("Bot: You're welcome!")

    # Exit the chatbot
    elif user in ["bye", "exit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    # Handle unknown input
    else:
        print("Bot: Sorry, I don't understand.")