print("Welcome Adekunle Oyenekan")
restart = ("Yes")
chances = 3
balance = 10000.29
while chances >= 0:
    pin = int(input("Please Enter Your Pin: \n"))
    if pin == (1234):
        print("Pin Correct\n")
        while restart not in ("n","NO","no","N"):
            print("C \n") #current
            print("S \n") #Savings
            option = input("Choose an Option? \n")
            if option == "S" or "C":
                print("Please Press 1 for balance \n")
                print("Please Press 2 for withdrawal \n")
                print("Please Press 3 for transfer \n")
                print("Please Press 4 for Buy Airtime \n")
                print("Please press 5 to Return card \n")
                option_1 = int(input("Choose an Option? \n"))
                if option_1 == 1:
                    print("Your Balance is N",balance,'\n')
                    restart = input("Would You like to go back? \n")
                    if restart in ("n","NO","no","N"):
                        print("Thank You for Banking With Us!")
                        break
                elif option_1 == 2:
                    option_2 = ("Yes")
                    withdrawal = float(input("How much do you want to withdraw? \nN1000/N5000/N10000/N15000/N20000"'\n'))
                    if withdrawal >= balance:
                        print("Insufficent Fund!\n")
                        print("Your Balance is N",balance)
                        withdrawal = float(input("Please Enter Your Desired Amount? \n"))
                        # restart = input("\nWould You like to go back? \n")
                        if restart in ("n","NO","no","N"):
                            print("Thank You for Banking With Us!")
                            break
                    if withdrawal <= balance:
                        balance = balance - withdrawal
                        print("\nYour Balance is N",balance)
                        restart = input("Would You like to go back? \n")
                        if restart in ("n","NO","no","N"):
                            print("Thank You for Banking With Us!")
                            break
                elif withdrawal > balance:
                    print("Insufficent Fund!\n")
                    restart = ("Yes")
                elif withdrawal == 1:
                    withdrawal = float(input("Please Enter Your Desired Amount? \n"))
            
            elif option == 3:
                transfer = float(input("How Much Would Ypu Like To Transfer? \n"))
                balance = balance - transfer
                print("\nYour Balance is now N",balance)
                restart = input("Would You like to go back? \n")
                if restart in ("n","NO","no","N"):
                    print("Thank You for Banking With Us!")
                    break
            
            elif option == 4:
                airtime = float(input("How Much Airtime would you like to Buy? \n N50/N100/N100/N500/N1000"))
                if airtime in [50,100,500,1000]:
                    balance = balance - airtime
                    print("\nYour balance is now N",balance)
                    restart = input("Would You like to go back? \n")
                    if restart in ("n","NO","no","N"):
                        print("Thank You for Banking With Us!")
                        break

            elif option == 5:
                print("Please wait!\n Take Your card!")
                print("Thank You for Banking With Us!")
                break
            else:
                print("Please Enter a Correct Pin: \n")
                restart = ("Yes")
    elif pin != ("1234"):
        print("Incorrct Pin \n Enter Correct Pin")
        chances = chances - 1
        if chances == 0:
            print("\n Card Blocked!! \n Contact Your bank")
            break
                




                

