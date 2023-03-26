# Calculating a mortgage loan with monthly compound interest
# By C. Calongne, 01/14/2019
# Pseudocode & Python with Strings, M3Lab2_student.py
# Write the statements requested in Steps 1-7 below
# 
# See the examples in the provided code
# Use structured programming and indent your code.
# Programmer Name: *****Bryce Redden****

print()
print("Welcome to the Mortgage Loan Calculator.")
print("****************************************")

# ****Instructions****
# Complete Steps 1-7 in the comments below. The remaining comments explain the logic.
# Customers can check a variety of loans and interest rates. When finished, type quit

# Step 1: add an input statement to enter name or type quit to exit
print('Enter name or type quit to exit:')
name = input()




# Step 2: add a while loop to keep asking for a name until the user types quit
while name != 'quit':
    


    # Step 3: declare two variables for loan and interest, like months below, 
    # convert them to float, and ask the user to input their values to the screen. 

    loan= float(input('What loan amount do you need?'))
    interest= float(input('What interest rate do you need?'))



    months = float(input("How many months will it take to repay your loan? "))

    print("***************************************************************")
    print (name, "you requested an estimate on a loan for {0:.2f}" .format(loan))

    # Step 4: add a print statement to display the interest and # of months
    print("Your interest is {0:.2f}" .format(interest))
    print("And You'll have {0:.2f} months." .format(months))
    
    print("*******************************************************************************")
    print("Here are the rates for simple interest, compound interest, and monthly interest", "\n") 

    # calculate the rate for one month's interest + payment by adding 1 to a month's interest
    interest_rate = float((interest/12)+1)

    # calculate the compound interest per payment period by raising the  
    # monthly payment to the negative power of total months
    compound_interest = float(1-((interest/12)+1) ** -months)


    # Step 5: print the interest_rate and compound_interest to the display screen
    print ("Your Simple interest rate will be: ")
    print ( interest_rate)
    print ("Your compound intrest rate will be: ")
    print ( compound_interest)



    # calculate the monthly interest based on the compound interest
    monthly_interest = float((interest/12)/ compound_interest)
    print("Your monthly interest rate will be: ")
    print( monthly_interest, "\n")

    # calculate the monthly loan payment with monthly compound interest
    payments = float(loan * monthly_interest)
   


    # Step 6: write a print statement that displays the monthly payments to two decimal points
    # Tip: use the 0:.2f format from an earlier example, only for the payments
    print("Your monthly payment will be:")
    print("{0:.2f}".format(payments))
    

    print("*******************************************")
    # Step 7: add an input statement to enter name or type quit to exit

    

    
elif name == 'quit':
    print("Thank you for using the Mortgage Loan Calculator")
