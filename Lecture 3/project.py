# Mini Bank Management System

balance = 0
while True:
    print('\nMINI BANK MANAGEMENT SYSTEM')
    print('1. Check Balance')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Exit')

    choice = int (input('Enter your choice (1-4): '))

    if choice == 4:
        print('Thank you for banking with us. Final Balance:', balance)
        break

    if choice < 1 or choice > 4:
        print('Invalid choice! Please enter a number between 1 and 4.')
    
    if choice == 1:
        print('Your current balance is: ', balance)
    elif choice == 2:
        while True:
            amount = float(input("Enter amount to deposit: "))

            if amount == 0:
                break
            if amount < 0:
                print('Invalid amount! Deposit amount cannot be negative.')
                continue
            
            balance += amount
            print('Deposited Successfully. New balance:', balance)
            break
    
    elif choice == 3:
        while True:
            amount = float(input('Enter amount to withdraw: '))

            if amount == 0:
                break
            if amount < 0:
                print('Invalid amount! Withdrawal amount cannot be negative.')
                continue

            if amount > balance:
                print('Insufficient balance! Your current balance is: ', balance)
                continue
            
            balance -= amount
            print('Withdrawal successful. New balance: ', balance)
            break