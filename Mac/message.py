import tkinter as tk
import urllib.request
import random
import threading
import time

# --- Configuration ---

URL = "https://ipgoc.gibranlp.dev/ipgoc"

# --- Functions ---

def fetch_random_message():
    try:
        with urllib.request.urlopen(URL) as response:
            lines = response.read().decode("utf-8").splitlines()
            lines = [line.strip() for line in lines if line.strip()]
            return random.choice(lines)
    except Exception as e:
        return "Te Amo Mucho <3"

def reveal_text(message, label):
    def animate():
        label.config(text="")
        current = ""
        for c in message:
            current += c
            label.config(text=current)
            time.sleep(0.03)  # speed of reveal
    threading.Thread(target=animate).start()

def update_message():
    msg = fetch_random_message()
    reveal_text(msg, message_label)

# --- GUI Setup ---

root = tk.Tk()
root.title("Mensaje de Amor")
root.geometry("500x200")
root.configure(bg="#fff")

message_label = tk.Label(root, text="", font=("Helvetica", 18), wraplength=480, bg="#fff")
message_label.pack(pady=30)

button = tk.Button(root, text="Otro Mensaje", command=update_message, font=("Helvetica", 14), bg="#f08080", fg="white")
button.pack()

# Initial message
update_message()

root.mainloop()
