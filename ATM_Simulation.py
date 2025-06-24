def ATM():
    balance = 1000
    correct_pin = ["1234", "5678", "3241"]
    userinput = input("Enter your 4 digit PIN: \n")

    if userinput in correct_pin:
        print("Access granted.")
        while True:
            options = input("balance:1, deposit:2, withdrawal:3, exit:4")
            if options == "1":
                return balance
            elif options == "2":
                deposit = float(input("Deposit: "))
                balance += deposit
            elif options == "3":
                withdraw = float(input("Withdrawal: "))
                if withdraw<=0:
                    print("Not valid ammount")
                elif withdraw>balance:
                    print("Not sufficient amount")
                else:
                    balance -= withdraw
            else:
                break
    else:
        print("Invalid Pin")

print(ATM())