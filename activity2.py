print("=== Welcome to CITBank ATM ===")
pin = 1234
username = "Carl Timothy"
balance = 1000000
pin2 = int(input("Enter your 4-digit PIN: "))

if not pin2 == pin:
    print("Invalid PIN!")
    exit()
else:
    user = username[0] + ("*" * len(username)) + username[-1]
    print(f"Hello {user}! You have successfully logged in.", "\n")
    while True:
        print(" [1] Check Balance", "\n", "[2] Deposit", "\n", "[3] Withdraw", "\n", "[4] Exit")
        menu = int(input("Choose an option: "))
        if menu == 1:
            print(f"Account Holder: {user}")
            print(f"Current Balance: ₱{balance}", "\n")
        elif menu == 2:
            amount = int(input("Enter amount to deposit: "))
            if amount == 100 or amount == 200 or amount == 500 or amount == 1000:
                balance += amount
                print(f"You deposited ₱{amount}. New Balance: ₱{balance}\n")
            else:
                print("Invalid input. Can only deposit ₱100, ₱200, ₱500, ₱1000", "\n")
        elif menu == 3:
            withdraw = int(input("Enter amount to withdraw: "))
            if withdraw == 100 or withdraw == 200 or withdraw == 500 or withdraw == 1000:
                balance -= withdraw
                print(f"You took ₱{withdraw}. New Balance: ₱{balance}\n")
            elif withdraw >= balance:
                print("Insufficient Balance!") 
            else:
                print("Invalid input. Can only dispense ₱100, ₱200, ₱500, ₱1000", "\n")
        else:
            exit()
            