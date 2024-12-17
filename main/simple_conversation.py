# simple_chatbot.py
import re

class SimpleChatbot:
    def __init__(self):
        self.patterns = {
            r'HI|HELLO': 'Hello!',
            r'HOW ARE YOU|HOWAREYOU': 'I am just a bot, but I am doing great! How about you?',
            r'WHAT IS YOUR NAME': 'I am a simple chatbot created for demonstration purposes.',
            r'BYE|GOODBYE': 'Goodbye! Have a great day!',
        }

    def respond(self, user_input):
        for pattern, response in self.patterns.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                return response
        return "I'm sorry, I don't understand that."

def create_chatbot():
    return SimpleChatbot()
