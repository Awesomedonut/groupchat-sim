import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
from character import CharacterManager
from api_handler import APIHandler
import random

class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Group Chat Simulator")
        self.root.geometry("600x800")
        
        self.character_manager = CharacterManager()
        self.api_handler = APIHandler()
        
        self._initialize_characters()
        self._setup_gui()

    def _initialize_characters(self):
        for character in self.character_manager.characters:
            self.api_handler.initialize_chat_for_character(character)

    def _setup_gui(self):

        self.chat_frame = ttk.Frame(self.root)
        self.chat_frame.pack(expand=True, fill='both', padx=10, pady=5)
        
        self.chat_display = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            width=50,
            height=30
        )
        self.chat_display.pack(expand=True, fill='both', pady=5)
        
        # bottom controls frame
        self.controls_frame = ttk.Frame(self.root)
        self.controls_frame.pack(fill='x', padx=10, pady=5)
        

        self.input_frame = ttk.Frame(self.controls_frame)
        self.input_frame.pack(fill='x', pady=(0, 5))
        
        self.message_input = ttk.Entry(self.input_frame)
        self.message_input.pack(side='left', expand=True, fill='x', padx=(0, 5))
        
        self.send_button = ttk.Button(
            self.input_frame,
            text="Send",
            command=self.send_message
        )
        self.send_button.pack(side='right')
        

        self.exit_frame = ttk.Frame(self.controls_frame)
        self.exit_frame.pack(fill='x')
        
        self.exit_button = ttk.Button(
            self.exit_frame,
            text="Exit",
            command=self.exit_program,
            style='Exit.TButton'
        )
        self.exit_button.pack(side='right')
        

        self.message_input.bind('<Return>', lambda e: self.send_message())
        

        style = ttk.Style()
        style.configure('Exit.TButton', foreground='red')

    def exit_program(self):
        self.root.quit()
        self.root.destroy()

    def send_message(self):
        message = self.message_input.get().strip()
        if message:
            self.chat_display.insert(tk.END, f"You: {message}\n")
            self.message_input.delete(0, tk.END)
            self.chat_display.see(tk.END)
            
            threading.Thread(
                target=self.generate_ai_responses,
                args=(message,),
                daemon=True
            ).start()

    def generate_ai_responses(self, message):
        responding_characters = self.character_manager.get_random_responders()
        
        for character in responding_characters:
            try:
                prompt = character.get_prompt(message, self.chat_display.get('1.0', tk.END))
                response = self.api_handler.get_response(character, prompt)
                self.root.after(0, self.update_chat_display, character.name, response)
                threading.Event().wait(random.uniform(0.5, 2.0))
            except Exception as e:
                print(f"Error getting response from {character.name}: {e}")

    def update_chat_display(self, username, message):
        self.chat_display.insert(tk.END, f"{username}: {message}\n")
        self.chat_display.see(tk.END)