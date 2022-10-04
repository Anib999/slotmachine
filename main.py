def deposit():
    while True:
        amount = input('Enter amount to deposit. Rs.')
        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print('Amount must be more than 0')
        else:
            print('Enter valid amount to deposit')
    return amount

def main():
    deposit()