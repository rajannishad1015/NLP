import spacy

nlp = spacy.blank("en")

print("Simple Chatbot")
print("Type 'bye' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    doc = nlp(user_input.lower())
    words = []

    for token in doc:
        words.append(token.text)
    if "hello" in words or "hi" in words:
        print("Bot: Hello! How can I help you?")

    elif "name" in words:
        print("Bot: My name is SimpleBot.")

    elif "course" in words:
        print("Bot: I can provide information about the course.")

    elif "python" in words:
        print("Bot: Python is a popular programming language.")

    elif "thanks" in words:
        print("Bot: You are welcome!")

    else:
        print("Bot: Sorry, I do not understand your question.")
