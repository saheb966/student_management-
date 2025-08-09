import tkinter as tk
import random
# Initialize game variables
secret_number = random.randint(1, 100)
attempts = 0
# Function to check the guess
def check_guess():
    global attempts
try:
    guess = (Entry.get())
except ValueError:
    result_label.config(text="Please enter a valid number!")
return
attempts += 1
if guess < secret_number:
    
    result_label.config(text="Too low! Try again.")
elif guess > secret_number:
    result_label.config(text="Too high! Try again.")
else:
    result_label.config(text=f"n Correct! You guessed it in {attempts} tries.")
entry.delete(0, tk.END) # Clear input
# Function to restart the game
def restart_game():
    global secret_number, attempts
secret_number = random.randint(1, 100)
attempts = 0
result_label.config(text="New game started! Guess between 1 and 100.")
# Create main window
root = tk.Tk()
root.title("Guess the Number")
root.geometry("300x200")
# UI elements
title_label = tk.Label(root, text="Guess the Number (1-100)", font=("Arial", 12))
title_label.pack(pady=5)
entry = tk.Entry(root)
entry.pack()
check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack(pady=5)
result_label = tk.Label(root, text="Start guessing!", font=("Arial", 10))
result_label.pack(pady=5)
restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.pack()
# Run the Tkinter event loop
root.mainloop()
