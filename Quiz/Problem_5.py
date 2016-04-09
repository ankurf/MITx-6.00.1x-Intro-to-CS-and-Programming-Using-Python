##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/19136f9d4de045fdab0ce099230f5385/af94467328b74ed38f0e901460166d70/
##
##Problem 5
##
##Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and 
##listB have the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the 
##dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    add=0
    for i in range(0,len(listA)):
        s=listA[i]*listB[i]
        add+=s
    return add
    
##dotProduct([38, 67, 97, 12, 79], [84, 52, -92, 7, 32])
##dotProduct([-31, -14, -57, -79, 13, 98], [32, -93, -37, 65, 78, 42])
##dotProduct([-31, -45, -80, -56, 5, -40, -45], [62, 13, 69, -84, 53, -57, 28])
##dotProduct([39, -9, 72, -12, 37, -37, -17, -63, -53], [91, -64, 52, 15, 31, -83, -64, -10, 18])
##dotProduct([-16, -4, -2, 45, 86, -59, 2, -6], [-71, 86, -69, 35, 72, -71, -22, -58])
##dotProduct([-71], [-46])
##dotProduct([-17, -49, 6, -51, 96], [-84, -92, -15, -44, -58])
##dotProduct([59, -33, 100, -74, -41], [-96, 87, 79, -11, 62])
##dotProduct([9, 13, -77, 40, 34, 78, -3, -66], [-62, -50, 16, -78, 82, -86, 33, 53])
##dotProduct([1, 48, 64, -67], [10, 92, -94, -90])
