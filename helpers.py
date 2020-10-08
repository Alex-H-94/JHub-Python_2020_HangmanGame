import random
import os

def getRandomWord():
    # Get a random word from the text file and return it.
    wordList = open('./words.txt', 'r').read()
    wordList = wordList.split()

    randomNo = random.randint(0, len(wordList))
    randomWord = wordList[randomNo]

    return randomWord

def obscureRandomWord(wordToGuess):
    obsecuredWord = "*" * len(wordToGuess)
    return obsecuredWord

def updateGallows(lives, wordToGuess):
    # Clear the screen and re-draw the gallows depending on the lives(guesses) left.
    x = 7 - lives
    bodyParts = ["O", "/", "|", "\\", "|", "/", "\\"]
    bpToShow = ["", "", "", "", "", "", ""]

    replace = lambda a,b,s: a[:s]+b+a[s+len(b):]
    bpToShow = replace(bodyParts, bpToShow, x)

    clear = lambda: os.system('cls')
    clear()

    return print("""
    ========== HANGMAN ==========
    Author: Huetson AH [OCT 2020]
    
          |-----|
          |     {}
          |    {}{}{}
          |     {}
          |    {} {}
          |
         _|\\_________
      
    You have {} guess(es) left.
    """.format(bpToShow[0], bpToShow[1], bpToShow[2], bpToShow[3], bpToShow[4], bpToShow[5], bpToShow[6], lives))

def updateObscured(userInput, wordToGuess, wordObscured):

    for location, char in enumerate(wordToGuess):
        if char == userInput:
            wordObscured = wordObscured[:location] + userInput + wordObscured[location + 1:]

    return wordObscured