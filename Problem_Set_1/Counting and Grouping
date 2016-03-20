##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Basic_Problem_Set_1/
##
##Counting and Grouping
##
##A catering company has hired you to help with organizing and preparing customer's orders. You are given a list of each customer's 
##desired items, and must write a program that will count the number of each items needed for the chefs to prepare. The items that a 
##customer can order are: salad, hamburger, and water.
##
##Write a function called item_order that takes as input a string named order. The string contains only words for the items the customer 
##can order separated by one space. The function returns a string that counts the number of each item and consolidates them in the 
##following order: salad:[# salad] hamburger:[# hambruger] water:[# water]
##
##If an order does not contain an item, then the count for that item is 0. Notice that each item is formatted as 
##[name of the item][a colon symbol][count of the item] and all item groups are separated by a space.

def item_order(order):
    s_order=order.split(" ")
    c_s=0
    c_h=0
    c_w=0
    for i in s_order:
        if i=="salad":
            c_s+=1
        if i=="hamburger":
            c_h+=1
        if i=="water":
            c_w+=1
    return "salad:"+str(c_s)+" hamburger:"+str(c_h)+" water:"+str(c_w)
