##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/19136f9d4de045fdab0ce099230f5385/af94467328b74ed38f0e901460166d70/
##
##Problem 8
##
##Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF)

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L

##2
##['a', 'a']

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    newL = []
    for i in L:
        if f(i) == True:
            newL.append(i)
    L[:] = newL
    return len(L)
run_satisfiesF(L, satisfiesF)

