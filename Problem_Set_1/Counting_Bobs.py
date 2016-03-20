##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Basic_Problem_Set_1/
##
##Counting Bobs
##
##Assume s is a string of lower case characters.
##
##Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', 
##then your program should print
##
##Number of times bob occurs is: 2

count=0
x=0
y=3
for n in range(len(s)-2):
    s1=s[x:y]
    x+=1
    y+=1
    if s1=="bob":
        count+=1
print("Number of times bob occurs is: "+str(count))
 
