import tkinter as tk
from chat_gui import ChatGUI

if __name__ == "__main__":
    root = tk.Tk()
    # print here???
    app = ChatGUI(root)
    root.mainloop()
    print("program running! :D") #ok this only ran when i pressed exit?????

# todo: have option to select character or unselect character for scene
# change context? or look at context ai has
# summarize when context window is filled
# prettify ui