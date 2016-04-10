##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/aa865f2062884d539964080fe9896f13/26b2527b4d7a422ea959d12f75de09eb/
##
##Problem 3
##
##Write a function called dict_invert that takes in a dictionary with immutable values and returns the inverse of the dictionary. 
##The inverse of a dictionary d is another dictionary whose keys are the unique dictionary values in d. The value for a key in the 
##inverse dictionary is a sorted list of all keys in d that have the same value in d.

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    inv_d = {}
    for k, v in d.iteritems():
        inv_d[v] = inv_d.get(v, [])
        inv_d[v].append(k)
        inv_d[v].sort()
    return inv_d
