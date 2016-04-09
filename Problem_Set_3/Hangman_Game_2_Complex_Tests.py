##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/sp13_Problem_Set_3/
##
##Hangman Game 2: Complex Tests
##

def hangman(secretWord):
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
        
    
##hangman(zzz)
##hangman(y)
##hangman(camel)
##hangman(guanabana)
##hangman(senselessness)
##hangman(cheetah)
