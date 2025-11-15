import random
import datetime
import re

class ChatBot:
    def __init__(self):
        self.responses = {
            'greeting': [
                "Hello! How can I assist you?",
                "Hi there! What’s up?",
                "Hey! How can I help?"
            ],
            'goodbye': [
                "Goodbye! Have a nice day!",
                "See you soon!",
                "Take care!"
            ],
            'thanks': [
                "You're welcome!",
                "Anytime!",
                "Glad to help!"
            ],
            'time': [
                "The current time is: {time}",
                "Right now it's {time}",
                "{time}"
            ],
            'default': [
                "I didn't quite get that.",
                "Can you rephrase it?",
                "Interesting... tell me more!"
            ]
        }

        self.patterns = {
            'greeting': r'\b(hello|hi|hey|sup|yo)\b',
            'goodbye': r'\b(bye|goodbye|see you|later)\b',
            'thanks': r'\b(thanks|thank you)\b',
            'time': r'\b(time|current time|what time)\b'
        }

    def get_response(self, message):
        message = message.lower().strip()

        for intent, pattern in self.patterns.items():
            if re.search(pattern, message):
                if intent == "time":
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    return random.choice(self.responses[intent]).format(time=now)
                return random.choice(self.responses[intent])

        return random.choice(self.responses['default'])


bot = ChatBot()

print("\n============================")
print("🤖 INTERACTIVE CHATBOT ACTIVE")
print("============================")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    if user.lower() in ["bye", "exit", "quit"]:
        print("Bot:", random.choice(bot.responses["goodbye"]))
        break

    reply = bot.get_response(user)
    print("Bot:", reply)
