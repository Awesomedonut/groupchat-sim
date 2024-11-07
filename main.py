import tkinter as tk
from tkinter import ttk, scrolledtext

class ChatSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Group Chat Simulator")
        self.root.geometry("600x800")
        
        self.setup_gui()
        
    def setup_gui(self):
        self.chat_frame = ttk.Frame(self.root)
        self.chat_frame.pack(expand=True, fill='both', padx=10, pady=5)
        
        self.chat_display = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            width=50,
            height=30
        )
        self.chat_display.pack(expand=True, fill='both', pady=5)
        
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(fill='x', padx=10, pady=5)
        
        self.message_input = ttk.Entry(self.input_frame)
        self.message_input.pack(side='left', expand=True, fill='x', padx=(0, 5))
        
        self.send_button = ttk.Button(
            self.input_frame,
            text="Send",
            command=self.send_message
        )
        self.send_button.pack(side='right')
        
        self.message_input.bind('<Return>', lambda e: self.send_message())
        
    def send_message(self):
        message = self.message_input.get().strip()
        if message:
            self.chat_display.insert(tk.END, f"You: {message}\n")
            self.message_input.delete(0, tk.END)
            self.chat_display.see(tk.END)
            
            self.simulate_ai_response()
    
    def simulate_ai_response(self):
        ai_message = "AI User: This is a simulated response!"
        self.chat_display.insert(tk.END, f"{ai_message}\n")
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatSimulator(root)
    root.mainloop()
