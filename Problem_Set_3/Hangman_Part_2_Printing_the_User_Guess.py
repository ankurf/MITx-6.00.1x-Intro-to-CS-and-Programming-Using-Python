##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/d5d822451677476fbfb0a0f9a14e0501/e59be1242a53477c95a48ac7fab34f4e/
##
##Hangman Part 2 - Printing the User Guess
##
##Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, 
##lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in 
##lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    list=[]
    for i in range(len(secretWord)):
        list.append(secretWord[i])
    a='_'*len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            a=a[:i]+secretWord[i]+a[i+1:]
    return a

##getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])
##getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'])
##getGuessedWord('lettuce', ['w', 'r', 'x', 'd', 'm', 'z', 's', 'q', 'p', 'e'])
##getGuessedWord('coconut', ['y', 'p', 'z', 'n', 'a', 'q', 'w', 'x', 'b', 'h'])
##getGuessedWord('grapefruit', [])
##getGuessedWord('carrot', ['c', 'a', 'w', 'h', 'v', 'r', 'k', 'q', 'j', 'g'])
