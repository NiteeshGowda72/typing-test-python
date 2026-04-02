import tkinter as tk
import time
import random

# Load sentences


def load_sentences():
    with open("sentences.txt", "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


# Return raw values for accuracy


def calculate_accuracy(choice, user_input):
    correct_chars = 0

    for j in range(min(len(choice), len(user_input))):
        if choice[j] == user_input[j]:
            correct_chars += 1

    total_chars = max(len(choice), len(user_input))
    return correct_chars, total_chars


sentences = load_sentences()
# Main typing test


def typing_test():

    test_duration = 6
    start_time = time.time()

    total_words = 0
    total_correct_chars = 0
    total_chars = 0

    while time.time() - start_time < test_duration:
        choice = random.choice(sentences)

        print("\nType this:")
        print(choice)

        user_input = input("Start typing: ")

        # Word count
        total_words += len(user_input.split())

        # Accuracy (using function)
        correct, total = calculate_accuracy(choice, user_input)
        total_correct_chars += correct
        total_chars += total

    # Final results
    print("\n⏱ Time's up!")

    final_wpm = (total_words / test_duration) * 60

    if total_chars > 0:
        final_accuracy = (total_correct_chars / total_chars) * 100
    else:
        final_accuracy = 0

    print("\n🏆 Final Results")
    print(f"Final WPM: {round(final_wpm, 2)}")
    print(f"Accuracy: {round(final_accuracy, 2)}%")

    total_time_taken = time.time() - start_time
    print(f"Total time: {round(total_time_taken, 2)} sec")


# # Run program
# typing_test()


# Step 1: create window
root = tk.Tk()
root.title("Typing Test")
root.geometry("600x400")

# ✅ Step 2: add label HERE
sentence_label = tk.Label(root, text="Hello", font=("Arial", 16))
sentence_label.pack()

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=10)

current_sentence = ""


def new_sentence():
    global current_sentence
    current_sentence = random.choice(sentences)
    sentence_label.config(text=current_sentence)
    entry.delete(0, tk.END)  # optional but good


def submit():
    user_text = entry.get()
    print(user_text)
    entry.delete(0, tk.END)


start_button = tk.Button(root, text="Start", command=new_sentence)
start_button.pack(pady=10)

button = tk.Button(root, text="Submit", command=submit)
button.pack(pady=10)

# Run app
root.mainloop()
