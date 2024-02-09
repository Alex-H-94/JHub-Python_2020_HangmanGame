import helpers

wordToGuess = helpers.getRandomWord()
wordObscured = helpers.obscureRandomWord(wordToGuess)
lettersEntered = []
lives = 7
win = False

def updateScreen():
    helpers.updateGallows(lives, wordToGuess)
    print("    Letters entered: " + str(lettersEntered))
    print("    Word To Guess: " + wordObscured)

    return

# Game loop
while (lives > 0):
    updateScreen()
    letter = input("\n    Please enter your next guess: ")

    if letter not in lettersEntered:
        lettersEntered.append(letter)

    if letter in wordToGuess:
        wordObscured = helpers.updateObscured(letter, wordToGuess, wordObscured)
    else:
        lives -= 1

    # The user has removed all * and revealed the word.
    if "*" not in wordObscured:
        win = True
        break

# Update the screen one last time.
updateScreen()

# Player on the game.
if win: print("""
    __________________________________________________
    \n    Congratulations, you win!.
    __________________________________________________
    """)

# Player lost the game.
if lives == 0: print("""
    __________________________________________________
    \n    You lose... The word was '{}'.
    __________________________________________________
    """.format(wordToGuess))
