print("Welcome Adekunle Oyenekan")
restart = ("Yes")
chances = 3
balance = 10000.29
while chances >= 0:
    pin = int(input("Please Enter Your Pin: \n"))
    if pin == (1234):
        print("Pin Correct\n")
        while restart not in ("n","NO","no","N"):
            print("Current \n")
            print("Savings \n")
            option = input("Choose an Option? \n")
            if option == Savings:
                print("Please Press 1 for balance \n")
                print("Please Press 2 for withdrawal \n")
                print("Please Press 3 for transfer \n")
                print("Please Press 4 for Buy Airtime \n")
                print("Please press 5 to Return card \n")
                # option_1 = int(input("What "))