def ai_chatbot():
    responses = {"hello": "Hi there!",
                 "how are you": "I'm doing great!", "what is your name": "I'm an AI chatbot",
                 "hi": "Hello!", "what is your favorite color": "I like all colors!",
                 "hey": "Hey there!", "good morning": "Good morning!", "good evening": "Good evening!",
                 "what's up": "Not much, how about you?", "who are you": "I'm an AI chatbot!", "what are you": "I'm an AI chatbot!",
                 "who made you": "I was created by an intern!", "are you ai": "Yes, I am an AI!",
                 "what time is it": "It's time to start chasing your dreams!",
                 "tell me the time": "It's time to start chasing your dreams!",
                 "what day is today": "Today is a great day!",
                 "what is today's date": "Today is a random day in 2026!",
                 "help": "You can ask me about Python, AI, machine learning, coding, jokes, greetings, or type bye to exit.",
                 "what is python": "Python is a high-level programming language!",
                 "what is ai": "AI stands for Artificial Intelligence!",
                 "what is machine learning": "Machine learning is a subset of AI that focuses on algorithms that can learn from data!",
                 "what is deep learning": "Deep learning is a type of machine learning that uses neural networks with multiple layers!",
                 "what is a chatbot": "A chatbot is a computer program that simulates conversation with human users!",
                 "what is coding": "Coding is the process of creating instructions for computers to execute!",
                 "tell me a joke": "Why don't scientists trust atoms? Because they make up everything ;)",
                 "bye": "Goodbye!"}

    while True:
        user_input = input("You: ").lower().strip().replace("?", "")

        if user_input == "bye" or user_input == "goodbye" or user_input == "exit":
            print("Bot: Goodbye!")
            break

        reply = responses.get(
            user_input, "I didn't understand that. Type 'help' to see what I can answer.")

        print("Bot:", reply)


ai_chatbot()
