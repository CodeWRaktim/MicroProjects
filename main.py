accounts = []
trans_money=[[0,0,0]]
def create_account():
    print("\n--- Create a New Account ---")
    username = input("Create Username: ").strip()
    password = input("Create Password: ").strip()
    c=10000000

    for account in accounts:
        c+=1
        if account['username'] == username:
            print("This username is already taken. Please choose a different one.")
            create_account()

    accounts.append({'username': username, 'password': password, 'balance': 0, 'acc_number':c})
    print(f"Account created successfully! Welcome, {username}!")
    print("You have been alloted with account number : ",c)


def login():
    print("\n--- Log In ---")
    username = input("Enter your Username: ").strip()
    password = input("Enter your Password: ").strip()

    for account in accounts:
        if account['username'] == username and account['password'] == password:
            print(f"\nWelcome back, {username}!")
            manage_account(account)
            return

    print("Incorrect username or password. Please try again.")

def manage_account(account):
    while True:
        print("\n1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Log Out")
        for i in range(0,len(trans_money)):
            if trans_money[i][1]==account['acc_number'] and trans_money[i][2]>0:
                print(f"Rs {trans_money[i][2]} is been received from account number {trans_money[i][0]}")
                trans_money[i][2]=0
        option = int(input("Choose an option (1/2/3/4/5): "))

        match option:
            case 1:
                print(f"Your account balance is: Rs {account['balance']}")
                manage_account(account)
            case 2:
                deposit = int(input("Enter amount to deposit (Rs): "))
                account['balance'] += deposit
                print(f"Rs {deposit} has been credited to your account.")
                print(f"Your account balance is: Rs {account['balance']}")
                manage_account(account)
            case 3:
                withdraw = int(input("Enter amount to withdraw (Rs): "))
                if account['balance'] >= withdraw:
                    account['balance'] -= withdraw
                    print(f"Rs {withdraw} has been debited from your account.")
                    print(f"Your account balance is: Rs {account['balance']}")
                else:
                    print("Insufficient balance.")
                manage_account(account)
            case 4:
                acc=int(input("Enter account number of receiver : "))
                t=0
                for accountt in accounts:
                    if accountt['acc_number']==acc:
                        t+=1
                        trans=int(input("Enter amount to transfer : "))
                        if trans<=account['balance']:
                            account['balance']-=trans
                            accountt['balance']+=trans
                            m=[account['acc_number'],accountt['acc_number'],trans]
                            trans_money.append(m)
                            print(f"{trans} is been successfully transfered to account number {acc}")
                        else:
                            print("Insufficent balance")

                if t==0:
                    ("Please enter valid account number")
                print(f"Your account balance is: Rs {account['balance']}")
                manage_account(account)
            case 5:
                print(f"Goodbye, {account['username']}!")
                run_banking_app()
            case _:
                print("Invalid option. Please try again.")
                manage_account(account)

def run_banking_app():
    while True:
        print("\n--- Welcome to Your RSSS Banking App ---")
        print("1. Log In")
        print("2. Create a New Account")
        print("3. Exit")

        choice = input("Please choose an option (1/2/3): ").strip()

        if choice == "1":
            login()
        elif choice == "2":
            create_account()
        elif choice == "3":
            print("Thank you for using the banking app. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

run_banking_app()