##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/sp13_Problem_Set_3/
##
##Hangman Part 1: Is the Word Guessed
##
##First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, 
##lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord 
##are in lettersGuessed) and False otherwise.

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    list=[]
    for i in range(len(secretWord)):
        list.append(secretWord[i])
    return all(item in lettersGuessed for item in list)
    
##isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
##isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
##isWordGuessed('lettuce', ['f', 'b', 'p', 'h', 'x', 'l', 'n', 'r', 'g', 'd'])
##isWordGuessed('lettuce', ['o', 'c', 'z', 'q', 'w', 'v', 'u', 'b', 'n', 's'])
##isWordGuessed('pineapple', [])
##isWordGuessed('lettuce', ['z', 'x', 'q', 'l', 'e', 't', 't', 'u', 'c', 'e'])


