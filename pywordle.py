# Dependencies
from random import randint
from sys import exit

# OOP
class PyWordle:
    def __init__(self):
        self.gameNumber = 1
        self.score = 0

    def run(self):
        """Starts the game."""
        wordsList = self.read_input_file()
        # show rules on first turn only
        if self.gameNumber == 1:
            self.game_rules()
        self.game_engine(wordsList)
        pass

    def game_engine(self, wordsList):
        """
        Runs the basic functions of the game:
        1. select keyword
        2. gameplay loop
        3. pass results to game_over func
        """

        # select the keyword from wordsList
        random_index = randint(0, len(wordsList)-1)
        keyword = wordsList[random_index]

        # create the grid for visuals
        grid = [["_" for i in range(0,5)] for j in range(0,6)]

        # store guessed words
        guessedWords = []

        # main gameplay loop
        for turn in range(1,7):
            #print the grid on screen
            print("\n\n**********")
            print("Turn", turn)
            print("**********")
            for row in grid:
                print(row)
            print("**********")

            if turn > 1:
                print("\nPrevious Guesses:")
                for word in guessedWords:
                    print(word)

            # collect users guess
            while True:
                print("\nEnter Your guess")
                guess = input(">").upper()
                # make sure the user enters a five letter word
                if len(guess) == 5:
                    break
                else:
                    print("The word you entered is not 5 letters.  Try again.")

            # added guess to guessed word list
            guessedWords.append(guess)

            if guess == keyword:
                for i, letter in enumerate(guess):
                    grid[turn-1][i] = letter.upper()
                for row in grid:
                    print(row)
                self.game_over("WIN", keyword)
            else:
                for i, letter in enumerate(guess):
                    # replace underscore with uppercase letter if it is
                    # correct letter and in correct location
                    if letter in keyword and i is keyword.find(letter):
                        grid[turn-1][i] = letter.upper()
                    # replace underscore with lowercase letter if it is
                    # correct letter but in wrong location
                    elif letter in keyword:
                        grid[turn-1][i] = letter.lower()
                    # continue if letter if is not in keyword at all
                    else:
                        continue

        # player ran out of turns. game over
        self.game_over("LOSE", keyword)
        return

    def game_over(self, status, keyword):
        """
        Displays game over, status (win or lose), and score.
        Allows continue.
        """
        if status == "WIN":
            print("\nCongrats! You Win!")
            self.score+=1
        else:
            print("\nToo Bad! You Lose!")
            print(f"The keyword was '{keyword}'.")

        print("\nGames:", self.gameNumber)
        print("Score:", self.score)

        input("\nPress ENTER to continue.")

        # play again?
        while True:
            print("\nWould you like to play again? Enter 'y' or 'n'")
            choice = input("> ").upper()
            if choice == "Y":
                self.gameNumber+=1
                self.run()
            elif choice == "N":
                exit("Exiting Game. Thank you for playing!")
            else:
                print("Invalid Entry.  Try again.")

    def read_input_file(self):
        """
        Reads list of words from external txt file.
        """
        wordsList = []
        with open("5_letters.txt") as txt:
            for row in txt:
                wordsList.append(row.strip().upper())
        return wordsList

    def game_rules(self):
        print("\n\n**********")
        print("PyWordle")
        print("**********")
        print("\nThe Rules:")
        print("1. Try to guess the 5-letter keyword in 6 turns or less.")
        print("2. If a letter in your guess is in the keyword AND is in the correction location, it is uppercase.")
        print("   If there are multiples of the same letter, the second will be lowercase even if in correct location.")
        print("3. If a letter in your guess is in the keyword but is in the wrong location, it is lowercase.")
        print("4. If a letter in your guess is not in the keyword, it is not displayed.")
        print("5. A list of previous guesses is displayed each turn.")
        print("**********")



if __name__ == "__main__":
    myGame = PyWordle()
    myGame.run()
