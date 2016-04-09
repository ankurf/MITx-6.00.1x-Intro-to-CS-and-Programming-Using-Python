##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/19136f9d4de045fdab0ce099230f5385/af94467328b74ed38f0e901460166d70/
##
##Problem 6
##
##Write a function to flatten a list. The list contains other lists, strings, or ints. 
##For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]

# Paste your function here
def flatten(l):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    k=[]
    for i in l:
        while isinstance(i, list):
            a=flatten(i)
            k.extend(a)
            break
        else:
            k.append(i)
    return k

##flatten([])
##flatten([[], []])
##flatten([1])
##flatten([[1]])
##flatten([[1], [1]])
##flatten([[1], [2, 3]])
##flatten([[3], [2, 1, 0], [4, 5, 6, 7]])
##flatten([[[1]], [[[5]]]])
##flatten([[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]]])
##flatten([[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]], [[3, 2, 1], [2, 1], [1, [0]]]])

