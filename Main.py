import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.ttk import Style

from Quiz_game import question_prompts


# Function to display the current question and choices
def show_question():
    global current_question
    question = question_prompts[current_question]
    qs_label.config(text=question["question"])

    # Display the choices on the buttons
    choices = question["choices"]
    for i in range(2):
        choice_btns[i].config(text=choices[i], state="normal")  # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    global current_question, score
    question = question_prompts[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(question_prompts)))
        feedback_label.config(text="Correct", foreground="Green")
    else:
        feedback_label.config(text="Incorrect", foreground="Red")

    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question += 1
    if current_question < len(question_prompts):
        # If there are more questions, Show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz completed",
                            "Quiz completed! Final score: {}/{}".format(score, len(question_prompts)))
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Deen e ilahi Quiz")
root.geometry("600x500")
style = Style()

# Config the front size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 16))
style.configure("TButton", font=("Helvetica", 14))

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)

qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(2):
    button = ttk.Button(
        root,
        command=check_answer(i)
    )
    button.pack(pady=3)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(question_prompts)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()
