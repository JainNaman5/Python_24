expenses = []

def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            del expenses[expenseToRemove]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

def printMenu():
    print("Please choose from one of the following options:")
    print("1. Add a new Expense")
    print("2. Remove an Expense")
    print("3. List all Expenses")

def listExpenses():
    print("\nHere is a list of your expenses:")
    print("------------------------------------")
    for counter, expense in enumerate(expenses):
        print(f"#{counter} - {expense['amount']} - {expense['category']}")
    print("\n")

if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")

        if optionSelected == "1":
            try:
                amountToAdd = float(input("How much was this expense? "))
                category = input("What category was this expense? ")
                addExpense(amountToAdd, category)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif optionSelected == "2":
            removeExpense()
        elif optionSelected == "3":
            listExpenses()
        else:
            print("Invalid input. Please try again.")