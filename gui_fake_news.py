import random 
import tkinter as tk

# Data
subjects = [
    "Shahrukh Khan", 
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

# Generate headline
def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)
    
    headline = f"🚨 BREAKING NEWS:\n{subject} {action} {place}!"
    animate_text(headline)

# Animation (fade effect)
def animate_text(new_text):
    label.config(text="")
    fade_in(new_text, 0)

def fade_in(text, i):
    if i <= len(text):
        label.config(text=text[:i])
        root.after(15, lambda: fade_in(text, i+1))

# Button hover effect
def on_enter(e):
    btn.config(bg="#ff4d4d")

def on_leave(e):
    btn.config(bg="#ff1a1a")

# GUI setup
root = tk.Tk()
root.title("Fake News Generator")
root.geometry("600x400")
root.configure(bg="#1e1e2f")

# Title
title = tk.Label(
    root, 
    text="📰 Fake Headline Generator", 
    font=("Helvetica", 18, "bold"), 
    bg="#1e1e2f", 
    fg="white"
)
title.pack(pady=15)

# Card Frame
card = tk.Frame(root, bg="#2b2b3c", bd=0, relief="ridge")
card.pack(pady=20, padx=20, fill="both", expand=True)

# Headline Label
label = tk.Label(
    card,
    text="Click below to generate news!",
    wraplength=500,
    justify="center",
    font=("Helvetica", 14),
    bg="#2b2b3c",
    fg="#f1f1f1",
    padx=20,
    pady=40
)
label.pack(expand=True)

# Generate Button
btn = tk.Button(
    root,
    text="Generate Headline",
    command=generate_headline,
    font=("Helvetica", 12, "bold"),
    bg="#ff1a1a",
    fg="white",
    activebackground="#ff4d4d",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2"
)
btn.pack(pady=10)

btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# Exit Button
exit_btn = tk.Button(
    root,
    text="Exit",
    command=root.quit,
    font=("Helvetica", 10),
    bg="#444",
    fg="white",
    bd=0,
    padx=10,
    pady=5
)
exit_btn.pack(pady=5)

# Run
root.mainloop()