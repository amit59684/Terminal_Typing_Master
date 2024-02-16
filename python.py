def load_words_from_json(category):
    try:
        with open(WORD_LIST_FILE, 'r') as file:
            word_list = json.load(file)
            words = word_list.get(category, [])
            print(f"Loaded words for '{category}': {words}")
            return words
    except FileNotFoundError:
        print("Word list file not found.")
        sys.exit()
    except json.decoder.JSONDecodeError:
        print("Error decoding JSON in the word list file.")
        sys.exit()


def get_user_input():
    return input("Type the words exactly as shown. Press 'Ctrl + Q' to quit.\n")

def main():
    print("Welcome to Terminal Typing Master!")

    # Get username
    username = input("Enter your username: ")

    while True:
        print("\nMenu:")
        print("1. Start Typing Test")
        print("2. Show Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            # Display available categories
            print("Available Categories:")
            try:
                with open(WORD_LIST_FILE, 'r') as file:
                    word_list = json.load(file)
                    categories = list(word_list.keys())
                    print(', '.join(categories))
            except FileNotFoundError:
                print("Word list file not found.")
                sys.exit()

            # Choose typing category
            category = input("Enter the typing category: ")
            words = load_words_from_json(category)

            # Check if the category exists
            if not words:
                print(f"'{category}' is not a valid category. Please choose a different one.")
                continue

            # Start typing test
            start_time = time.time()
            typed_words = get_user_input().split()
            end_time = time.time()

            # Calculate WPM
            time_taken = end_time - start_time
            words_typed = len(typed_words)
            wpm = int((words_typed / time_taken) * 60)

            print(f"\nWords Typed: {words_typed}")
            print(f"Time Taken: {time_taken:.2f} seconds")
            print(f"Words Per Minute (WPM): {wpm}")

            # Update and show leaderboard
            update_leaderboard(username, wpm)
            show_leaderboard()

        elif choice == '2':
            # Show leaderboard
            show_leaderboard()

        elif choice == '3':
            print("Thank you for using Terminal Typing Master. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

