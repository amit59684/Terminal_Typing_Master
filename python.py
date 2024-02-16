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
