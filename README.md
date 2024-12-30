# Slot Machine Game

This is a simple slot machine game implemented in Python. The game allows users to deposit money, place bets on multiple lines, spin the slot machine, and calculate winnings based on the spin results.

## Features

- Deposit money to start the game.
- Place bets on up to 3 lines.
- Spin the slot machine with 3 rows and 3 columns.
- Calculate winnings based on the symbols and their values.
- Display the user's balance after each round.
- Option to quit the game at any time.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository or download the `main.py` file.
2. Open a terminal and navigate to the directory containing `main.py`.
3. Run the script using the following command:

    ```sh
    python main.py
    ```

4. Follow the on-screen prompts to play the game.

## Game Workflow

1. **Deposit Money**: The user is prompted to enter a deposit amount.
2. **Place Bets**: The user is prompted to enter the number of lines to bet on and the bet amount per line.
3. **Spin the Slot Machine**: The slot machine spins and displays the result.
4. **Calculate Winnings**: The game calculates the winnings based on the spin result and updates the user's balance.
5. **Continue or Quit**: The user can choose to play another round or quit the game.

## Code Overview

- `check_winnings(columns, bet, lines, values)`: Checks the winnings based on the slot machine columns, bet amount, number of lines, and symbol values.
- `get_all_symbols(symbols)`: Generates a list of all symbols based on their counts.
- `get_slot_machine_spin(rows, columns, all_symbols)`: Generates a slot machine spin result with the given number of rows and columns.
- `print_slot_machine_output(columns)`: Prints the slot machine columns in a formatted way.
- `deposit()`: Prompts the user to enter a deposit amount and validates the input.
- `get_no_of_lines()`: Prompts the user to enter the number of lines to bet on and validates the input.
- `get_bet()`: Prompts the user to enter the bet amount per line and validates the input.
- `game(rows, columns, deposit_amount, symbols, symbol_value)`: Manages the game logic, including placing bets, spinning the slot machine, and calculating winnings.
- `spin(rows, columns, all_symbols)`: Generates a slot machine spin result and prints the output.
- `main()`: The main function to run the slot machine game.
