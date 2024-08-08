import nltk
from nltk.tokenize import word_tokenize

# Ensure you have downloaded the necessary NLTK resources
nltk.download('punkt')

def respond(user_input):
    # Define keywords for specific responses
    greetings = ["hello", "hi", "hey", "greetings"]
    farewell = ["bye", "goodbye", "see you", "farewell"]
    thanks = ["thank you", "thanks", "thx"]
    weather = ["weather", "forecast", "sunny", "rain"]
    time = ["time", "clock", "hour", "minute"]
    hobbies = ["hobby", "hobbies", "interest", "interests"]
    food = ["food", "eat", "meal", "dinner", "lunch"]
    movies = ["movie", "film", "cinema", "watch"]

    # Define a dictionary of responses
    responses = {
        "how are you": "I'm just a bunch of code, but I'm doing great! How about you?",
        "what is your name": "I'm K-P103, your friendly neighborhood chatbot!",
        "tell me a joke": "Why did the computer go to therapy? It had too many bytes!",
        "what can you do": "I can chat with you, tell jokes, discuss movies, and more!",
        "what is the weather": "I wish I could tell you, but I don't have access to live data. Maybe check your favorite weather app?",
        "what time is it": "I'm not sure about the current time, but your device should have the answer!",
        "thank you": "No problem! I'm here to assist you with anything you need.",
        "what are your hobbies": "I enjoy sifting through data, learning new algorithms, and making human friends!",
        "what is your favorite food": "I don't eat, but I hear pizza is a big hit among humans.",
        "recommend a movie": "I recommend 'The Matrix'—a classic for anyone interested in the world of technology and AI!",
        "default": "That's interesting! Can you tell me more or rephrase your question?"
    }

    # Tokenize and normalize the input
    words = word_tokenize(user_input.lower())

    # Check for greetings
    if any(word in words for word in greetings):
        return "Hello there! What's on your mind today?"

    # Check for farewells
    if any(word in words for word in farewell):
        return "Farewell! Hope to chat with you soon."

    # Check for gratitude
    if any(word in words for word in thanks):
        return "You're very welcome! Let me know if there's anything else I can assist with."

    # Check for weather inquiry
    if any(word in words for word in weather):
        return "I don't have live weather updates, but I hope it's nice where you are!"

    # Check for time inquiry
    if any(word in words for word in time):
        return "Unfortunately, I don't have a clock, but your device should have the answer!"

    # Check for hobbies
    if any(word in words for word in hobbies):
        return responses["what are your hobbies"]

    # Check for food inquiry
    if any(word in words for word in food):
        return responses["what is your favorite food"]

    # Check for movie recommendation
    if any(word in words for word in movies):
        return responses["recommend a movie"]

    # Check for known responses
    for key in responses:
        if key in user_input.lower():
            return responses[key]

    # Return the default response if no known phrases are detected
    return responses["default"]

def main():
    print("Welcome to K-P103! Type 'bye' to exit.")
    while True:
        # Get user input
        user_input = input("You: ")

        # Break loop if the user wants to exit
        if user_input.lower() == "bye":
            print("K-P103: Goodbye! Have a great day!")
            break

        # Get the response from the chatbot
        response = respond(user_input)

        # Print the bot's response
        print(f"K-P103: {response}")

if __name__ == "__main__":
    main()

