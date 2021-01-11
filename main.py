import os

while True:

    option = input("Email or Account or Show: ")


    if option == "Email":
        email = input("Email (without @gmail.com): ")
        password = input("Password for the email: ")
        account = input("Account name with that email: ")

        with open(f"Email Info - {account}.txt", 'w') as f:
            f.write(f"email: {email}@gmail.com")
            f.write(f"\npassword: {password}")
            f.close()

    if option == "Account":
        email = input("Email (without @gmail.com): ")
        password = input("Password for the account: ")
        account = input("Account name with that email: ")

        with open(f"Account info - {account}.txt", 'w') as f:
            f.write(f'email: {email}@gmail.com')
            f.write(f"\npassword: {password}")
            f.close()
        
    if option == "Show":
        option = input("Email or Account: ")

        if option == "Email":
            account = input("What's the account linked to the email: ")
            os.popen(f"start Email Info - {account}.txt")
        elif option == "Account":
            account = input("What's the account name: ")
            os.popen(f"start Account Info - {account}.txt")