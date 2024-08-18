budget = int(input("Enter the initial amount: "))
expense = budget
hist = [] 

def addExp():
    global expense
    desc = input("Enter Description: ")
    add = int(input("Enter expense amount: "))
    addRec = desc + " : " + "-" + str(add) + "\n"
    hist.append(addRec)  
    expense -= add
    print("Current Budget: ", expense)
    menu()

def addInc():
    global expense
    desc = input("Enter Description: ")
    add = int(input("Enter income amount: "))
    addRec = desc + " : " + "+" + str(add) + "\n"
    hist.append(addRec)  
    expense += add
    print("Current Budget: ", expense)
    menu()

def summ():
    print("History:")
    print("".join(hist))
    menu()

def menu():
    print("==============")
    print("Choose action:")
    print("1. Add expense")
    print("2. Add Income")
    print("3. Account Summary")
    print("4. exit")
    choice = int(input("Enter Choice: "))
    print("==============")

    if choice == 1:
        addExp()
    elif choice == 2:
        addInc()
    elif choice == 3:
        summ()

menu()