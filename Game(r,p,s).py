import random
import tkinter as tk
from tkinter import messagebox

# Function to generate the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

# Function to handle user choice and play a round
def play_round(user_choice=None):
    global current_round, timer_id, game_over

    if game_over:
        return

    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None

    if user_choice is None:
        result_text = "Time's up! Computer wins this round!"
        scores['computer'] += 1
        result_label.config(text=result_text)
        score_label.config(text=f"Score - You: {scores['user']} Computer: {scores['computer']}")
    else:
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            result_text = "You win this round!"
            scores['user'] += 1
        elif result == "computer":
            result_text = "Computer wins this round!"
            scores['computer'] += 1
        else:
            result_text = "This round is a tie!"
        
        result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result_text}")
        score_label.config(text=f"Score - You: {scores['user']} Computer: {scores['computer']}")

    current_round += 1
    if current_round > total_rounds:
        display_final_result()
    else:
        start_timer()

# Function to start the timer
def start_timer():
    global timer_id
    timer_label.config(text=f"Time left: {time_per_round} seconds")
    timer_id = root.after(1000, update_timer, time_per_round)

# Function to update the timer
def update_timer(time_left):
    if time_left > 0:
        timer_label.config(text=f"Time left: {time_left - 1} seconds")
        timer_id = root.after(1000, update_timer, time_left - 1)
    else:
        play_round()

# Function to display the final result
def display_final_result():
    global game_over

    if game_over:
        return

    game_over = True

    if scores['user'] > scores['computer']:
        final_result = "Congratulations! You win the game!"
    elif scores['user'] < scores['computer']:
        final_result = "Sorry! The computer wins the game!"
    else:
        final_result = "It's a tie game!"
    
    result_label.config(text=final_result)
    messagebox.showinfo("Game Over", final_result)
    disable_buttons()

# Function to disable all buttons
def disable_buttons():
    start_button.config(state=tk.NORMAL)  # Enable start button for a new game
    for button in choice_buttons:
        button.config(state=tk.DISABLED)

# Function to reset the game
def reset_game():
    global current_round, total_rounds, timer_id, game_over
    current_round = 1
    scores['user'] = 0
    scores['computer'] = 0
    result_label.config(text="")
    score_label.config(text="Score - You: 0 Computer: 0")
    timer_label.config(text="")
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None
    disable_buttons()
    game_over = False

# Function to start the game with the specified number of rounds
def start_game():
    global total_rounds, timer_id
    try:
        total_rounds = int(rounds_entry.get())
        if total_rounds < 1:
            messagebox.showerror("Invalid Input", "Number of rounds should be at least 1.")
            return
        start_button.config(state=tk.DISABLED)
        for button in choice_buttons:
            button.config(state=tk.NORMAL)
        start_timer()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the rounds.")

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.configure(bg='lightblue')  # Set background color

# Initialize scores and round tracking
scores = {'user': 0, 'computer': 0}
current_round = 1
total_rounds = 0
timer_id = None
time_per_round = 10  # seconds
game_over = False

# Create and place widgets
tk.Label(root, text="Enter the number of rounds:", bg='lightblue', font=("Arial", 12)).pack(pady=10)

rounds_entry = tk.Entry(root)
rounds_entry.pack(pady=5)

start_button = tk.Button(root, text="Start Game", command=start_game, bg='green', fg='white', font=("Arial", 12))
start_button.pack(pady=10)

tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg='lightblue', font=("Arial", 12)).pack(pady=10)

button_frame = tk.Frame(root, bg='lightblue')
button_frame.pack(pady=5)

choice_buttons = [
    tk.Button(button_frame, text="Rock", command=lambda: play_round('rock'), state=tk.DISABLED, bg='red', fg='white', font=("Arial", 12)),
    tk.Button(button_frame, text="Paper", command=lambda: play_round('paper'), state=tk.DISABLED, bg='blue', fg='white', font=("Arial", 12)),
    tk.Button(button_frame, text="Scissors", command=lambda: play_round('scissors'), state=tk.DISABLED, bg='yellow', fg='black', font=("Arial", 12))
]

for i, button in enumerate(choice_buttons):
    button.grid(row=0, column=i, padx=5)

result_label = tk.Label(root, text="", bg='lightblue', font=("Arial", 12))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 Computer: 0", bg='lightblue', font=("Arial", 12))
score_label.pack(pady=10)

timer_label = tk.Label(root, text="", bg='lightblue', font=("Arial", 12))
timer_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game, bg='orange', fg='white', font=("Arial", 12))
reset_button.pack(pady=10)

# Run the application
root.mainloop()
