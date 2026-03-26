import time
import random

with open("sentences.txt", "r") as file:
    sentences = file.readlines()
    sentences = [line.strip() for line in file.readlines() if line.strip()]


def rounds(n):
    scores = []

    for round_num in range(n):
        print(f"\n--- Round {round_num + 1} ---")
        choice = random.choice(sentences)

        input("Press Enter to start...")

        print("Type this:")
        print(choice)

        start = time.time()

        user_input = input("")

        end = time.time()

        time_taken = end - start

        # Compare
        if choice.strip() == user_input.strip():
            print("✅ Correct!")
        else:
            print("❌ Incorrect!")

        print(f"⏱ Time taken: {round(time_taken, 2)} seconds")

        # WPM
        words = len(user_input.split())
        if time_taken > 0:
            wpm = (words / time_taken) * 60
        else:
            wpm = 0
        scores.append(wpm)
        print(f"Typing Speed: {round(wpm, 2)} WPM")

        # Accuracy
        correct_chars = 0

        for j in range(min(len(choice), len(user_input))):
            if choice[j] == user_input[i]:
                correct_chars += 1

        total_chars = max(len(choice), len(user_input))
        accuracy = (correct_chars / total_chars) * 100
        print(f"Accuracy: {round(accuracy, 2)}%")

        # Scores

    print("\n🏆 Final Results")
    print(f"Best WPM: {round(max(scores), 2)}")
    print(f"Average WPM: {round(sum(scores)/len(scores), 2)}")


rounds(3)
