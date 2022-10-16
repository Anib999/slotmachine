import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row])


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


def number_of_lines():
    while True:
        lines = input('Enter lines to bet on (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines')
        else:
            print('Enter a number')
    return lines


def get_bet():
    while True:
        amount = input('Enter the amount to bet on each line. Rs.')
        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Enter valid bet between Rs.{MIN_BET}-Rs.{MAX_BET}')
        else:
            print('Enter valid amount')
    return amount


def main():
    balance = deposit()
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(
                f'You dont have enough to bet that amount. Your current balance is Rs.{balance}')
        else:
            break
    print(
        f'You are betting Rs.{bet} on {lines} lines. Total bet is Rs.{total_bet}')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()
