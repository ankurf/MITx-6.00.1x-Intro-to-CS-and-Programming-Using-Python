##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/sp13_Problem_Set_3/
##
##Hangman Game 1: The Game/Complex Tests
##
##Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. 
##This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three 
##helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    lettersGuessed=[]
    mistakesMade=0
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is "+str(len(secretWord))+" letters long.")
    while not(isWordGuessed(secretWord, lettersGuessed)) and (mistakesMade<8 and mistakesMade>=0):
        print("-------------")
        print("You have "+str(8-mistakesMade)+" guesses left.")
        print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
        guess=raw_input("Please guess a letter: ")
        guess = guess.lower()
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed)))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: "+str(getGuessedWord(secretWord, lettersGuessed)))
        elif guess not in secretWord:
            lettersGuessed.append(guess)
            mistakesMade+=1
            print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
    print("-------------")
    if mistakesMade>7:
        print("Sorry, you ran out of guesses. The word was "+secretWord+".")
    else:
        print("Congratulations, you won!")
        
