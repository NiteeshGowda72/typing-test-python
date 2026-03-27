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


# Main typing test
def typing_test():
    sentences = load_sentences()

    test_duration = 60
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


# Run program
typing_test()
