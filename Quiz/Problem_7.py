##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/19136f9d4de045fdab0ce099230f5385/af94467328b74ed38f0e901460166d70/
##
##Problem 7
##
##Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. You are also given a function f, 
##that takes in two integers, performs an unknown operation on them, and returns a value.
##
##Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of 
##two dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:
##
##intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect 
##dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key 
##in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function. 
##Do not implement f inside your dict_interdiff code -- assume it is defined outside.
##difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and 
##not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1

def dict_interdiff(d1,d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    d={}
    for key1, value1 in d1.iteritems():
        for key2, value2 in d2.iteritems():
            if key1==key2:
                c=f(value1,value2)
                d[key1]=c
    g=d.keys()
    for i in g:
        del d1[i]
        del d2[i]
    d4 = dict(d1.items() + d2.items())
    t=tuple(d4)
    return (d,d4)

##dict_interdiff({}, {})
##dict_interdiff({1: 1}, {1: 1})
##dict_interdiff({1: 2}, {2: 1})
##dict_interdiff({0: 0, 2: 5, 5: 2}, {0: 0, 2: 5})
##dict_interdiff({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3})
##dict_interdiff({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3})
##dict_interdiff({1: 1, 2: 2, 3: 3, 4: 4, 5: 4}, {1: 1, 2: 2, 3: 3, 4: 5})
##dict_interdiff({1: 1, 2: 2, 3: 3, 4: 4}, {1: 1, 2: 2, 3: 3, 4: 5, 6: 2})
##dict_interdiff({1: 0, 2: 1, 3: 2, 4: 3, 5: 0}, {1: 1, 2: 2, 3: 3, 4: 5, 6: 2})
##dict_interdiff({1: 1, 2: 0, 3: 0, 4: 0, 6: 0, 7: 0}, {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0})
##dict_interdiff({1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0}, {9: 1, 5: 3, 6: 3, 7: 4})
##dict_interdiff({9: 1, 5: 3, 6: 3, 7: 4}, {1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0})
##dict_interdiff({9: 1, 4: 4, 5: 3, 6: 3}, {1: 1, 2: 2, 3: 3, 4: 5, 8: 4, 10: 0})
##dict_interdiff({4: 4, 5: 3, 6: 3, 8: 4, 9: 1, 10: 0}, {1: 1, 2: 2, 3: 3, 4: 5})


