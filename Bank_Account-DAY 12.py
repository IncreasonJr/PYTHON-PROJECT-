class Bank_Account:
    def owner_details(self):
        global balance
        name =input('Enter your name: ').capitalize().strip()
        while not name:
          print("❌ Name cannot be empty!")
          name =input('Enter your name: ').capitalize().strip()
          continue
        try:
            balance = int(input('How much do you want to create the account with: '))
            while balance <= 0:
                print('Invalid amount, enter a valid greater than zero: ')
                balance = int(input('How much do you want to create the account with: '))
        except ValueError:
            print('Invalid amount')
        print(f'Account holder: {name} Initial_balance: GHC{balance}')

    def deposit(self):
        global balance
        deposit=int(input('How much do you want to deposit: '))
        while deposit < 0:
            print('Invalid amount.Enter a positive amount:  ')
            deposit=int(input('How much do you want to deposit: '))
        balance = balance + deposit
        print(f'You deposited GHC{deposit:.2f}, your new balance is GHC{balance:.2f}')

    def withdraw(self):
        global balance
        try:
            withdrawal_amount=int(input('How much do you want to withdraw: '))     
            while withdrawal_amount < 0:
                print('Invalid amount.Enter a positive value: ')
                withdrawal_amount=int(input('How much do you want to withdraw: '))  
            while withdrawal_amount > balance:
                print(f'Insufficient balance. You can only withdraw up to GHC{balance:.2f}')
                withdrawal_amount=int(input('How much do you want to withdraw: '))  
            balance = balance - withdrawal_amount
            print(f'GHC{withdrawal_amount:.2f} has been withdrawn from your account. Your new balance is GHC{balance:.2f}')
        except ValueError: 
            print('Invalid amount')
        


account1=Bank_Account()
account1.owner_details()
account1.deposit()
account1.withdraw()