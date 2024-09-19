import random

DictOfCountries = [
    "SINGAPORE",
    "MALAYSIA",
    "BRUNEI",
    "THAILAND",
    "MYANMAR",
    "CAMBODIA",
    "LAOS",
    "VIETNAM",
    "PHILIPPINES",
    "INDONESIA",
    "RUSSIA",
    "INDIA",
    "BRAZIL",
    "CHINA",
    "FRANCE",
    "SPAIN",
    "ENGLAND",
    "SWEDEN",
    "MONGOLIA",
    "ARGENTINA",
    "NIGERIA",
    "MOROCCO",
    "GERMANY",
    "GHANA",
]
RandomCountry = random.choice(DictOfCountries)

def main():
    # Welcoming the player into the game
    print("\n")
    print("Welcome to Hangman Game: Guess The Country Edition!")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    # First print the amount of letters in the country to be guessed
    for _ in RandomCountry:
        print("_", end=" ")
    print("\n")

    AmountOfWrongTries = 0
    ListOfGuessedLetters = []

    while True:
        # Now the guess a letter for the Country
        PlayerGuessedLetter = input("GUESS A LETTER: ").upper()

        # If the player is right
        if PlayerGuessedLetter in RandomCountry:
            ListOfGuessedLetters.append(PlayerGuessedLetter)
            x = f"{'\n'.join(DrawHangman(AmountOfWrongTries))}"
            print(x)
            # Show the player the guessed letters so they should not guess the same letters
            print(f"[The letters that you have guessed: {PrintGuessedLetters(ListOfGuessedLetters)} ]")
            AmountOfCorrectlyGuessedLetters = counter(ListOfGuessedLetters,RandomCountry)
            country = RandomCountry
            for char in country:
                if char in ListOfGuessedLetters:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
            print()
            if AmountOfCorrectlyGuessedLetters == len(RandomCountry):
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠤⢴⣖⠲⠶⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠞⣩⣴⠚⢿⣟⣿⣻⣟⡿⣶⣬⣉⡒⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣹⣯⣻⡿⣿⣷⣌⣿⣞⡷⣯⣟⡷⣯⣿⡿⣿⣄⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⣾⣯⣿⣽⡿⣾⣟⡷⣯⣟⡷⣯⣟⣷⡿⣟⣿⣽⡟⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⣾⣿⣻⣟⡾⣽⣳⢿⣟⣷⢯⣟⡷⣯⡿⣽⣿⣟⣿⡇⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢣⠟⠺⠷⠯⣟⣷⣯⣟⣾⣟⡿⣾⣽⡿⣽⣿⣟⠾⠟⠛⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢩⣴⣾⢿⣶⣶⣤⣑⣛⣿⠯⠿⠷⢯⣿⣛⣥⣴⣶⣶⣶⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣶⠹⢿⣆⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⣧⡈⠙⠷⣦⣩⢧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠏⣠⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣻⢶⣤⣤⣭⣟⣻⠿⣿⣿⣿⣿⢿⣟⣯⣵⣶⣿⣯⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣯⢿⣽⣻⣿⠿⠿⠿⠷⠾⠶⠿⠿⠿⢿⣽⣾⣽⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣟⣯⣿⣷⣼⣉⣉⣩⡶⠩⠄⡈⢉⣵⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡻⣿⡿⣽⣧⡳⣕⢲⢒⠒⢆⡠⣲⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠋⢳⡄⠀⠀⠀⠀⠀⠀⠀⢀⡇⠐⠝⠻⢯⣿⣷⣶⣶⣶⣶⣾⣿⠟⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢻⠀⠀⠀⠀⢀⣀⡤⢾⣇⠀⠈⠢⡀⠉⠉⠉⠉⠉⠛⠉⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⢺⣀⣤⢖⣺⣭⣶⢾⡿⣿⣷⣤⡀⠈⠂⠄⡀⠀⠀⠀⠀⢀⣠⣶⣿⣷⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⢀⣠⣼⡇⢒⠁⢷⣾⢿⣽⣳⢯⡿⣽⣳⢯⡿⣿⣶⣦⣤⣠⣅⣠⣴⣶⣿⢿⣻⢿⡽⣯⣟⡿⣿⣿⣲⠦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⣠⡾⠿⠾⠽⠾⠤⠥⠬⢿⣟⡾⣽⢯⣟⡷⣯⢿⣽⣳⢯⣟⣿⡻⠏⢿⣯⢷⣯⣟⣯⢿⡽⣷⢯⣟⡷⣯⣟⡿⣶⣦⣭⡙⣳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⢀⢟⣾⡏⠀⠀⠀⠀⠀⠀⢀⠈⣿⣻⣽⣻⢾⡽⣯⣟⡾⣽⣻⢾⠟⠁⠀⠈⠙⣿⢾⡽⣞⣿⡽⣯⣟⣾⣻⢷⣯⣟⡷⣯⡟⣱⡿⣷⣮⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⣸⣼⠋⠀⠀⠐⠒⠒⠒⠂⠒⠊⢿⣷⢯⣟⣯⣟⡷⣯⣟⣷⠟⠁⠀⠀⠀⠀⠀⠉⣿⣻⡽⣾⡽⣷⢯⣷⣻⣟⡾⣽⣻⡝⢰⣿⣽⣳⣟⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⡇⣿⣇⠀⠀⢀⢀⢀⣀⣀⣐⣈⣸⡿⣯⣟⡾⣽⣻⢷⡻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢟⣷⣻⡽⣟⣾⣳⢯⣟⣷⡟⢀⣿⡷⣯⣷⣻⢾⣿⢷⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⢸⣷⣿⣿⡀⠀⠁⠉⢉⡁⠀⠀⠈⣿⣟⡷⣯⣟⡷⡯⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣻⣟⡾⣽⣯⣟⣾⠁⢸⣯⣟⡷⣯⣟⡿⣞⣿⡆⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⢸⣿⣿⢻⡇⠀⠀⠂⠒⠒⠒⠒⢺⣿⡽⣯⢷⡯⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣯⣟⣷⣻⢾⠃⠀⣾⣿⣽⣻⢷⣯⣟⣯⣟⣿⡄⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⣼⣿⡟⠈⠧⠤⣤⣤⣤⣤⣤⠤⠞⣿⣿⣽⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣾⣳⢯⡏⠀⡀⣿⣿⡾⣽⣻⢾⡽⣾⡽⣾⣿⣄⠀⠀⠀⠀⠀")
                print("⠀⢠⣟⣿⣀⣤⣴⡿⣿⢿⣆⠀⠀⠀⠀⣿⢘⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣽⡿⠀⢠⢰⣿⣟⣿⣯⣟⣯⣟⣷⣻⡽⣿⣿⣆⠀⠀⠀⠀")
                print("⠀⣼⣿⠹⣿⣽⣳⣟⣿⣟⣿⣷⣄⠀⣼⣿⡾⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⡅⠀⠎⢸⣿⣟⡾⣷⣟⡾⣽⢾⣽⣻⢷⣻⣞⣷⡀⠀⠀")
                print("⢀⣿⣿⡆⣿⣞⣷⣻⡿⣾⣟⣾⣿⢿⣿⣿⡿⣽⣻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣷⡘⠀⣾⣿⡿⣽⣻⢾⣟⣯⢿⡾⣽⢯⡿⣽⣿⣧⠀⠀")
                print("⢸⣿⣿⣿⣿⣽⢾⣿⡽⠟⠊⠉⠀⠸⣷⣿⣟⡷⣯⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣟⣷⣻⣇⢀⡏⢻⣿⣯⣟⣯⢿⣾⢿⡽⣯⡿⣽⢷⣻⣿⡆⠀")
                print("⢸⣿⣿⣽⣻⣿⠛⠁⠀⠀⠀⠀⠀⠀⢹⣿⢯⡿⣽⣻⢾⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣟⣷⣻⢾⣟⣿⣼⠀⠀⠻⣿⣽⡾⣯⢿⣯⣟⡷⣟⣯⣿⣳⢿⣿")
                print("Congratulation! You've Guess The Correct Country 🥳🎉👏🤝👍🌷")
                break
            else:
                continue

        # If the player is wrong
        else:
            ListOfGuessedLetters.append(PlayerGuessedLetter)
            AmountOfWrongTries = AmountOfWrongTries + 1
            x = f"{'\n'.join(DrawHangman(AmountOfWrongTries))}"
            print(x)
            # Show the player the guessed letters so they should not guess the same letters
            print(f"[The letters that you have guessed: {PrintGuessedLetters(ListOfGuessedLetters)} ]")
            country = RandomCountry
            for char in country:
                if char in ListOfGuessedLetters:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
            print()
            if AmountOfWrongTries == 7:
                print("GAMEOVER. Don't Give Up! Try Again💪!!!")
                print(f"The answer is {RandomCountry}")
                break
            else:
                continue


def DrawHangman(AmountOfGuessWrong):
    if AmountOfGuessWrong == 0:
        hangman = ["+======+", "|      ", "|     ", "|      ", "|     ", "|", "==========="]
        return hangman
    elif AmountOfGuessWrong == 1:
        hangman = ["+======+", "|      O", "|      ", "|      ", "|     ", "|", "==========="]
        return hangman
    elif AmountOfGuessWrong == 2:
        hangman = ["+======+", "|      O", "|     / ", "|      ", "|      ", "|", "==========="]
        return hangman
    elif AmountOfGuessWrong == 3:
        hangman = ["+======+", "|      O", "|     /| ", "|      ", "|      ", "|", "==========="]
        return hangman
    elif AmountOfGuessWrong == 4:
        hangman = ["+======+", "|      O", "|     /|へ ", "|      ", "|      ", "|", "==========="]
        return hangman
    elif AmountOfGuessWrong == 5:
        hangman = ["+======+", "|      O", "|     /|へ ", "|      |", "|      ", "|", "==========="]
        return hangman
    elif AmountOfGuessWrong == 6:
        hangman = ["+======+", "|      O", "|     /|へ ", "|      |", "|     /  ", "|", "==========="]
        return hangman
    else:
        hangman = ["+======+", "|      O", "|     /|へ ", "|      |", "|     / へ ", "|", "==========="]
        return hangman


def counter(ListOfGuessedLetters,country):
    counter = 0
    for char in country:
        if char in ListOfGuessedLetters:
            counter += 1
        else:
            continue
    return counter


def PrintGuessedLetters(ListOfGuessedLetters):
    x = " ".join(ListOfGuessedLetters)
    return x


if __name__ == "__main__":
    main()
