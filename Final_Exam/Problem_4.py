##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/aa865f2062884d539964080fe9896f13/26b2527b4d7a422ea959d12f75de09eb/
##
##Problem 4
##
##Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.
##assume L is not empty
##assume 0 < n <= len(L)
##This function returns a list of all possible sublists in L of length n without skipping elements in L. 
##The sublists in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller 
##index being at the front of the list.

def getSublists(L,n):
    m=[]
    for i in range(len(L)-n+1):
        l = []
        for j in range(n):
            l.extend([L[i+j]])
        m.append(l)
    return m
print(getSublists([10, 4, 3, 4, 7, 7],4))
