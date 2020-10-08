import helpers

wordToGuess = helpers.getRandomWord()
wordObscured = helpers.obscureRandomWord(wordToGuess)
lettersEntered = []
lives = 7
win = False

def updateScreen():
    helpers.updateGallows(lives, wordToGuess)
    print("    Word To Guess: " + wordObscured)
    print("    Letters entered: " + str(lettersEntered))

    return

# Game loop
while (lives > 0):
    updateScreen()
    letter = input("\n    Enter a letter: ")

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
    \n    You won! Congratulations!.
    __________________________________________________
    """)

# Player lost the game.
if lives == 0: print("""
    __________________________________________________
    \n    You lost... The word was '{}'.
    __________________________________________________
    """.format(wordToGuess))