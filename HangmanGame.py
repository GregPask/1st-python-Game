import random
import time


#Introduce the game and obtain users name.....

print("What is your name?")
name = input()
print("Hello " + str(name) + " and welcome to...")
print()

time.sleep(1)


HANGMANPICS = ['''

  +---+
      |
      |
      |
      |
      |
========== ''','''

  +---+
  O   |
      |
      |
      |
      |
========== ''','''

  +---+
  O   |
  |   |
      |
      |
      |
========== ''','''

  +---+
  O   |
 /|   |
      |
      |
      |
========== ''','''

  +---+
  O   |
 /|\  |
      |
      |
      |
========== ''','''

  +---+
  O   |
 /|\  |
 /    |
      |
      |
========== ''','''

  +---+
  O   |
 /|\  |
 / \  |
      |
      |
========== ''']


words = 'greg alex mum dad james paul john matty liverpool python england programming function hangman'.split()







#This function is fed the long list of wrods and creates a random index to pick a word from it

def getRandomWords(words):
    wordIndex = random.randint(0,len(words)-1)
    randomWord = words[wordIndex]
    return randomWord


#this function displays the Hangman pic board as well as missed letters and blanks

def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print("Missed letters:",end= " ")

    for x in missedLetters:
        print(x, end=",")
    print()

    blanks = "_" * len(secretWord)



    for x in range(len(secretWord)):
        if secretWord[x] in correctLetters:
            blanks = blanks[:x] + secretWord[x] + blanks[x+1:]
    print()

    for x in blanks:
        print(x,end="")
    print()




#This function allows user to take a guess and checks if the guess is valid

def takeAGuess(alreadyGuessed):
    while True:
        print("Take a guess " + str(name) + ":")
        guess = input()


        if len(guess) != 1:
            print("Please choose only 1 letter...")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please choose a letter..")
        elif guess in alreadyGuessed:
            print("You've already guessed this letter matey..")
        else:
            return guess



#this asks user if they want to play again returns true of false
def playAgain():
    print("Do you want to play again? (Yes or No)")
    answer = input().lower().startswith("y")
    return answer



#this starts the game
print("........H A N G M A N........")
print()
print()
print("You will need to guess a random word presented to you\nto many guesses and you will face the Henchmans rope. Good luck!!!")
time.sleep(5)
missedLetters = ""
correctLetters = ""
secretWord = getRandomWords(words)
isGameDone = False





#while true this code executes...... If guess was in secret word checks if user won, also checks if guess is not correct/ end game requirements

while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    guess = takeAGuess(missedLetters + correctLetters)

    if guess in secretWord:
        print("Correct!")
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for x in range(len(secretWord)):
            if secretWord[x] not in correctLetters:
                foundAllLetters = False
                break


        if foundAllLetters:
            print("Well done you guessed the secret word of " + str(secretWord))
            isGameDone = True


#user guesses incorrectly
    else:
        missedLetters = missedLetters + guess
        print("That letter was incorrect, try again!")
        print("Number of missed letters" + str(len(missedLetters)))

        if len(missedLetters) == len(HANGMANPICS) -1:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
            print()
            print("Sorry you failed, the correct answer was " + str(secretWord))
            print()
            isGameDone = True


#If the game is done it will call playAgain() function and return "True" or "False"

    if isGameDone:
        if playAgain():
            print("H A N G M A N")
            missedLetters = ""
            correctLetters = ""
            secretWord = getRandomWords(words)
            isGameDone = False

        else:
            print("Thanks for playing my hangman game!")
            break

#game is done set to true/ calls play again function  else breaks out of loop


