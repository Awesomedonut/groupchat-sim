from character import Character
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()


api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)
# model = genai.GenerativeModel("gemini-1.5-flash")
# print(model.generate_content("tell me a joke").text)

class APIHandler:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        self.is_available = True

    def initialize_chat_for_character(self, character: Character):
        if self.is_available and self.model:
            character.set_chat_history(self.model.start_chat())

    def get_response(self, character: Character, prompt: str) -> str:
        if not self.is_available:
            return "(Gemini API not available)"
        
        try:
            response = character.chat_history.send_message(prompt)
            return response.text
        except Exception as e:
            print(f"Error getting AI response: {e}")
            return "(Error generating response)" 