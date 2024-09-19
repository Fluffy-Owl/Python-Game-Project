# **HANGMAN GUESS THE COUNTRY**

### Video Demo:  https://youtu.be/7WEM3VlQ1M0

### Description:
### Hello this is my CS50P Final Project: Hangman Guess The Country

*Ideation*

I have always love looking at the world map. So I decided to make a game for my CS50p Project that has something to do with the world map. After some time, I decided to create a hangman game but the word that the user needs to guess is a country. That way, maybe the user might learn about a country's existence through this game. Or just enjoy trying to guess the country's name through a hangman game.

*Planning*

So here is my plan on how I want to code it.
* I need to print out a welcome message for the user into the game
* Have a list of countries to store all the countries' name and use *import random and random.choice* to randomly chose ONE COUNTRY for the game
* The game will be controlled by a while loop. So *while true* the game will keep asking the user for a letter. The game will stop when the country's name is guessed or the number of wrong tries reached 7 times.
While the game is being played, the game will need to show the user the letters that they have guessed, the drawing of the hangman to show them that they are running out of tries, and the blanked letters that they have yet to guess

*The Function*

1. The first function is *DrawHangman(AmountOfGuessWrong)* where the function *DrawHangman* takes an argument of an integer for the amount of tries the user have guessed a wrong letter. So if the *AmountOfGuessWrong* is 0, the function returns a drawing of a gallows. If the *AmountOfGuessWrong* is 1, the function returns a drawing of the gallows with the head. As the *AmountOfGuessWrong* increase, the function returns a more complete drawing of the gallows and the hanged man. Once the *AmountOfGuessWrong* reached 7, a full drawing of a man hanged is drawn and the game end as the user failed to guess the correct country.

2. The second function is *counter(ListOfGuessedLetters,country)* where the function *counter* will take in 2 argument *ListOfGuessedLetters* and *country*. *ListOfGuessedLetters* is a list that stores the letters that is guessed by the user. Argument *country* is the country's name selected for the current game. Then the function returns a counter(an integer) where it will check the amount of letters in the country's name that is in the *ListOfGuessedLetters*'s list. If the number of letters (in the country's name) that is correctly guessed is equal to the *len(RandomCountry)*, the user have correctly guessed the country's name.

3. The last function is *PrintGuessedLetters(ListOfGuessedLetters)* where the function takes in an argument a list of letters that are guessed by the user. The purpose of the function is to eventually print the list of letters the user have guessed so that the user knows his/her previous guesses so they can avoid guessing the same letter in the future.

*How The Game Ends*

So the *while loop* takes care of the game being in the loop, printing out all the things we have mentioned. Including printing the blank spaces excluding the letters that the user have guessed correctly.

The game ends by either:

1. The *AmountOfGuessWrong*(amount of times the user guessed a wrong letter) reached 7, where the hanged man is fully drawn and the while breaks after printing "GAMEOVER. Don't Give Up! Try Again💪!!!"

2. Or the user have guessed all the letters in the country's name where the while loop breaks after printing "Congratulation! You've Guess The Correct Country 🥳🎉👏🤝👍🌷"


This is my very first python project, thank you for reading :)
