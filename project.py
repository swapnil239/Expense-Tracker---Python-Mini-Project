# Expense Tracker Project

expensesList = [] # list of expenses in the form of dictionary
print(" Welcome to Expense Tracker : Try to save more and Spend less!")

while True:
    print("=== MENU ===")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = int(input(" Please Enter Your choice: "))

    #  1. Add Expense

    if(choice == 1):
        date = input("On which date did you spend the money?")
        category = input("What was the expense for?")
        description = input("Add a description of the category: ")
        amount = float(input("Enter the total amount you spend: "))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        expensesList.append(expense)
        print("Your Expenses is added successfully done!")

        # 2. View All Expenses

    elif (choice == 2):
            if(len(expensesList) == 0):
                print("No Expenses Yet! Go and spend")
            else:
                print("=== Your Total Expenses so far ===")
                count = 1
            for eachExpenses in expensesList:
             print(f"Your Expenses: {count} -> {eachExpenses["date"]}, {eachExpenses["category"]}, {eachExpenses["description"]}, {eachExpenses["amount"]}")
            count = count + 1


             # 3. View Total Expenses

    elif(choice == 3):
        total = 0
        for eachExpenses in expensesList:
            total = total + eachExpenses["amount"]
        print("\n Total Expenses = ", total)

        # 4. EXIT
    elif(choice == 4):
     print(" THANKYOU! Hope You Will Come Again With More Expenses")
     break

    else:
        print("INVALID CHOICE! TRY AGAIN")




                   
                         



