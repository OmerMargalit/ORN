import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("ORN Client Window")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set client window dimensions and center it on the screen
width = 800
height = 600
x = (screen_width - width) // 2
y = (screen_height - height) // 2
root.geometry("{}x{}+{}+{}".format(width, height, x, y))

# Add background image
background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create label and entry for search query
search_label = tk.Label(root, text="What would you like to search for?", font=("Helvetica", 16), bg="#2c3e50", fg="white")
search_label.pack(pady=50)

search_entry = tk.Entry(root, font=("Helvetica", 16))
search_entry.pack(pady=20)

# Save query when user clicks search button or presses Enter
def save_query(event=None):
    query = search_entry.get()
    print("Client search for: " + query)
    #play_sound()

# Add search button and bind it to save_query function
search_button = tk.Button(root, text="Search", font=("Helvetica", 16), command=save_query, bg="#3498db", fg="white")
search_button.pack(pady=20)
search_button.bind("<Return>", save_query)

# Add function to play sound when search button or Enter is pressed
def play_sound():
    os.system('aplay ClickSound.wav &')

root.mainloop()
