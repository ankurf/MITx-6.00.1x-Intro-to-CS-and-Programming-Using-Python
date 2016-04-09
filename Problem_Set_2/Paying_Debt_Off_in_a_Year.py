##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Problem_Set_2/
##Paying Debt Off in a Year
##Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.
##
##In this problem, we will not be dealing with a minimum monthly payment rate.
##
##The following variables contain values as described below:
##
##balance - the outstanding balance on the credit card
##
##annualInterestRate - annual interest rate as a decimal

new_bal=balance
monthly_payment=0
while new_bal>0:
    new_bal=balance
    monthly_payment+=10
    for n in range(1,13):
        rem_bal=round((new_bal-monthly_payment),2)
        interest=round(((annualInterestRate/12)*rem_bal),2)
        new_bal=rem_bal+interest
print("Lowest Payment: "+str(monthly_payment))
