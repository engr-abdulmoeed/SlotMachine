import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

SYMBOLS = {
    "A": 4,
    "B": 6,
    "C": 7,
    "D": 9
}

SYMBOL_VALUE = {
    "A": 6,
    "B": 5,
    "C": 4,
    "D": 3
}


def check_winnings(columns: list[list], bet: int, lines: int, values: dict[str, int]) -> tuple[int, list[int]]:
    """
    Check the winnings based on the slot machine columns, bet amount, number of lines, and symbol values.

    Args:
        columns (list[list]): The columns of symbols from the slot machine spin.
        bet (int): The bet amount per line.
        lines (int): The number of lines to bet on.
        values (dict[str, int]): The values of each symbol.

    Returns:
        tuple[int, list[int]]: A tuple containing the total winnings and a list of winning lines.
    """
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]

        if all(symbol == column[line] for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_all_symbols(symbols: dict[str, int]) -> list[str]:
    """
    Generate a list of all symbols based on their counts.

    Args:
        symbols (dict[str, int]): A dictionary where keys are symbols and values are their counts.

    Returns:
        list[str]: A list containing all symbols, repeated according to their counts.
    """
    return [symbol for symbol, count in symbols.items() for _ in range(count)]


def get_slot_machine_spin(rows: int, columns: int, all_symbols: list[str]) -> list[list]:
    """
    Generate a slot machine spin result with the given number of rows and columns.

    Args:
        rows (int): The number of rows in the slot machine.
        columns (int): The number of columns in the slot machine.
        all_symbols (list[str]): A list of all symbols to be used in the slot machine.

    Returns:
        list[list]: A 2D list representing the slot machine spin result, where each sublist is a column of symbols.
    """

    return [[random.choice(all_symbols) for _ in range(rows)] for _ in range(columns)]


def print_slot_machine_output(columns: list[list]) -> None:
    """
    Print the slot machine columns in a formatted way.

    Args: columns (list[list]): A 2D list representing the slot machine columns, where each sublist is a column of
    symbols.
    """
    for row in range(len(columns[0])):
        print(" | ".join(column[row] for column in columns))


def deposit() -> int:
    """
    Prompt the user to enter a deposit amount and validate the input.

    Returns:
        int: The validated deposit amount.
    """
    while True:
        amount = input("How much money would you like to deposit? Rs.")

        if amount.isdigit() and int(amount) > 0:
            return int(amount)

        print("Invalid input. Enter a positive number.")


def get_no_of_lines() -> int:
    """
    Prompt the user to enter the number of lines to bet on and validate the input.

    Returns:
        int: The validated number of lines to bet on.
    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1 - {MAX_LINES}): ")

        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)

        print(f"Invalid input. Enter a number between 1 and {MAX_LINES}.")


def get_bet() -> int:
    """
    Prompt the user to enter the bet amount per line and validate the input.

    Returns:
        int: The validated bet amount per line.
    """
    while True:
        bet = input(f"What would you like to bet on each line? ({MIN_BET} - {MAX_BET}) ")

        if bet.isdigit() and MIN_BET <= int(bet) <= MAX_BET:
            return int(bet)

        print(f"Invalid input. Enter a number between {MIN_BET} and {MAX_BET}.")


def game(rows: int, columns: int, deposit_amount: int, symbols: dict[str, int], symbol_value: dict[str, int]) -> int:
    """
    Manage the game logic, including placing bets, spinning the slot machine, and calculating winnings.

    Args:
        rows (int): The number of rows in the slot machine.
        columns (int): The number of columns in the slot machine.
        deposit_amount (int): The initial deposit amount.
        symbols (dict[str, int]): A dictionary of symbols and their counts.
        symbol_value (dict[str, int]): A dictionary of symbols and their values.

    Returns:
        int: The net result of the game (winnings minus total bet).
    """
    lines = get_no_of_lines()

    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > deposit_amount:
            print(f"You do not have enough balance to place this bet. Your current balance is Rs.{deposit_amount}")
        else:
            break

    print(f"You are betting Rs.{bet} on each line. Total bet amount is Rs.{total_bet}")

    all_symbols = get_all_symbols(symbols)
    slots = spin(rows, columns, all_symbols)

    winning, winning_lines = check_winnings(slots, bet, lines, symbol_value)
    print(f"You have won Rs.{winning}")
    print("You won on lines:", *winning_lines)

    return winning - total_bet


def spin(rows: int, columns: int, all_symbols: list[str]) -> list[list]:
    """
    Generate a slot machine spin result and print the output.

    Args:
        rows (int): The number of rows in the slot machine.
        columns (int): The number of columns in the slot machine.
        all_symbols (list[str]): A list of all symbols to be used in the slot machine.

    Returns:
        list[list]: A 2D list representing the slot machine spin result, where each sublist is a column of symbols.
    """
    slots = get_slot_machine_spin(rows, columns, all_symbols)
    print_slot_machine_output(slots)

    return slots


def main() -> None:
    balance = deposit()

    while True:
        print(f"Your current balance: Rs.{balance}")
        play = input("Press Enter to play (or 'q' to quit) ")

        if play == 'q':
            break

        balance += game(ROWS, COLUMNS, balance, SYMBOLS, SYMBOL_VALUE)


if __name__ == "__main__":
    main()
