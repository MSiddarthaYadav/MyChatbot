def simple_chatbot():
    """
    A simple dictionary-based chatbot.
    """
    responses = {
        "hello": "Hello! How can I help you today?",
        "how are you": "I am a bot, so I am always doing great!",
        "what is your name": "I am a simple chatbot.",
        "bye": "Goodbye! Have a great day!"
    }

    print("Simple Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print(f"Simple Chatbot: {responses[user_input]}")
            if user_input == "bye":
                break
        else:
            print("Simple Chatbot: I am not sure how to respond to that.")

if __name__ == "__main__":
    simple_chatbot()