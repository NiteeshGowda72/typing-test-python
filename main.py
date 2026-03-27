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


def rounds(n):
    scores = []

    for round_num in range(n):
        print(f"\n--- Round {round_num + 1} ---")

        choice = random.choice(sentences)

        input("Press Enter to start...")

        print("\nType this:")
        print(choice)

        start = time.time()
        user_input = input("Start typing: ")
        end = time.time()

        time_taken = end - start

        print(f"⏱ Time taken: {round(time_taken, 2)} seconds")

        compare(choice, user_input)

        wpm = calculate_wpm(user_input, time_taken)
        scores.append(wpm)

        calculate_accuracy(choice, user_input)

    print("\n🏆 Final Results")
    print(f"Best WPM: {round(max(scores), 2)}")
    print(f"Average WPM: {round(sum(scores)/len(scores), 2)}")


rounds(3)
