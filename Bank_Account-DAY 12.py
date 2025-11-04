class Bank_Account:
    def __init__(self):
       self.balance = 0

    def owner_details(self):
        name =input('Enter your name: ').capitalize().strip()
        while not name:
          print("Name cannot be empty!")
          name =input('Enter your name: ').capitalize().strip()
        while not name.isalpha():
            print('Name can only contain letters!Try again')
            name =input('Enter your name: ').capitalize().strip()
        try:
            self.balance = int(input('How much do you want to create the account with: '))
            while self.balance <= 0:
                print('Invalid amount, enter a valid greater than zero: ')
                self.balance = int(input('How much do you want to create the account with: '))
        except ValueError:
          print('Invalid amount')
        print(f'Account holder: {name} Initial_balance: GHC{self.balance}')

    def deposit(self):
        try:
            deposit=int(input('How much do you want to deposit: '))
            while deposit < 0:
             print('Invalid amount.Enter a positive amount:  ')
             deposit=int(input('How much do you want to deposit: '))
            self.balance = self.balance + deposit
            print(f'You deposited GHC{deposit:.2f}, your new balance is GHC{self.balance:.2f}')
        except ValueError:
          print('Invalid amount')

    def withdraw(self):
        try:
            withdrawal_amount=int(input('How much do you want to withdraw: '))     
            while withdrawal_amount < 0:
                print('Invalid amount.Enter a positive value: ')
                withdrawal_amount=int(input('How much do you want to withdraw: '))  
            while withdrawal_amount > self.balance:
                print(f'Insufficient balance. You can only withdraw up to GHC{self.balance:.2f}')
                withdrawal_amount=int(input('How much do you want to withdraw: '))  
            self.balance = self.balance - withdrawal_amount
            print(f'GHC{withdrawal_amount:.2f} has been withdrawn from your account. Your new balance is GHC{self.balance:.2f}')
        except ValueError: 
            print('Invalid amount')
        

def main():
    account1=Bank_Account()
    account1.owner_details()


    while True:
        print('This is your bank account')
        print('1. Deposit ')
        print('2. Withdraw')
        print('3. Exit')
        choice = input('What do you want to do today: ')
        if choice == '1':
            account1.deposit()
        elif choice == '2':
            account1.withdraw()
        elif choice == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid option')
            break
   
main()

