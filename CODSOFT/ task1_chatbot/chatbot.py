print("=== CODSOFT AI CHATBOT ===")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hi macha! How are you?")

    elif user == "how are you":
        print("Bot: I am fine and happy!")

    elif user == "your name":
        print("Bot: I am CodSoft AI Chatbot.")

    elif user == "who created you":
        print("Bot: Sai Charan created me using Python.")

    elif user == "what are you doing":
        print("Bot: I am chatting with you in terminal.")

    elif user == "good morning":
        print("Bot: Good morning macha! Have a great day.")

    elif user == "good night":
        print("Bot: Good night macha! Sleep well.")

    elif user == "i am sad":
        print("Bot: Don't worry macha. Everything will be okay.")

    elif user == "i am happy":
        print("Bot: That's awesome macha!")

    elif user == "tell me joke":
        print("Bot: Why do programmers hate bugs? Because bugs also hate them!")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "what is ai":
        print("Bot: AI means Artificial Intelligence.")

    elif user == "what is your favorite movie":
        print("Bot: I like sci-fi movies macha!")

    elif user == "what is your favorite food":
        print("Bot: I only eat electricity 😄")

    elif user == "can you help me":
        print("Bot: Yes macha! I will try my best.")

    elif user == "thank you":
        print("Bot: Welcome macha!")

    elif user == "bye":
        print("Bot: Goodbye macha!")
        break

    else:
        print("Bot: Sorry macha, I don't understand.")
        