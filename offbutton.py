import tkinter as tk
from tkinter import messagebox

class OffButton:
    def __init__(self, master):
        self.master = master
        master.title("Off Button")
        
        # Set window size and position
        master.geometry("300x200+500+300")
        
        # Create and place the button
        self.off_button = tk.Button(master, text="Turn Off", command=self.turn_off, height=2, width=10)
        self.off_button.pack(expand=True)

    def turn_off(self):
        if messagebox.askokcancel("Confirm", "Are you sure you want to turn off?"):
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = OffButton(root)
    root.mainloop()
