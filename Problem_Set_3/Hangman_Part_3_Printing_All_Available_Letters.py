##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/sp13_Week_3/sp13_Problem_Set_3/
##
##Hangman Part 3: Printing All Available Letters
##
##Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. 
##This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are 
##not in lettersGuessed.

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    a=string.ascii_lowercase
    for i in range(len(lettersGuessed)):
        a=a.replace(lettersGuessed[i],"")
    return a

##getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
##getAvailableLetters([])
##getAvailableLetters(['a', 'r', 'q', 'f', 'z', 'h'])
##getAvailableLetters(['c', 'w'])
##getAvailableLetters(['l', 'b', 'p', 'u'])
##getAvailableLetters(['p', 'n'])
