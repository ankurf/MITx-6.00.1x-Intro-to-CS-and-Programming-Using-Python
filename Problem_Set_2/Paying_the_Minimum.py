##https://courses.edx.org/courses/course-v1:MITx+6.00.1x_8+1T2016/courseware/Week_2/Problem_Set_2/
##
##Paying the Minimum
##
##Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by 
##the credit card company each month.
##
##The following variables contain values as described below:
##
##balance - the outstanding balance on the credit card
##
##annualInterestRate - annual interest rate as a decimal
##
##monthlyPaymentRate - minimum monthly payment rate as a decimal

total_min_payment=0.00
total_paid=0.00
for n in range(1,13):
    min_payment=round((balance*monthlyPaymentRate),2)
    rem_bal=round((balance-min_payment),2)
    interest=round(((annualInterestRate/12)*rem_bal),2)
    balance=rem_bal+interest
    total_min_payment+=min_payment
    total_paid+=min_payment
    print("Month: %d" %(n))
    print("Minimum monthly payment: "+str(min_payment))
    print("Remaining balance: "+str(balance))
print("Total paid: "+str(total_paid))
print("Remaining balance: "+str(balance))
