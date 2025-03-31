import random

MAX_LINES = 3
MIN_BET = 100
MAX_BET = 1000

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(lines,columns,bet,values):
    winnings = 0 
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += (values[symbol] * bet)
            winning_lines.append(line+1)
    return winnings,winning_lines



def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row] , end="\n")



def deposit():
    while True:
        amount = input("Enter the amount you like to deposit? -> Rs.")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter amount > Rs 0")
        else:
            print("Enter a valid amount (number!!)")

    return amount
    

def get_num_of_lines():
    while True:
        lines = input(f"Enter the number of lines you'd like to bet on (1-{MAX_LINES}): -> ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter valid number of lines")
        else:
            print("Enter a valid line number!!")

    return lines

def get_bet():
    while True:
        amount = input(f"What amount would you like to bet on each line (Rs.{MIN_BET} - Rs.{MAX_BET}): -> ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter valid betting amount. Must be between Rs.{MIN_BET} - Rs.{MAX_BET}.")
        else:
            print("Enter a valid number!!")

    return amount


def spin(balance):
    while True:
        lines = get_num_of_lines()
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"Your balance is insufficient: Balance = Rs.{balance}")
            morebal = input("If you want to deposit more (Enter y) : ")
            if morebal == "y":
                balance = deposit()
                return balance
            else: return 0
        else:
            break
    print(f"YOU ARE BETTING Rs.{bet} ON {lines} LINES, TOTAL BET IS : Rs.{total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(lines,slots,bet,symbol_value)
    print(f"You won Rs.{winnings}")

    if winnings>0:
        winnings+=(len(winning_lines)*bet)

    print(f"You won on line: ", *winning_lines)
        
    return winnings - total_bet



def main():    
    balance = deposit()
    while True:
        print(f"Current balance is Rs.{balance}")
        useropt = input("Press enter to play and q to quit ")
        if useropt == "q" or spin == "Q":
            break
        balance += spin(balance)
    print(f"You left with balance : Rs.{balance}")





main()
