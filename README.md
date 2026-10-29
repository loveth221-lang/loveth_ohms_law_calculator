## Ohm's Law and Power Calculator

## What it does

This Python program calculates voltage, current, resistance, and electrical power using Ohm's Law formulas. It accepts numerical values with SI prefixes, displays results with the appropriate units, and allows users to perform multiple calculations until they choose to quit.

## How to run it

Install Python 3, then run:

"python ohms_law_calculator.py"

## Sample output

===== OHM'S LAW CALCULATOR =====
1. Calculate Voltage (V)
2. Calculate Current (I)
3. Calculate Resistance (R)
4. Calculate Power (P)
5. View Calculation History
6. Quit

Choose an option (1-6): 2
Enter voltage in volts (V): 12
Enter resistance in ohms (Ω): 6

Result: Current = 2 A

## My own twist

I added four special features to make my calculator more useful:

1. Component Safety Advisor: Uses a built-in 2x thermal safety margin to recommend an operating power limit based on the component's rated power.
2. SI Prefix Support: Accepts values such as 4.7k for 4,700 and 250m for 0.25.
3. Calculation History: Stores previous calculation results so users can review them during the current session.
4. Power-Saving Tips: Displays general power-related tips based on the calculated electrical power.

## What I learned

I learned how to use Python functions, loops, conditional statements, lists, and error handling to build a practical calculator. I also learned how to apply Ohm's Law formulas and work with SI prefixes in electrical engineering calculations.

## Author

Nnadede Chidinma Loveth, ND1 Mechatronics Engineering, YabaTech.
