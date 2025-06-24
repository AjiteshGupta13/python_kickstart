#user input pin, have set of pins
#check balance
#append money or subtract money

def ATM()
    balance = 1000
    correct_pin = ["1234", "5678", "3241"]

  userinput =  input("Enter your 4 digit PIN: ")

    if userinput == correct_pin:
        print("Access granted.")
    else:
        print("Incorrect pin")