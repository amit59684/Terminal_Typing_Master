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
