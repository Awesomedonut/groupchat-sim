import tkinter as tk
from chat_gui import ChatGUI

if __name__ == "__main__":
    root = tk.Tk()
    print("hi")
    app = ChatGUI(root)
    root.mainloop()
    print("program running! :D") #ok this only ran when i pressed exit?????

# todo: have option to select character or unselect character for scene -- bot is actually pretty smart here, preliminary testing shows the one thats spoken to responds
# change context? or look at context ai has
# summarize when context window is filled
# prettify ui
# add history?