## https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Basic_Problem_Set_1/
## Counting Vowels
##
## Assume s is a string of lower case characters.
##
## Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
##
##Number of vowels: 5

count=0
for v in s:
    if (v=="a" or v=="e" or v=="i" or v=="o" or v=="u"):
        count+=1
print("Number of vowels: "+str(count))
