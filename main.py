import time
import random

with open("sentences.txt", "r") as file:
    sentences = [line.strip() for line in file.readlines() if line.strip()]


def compare(choice, user_input):
    if choice.lower() == user_input.lower():
        print("✅ Correct!")
    else:
        print("❌ Incorrect!")


def calculate_wpm(user_input, time_taken):
    words = len(user_input.split())
    wpm = (words / time_taken) * 60 if time_taken > 0 else 0
    print(f"Typing Speed: {round(wpm, 2)} WPM")
    return wpm


def calculate_accuracy(choice, user_input):
    correct_chars = 0

    for j in range(min(len(choice), len(user_input))):
        if choice[j] == user_input[j]:
            correct_chars += 1

    total_chars = max(len(choice), len(user_input))
    accuracy = (correct_chars / total_chars) * 100

    print(f"Accuracy: {round(accuracy, 2)}%")
    return accuracy


test_duration = 60
start_time = time.time()

scores = []
total_words = 0

while time.time() - start_time < test_duration:
    choice = random.choice(sentences)

    print("\nType this:")
    print(choice)

    start = time.time()
    user_input = input("Start typing: ")
    end = time.time()

    time_taken = end - start

    total_words += len(user_input.split())

    compare(choice, user_input)

    wpm = calculate_wpm(user_input, time_taken)
    scores.append(wpm)

    calculate_accuracy(choice, user_input)


# AFTER LOOP
print("\n⏱ Time's up!")

final_wpm = (total_words / test_duration) * 60

print("\n🏆 Final Results")
print(f"Final WPM: {round(final_wpm, 2)}")
print(f"Best WPM: {round(max(scores), 2)}")
print(f"Average WPM: {round(sum(scores)/len(scores), 2)}")
