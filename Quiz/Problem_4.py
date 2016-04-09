##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/19136f9d4de045fdab0ce099230f5385/af94467328b74ed38f0e901460166d70/
##
## Problem 4
##
##Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) and False otherwise. 
##Do not use Python's built-in reverse function or aString[::-1] to reverse strings.

def isPalindrome(aString):
    '''
    aString: a string
    '''
    if len(aString)<=1:
        return True
    else:
        while(len(aString)>1):
            if aString[0]==aString[len(aString)-1]:
                aString=aString[1:-1]
            else:
                return False
        return True

##isPalindrome('')
##isPalindrome('HLRhUlzr')
##isPalindrome('wCLCw')
##isPalindrome('qgeSmaG')
##isPalindrome('TvdkQkdvT')
##isPalindrome('L')
##isPalindrome('CtC')
##isPalindrome('OMrQHvJVY')
##isPalindrome('JhJJhJ')
##isPalindrome('cRCGfb')


