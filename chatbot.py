def chatbot(user_input):
    user_input = user_input.lower().strip()

    if "hello" in user_input or user_input == "hi" or user_input == "hii" or "hey" in user_input:
        return "Hello! I'm ManeeBot. How can I help you?"
    elif "machine learning" in user_input or "what is ml" in user_input:
        return "ML is a subset of AI where machines learn from data!"
    elif "artificial intelligence" in user_input or "what is ai" in user_input:
        return "AI is the simulation of human intelligence by machines!"
    elif "who made you" in user_input or "creator" in user_input:
        return "I was created by Maneesha, a B.Tech AIML student!"
    elif "python" in user_input:
        return "Python is used in AI, data science and web development!"
    elif "name" in user_input:
        return "I'm ManeeBot, built with Python!"
    elif "how are you" in user_input:
        return "I'm running great! Thanks for asking!"
    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? Light attracts bugs! haha"
    elif "college" in user_input or "university" in user_input:
        return "Bahra University, Shimla Hills, Himachal Pradesh!"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Keep coding!"
    else:
        return "I don't know that yet. Try asking about AI or ML!"

print("=" * 35)
print("     Welcome to ManeeBot!")
print("=" * 35)

while True:
    user = input("You: ")
    if user.strip() == "":
        continue
    response = chatbot(user)
    print("ManeeBot:", response)
    if "bye" in user.lower() or "exit" in user.lower():
        break