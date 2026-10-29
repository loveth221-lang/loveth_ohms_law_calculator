# ============================================
# OHM'S LAW AND POWER CALCULATOR
# Description: Calculates voltage, current,resistance, and power.
# ============================================

# Stores previous calculations during the session
history = []

# SI prefixes and their numerical multipliers
PREFIXES = {
    "p": 1e-12,   # pico
    "n": 1e-9,    # nano
    "u": 1e-6,    # micro
    "µ": 1e-6,    # micro
    "m": 1e-3,    # milli
    "k": 1e3,     # kilo
    "K": 1e3,     # kilo
    "M": 1e6,     # mega
    "G": 1e9      # giga
}


# Converts a number with an optional SI prefix to a float
def parse_value(text):
    text = text.strip()

    if not text:
        raise ValueError("Input cannot be empty.")

    # Check whether the last character is an SI prefix
    if text[-1] in PREFIXES:
        number = float(text[:-1])
        multiplier = PREFIXES[text[-1]]
        return number * multiplier

    # Otherwise, convert the input directly to a number
    return float(text)


# Gets a valid positive number from the user
def get_value(message):
    while True:
        try:
            value = parse_value(input(message))

            if value <= 0:
                print("Error: Enter a number greater than zero.")
            else:
                return value

        except ValueError:
            print("Invalid input! Try a value like 12, 4.7k, or 250m.")


# Displays the answer and saves it in calculation history
def save_result(result):
    print("\nResult:", result)
    history.append(result)


# Advises the user about component power ratings
def safety_advisor(power):
    print("\n--- COMPONENT SAFETY ADVISOR ---")

    rating = get_value(
        "Enter the component's rated power in watts (W): "
    )

    # Apply a 2x thermal safety margin:
    # The recommended operating limit is half the rating.
    safe_limit = rating / 2

    print(f"Component rating: {rating:.4g} W")
    print(f"Recommended power limit: {safe_limit:.4g} W")
    print(f"Calculated power: {power:.4g} W")

    # Compare the calculated power with the rating and safe limit
    if power > rating:
        print("WARNING: Calculated power exceeds the component rating!")
        print("Choose a suitably rated component or reduce the load.")

    elif power > safe_limit:
        print("CAUTION: Power is within the rating but exceeds")
        print("the recommended 2x thermal safety margin.")

    else:
        print("Power is within the recommended 2x safety-margin limit.")

    print("Note: This is a screening check, not a guarantee of safety.")
    print("Check the datasheet, temperature, cooling, and other limits.")


# Calculates voltage, current, resistance, or power
def calculate():
    print("\n===== OHM'S LAW CALCULATOR =====")
    print("1. Calculate Voltage (V)")
    print("2. Calculate Current (I)")
    print("3. Calculate Resistance (R)")
    print("4. Calculate Power (P)")
    print("5. View Calculation History")
    print("6. Quit")

    choice = input("Choose an option (1-6): ").strip()

    try:
        # Calculate voltage: V = I * R
        if choice == "1":
            current = get_value("Enter current in amperes (A): ")
            resistance = get_value("Enter resistance in ohms (Ω): ")

            voltage = current * resistance
            save_result(f"Voltage = {voltage:.4g} V")

        # Calculate current: I = V / R
        elif choice == "2":
            voltage = get_value("Enter voltage in volts (V): ")
            resistance = get_value("Enter resistance in ohms (Ω): ")

            current = voltage / resistance
            save_result(f"Current = {current:.4g} A")

        # Calculate resistance: R = V / I
        elif choice == "3":
            voltage = get_value("Enter voltage in volts (V): ")
            current = get_value("Enter current in amperes (A): ")

            resistance = voltage / current
            save_result(f"Resistance = {resistance:.4g} Ω")

        # Calculate power using one of three formulas
        elif choice == "4":
            print("\nChoose a power formula:")
            print("1. P = V * I")
            print("2. P = I² * R")
            print("3. P = V² / R")

            method = input("Choose a method (1-3): ").strip()

            if method == "1":
                voltage = get_value("Enter voltage (V): ")
                current = get_value("Enter current (A): ")
                power = voltage * current

            elif method == "2":
                current = get_value("Enter current (A): ")
                resistance = get_value("Enter resistance (Ω): ")
                power = current ** 2 * resistance

            elif method == "3":
                voltage = get_value("Enter voltage (V): ")
                resistance = get_value("Enter resistance (Ω): ")
                power = voltage ** 2 / resistance

            else:
                print("Invalid method! Choose 1, 2, or 3.")
                return

            # Display and save the calculated power
            save_result(f"Power = {power:.4g} W")

            # Special feature 1: Component Safety Advisor
            safety_advisor(power)

            # Special feature 2: Power-saving tips
            if power > 1000:
                print("\nPower Tip: Check the equipment's power rating")
                print("and cooling requirements carefully.")

            elif power > 100:
                print("\nPower Tip: Avoid unnecessary energy use")
                print("and check the equipment's specifications.")

            else:
                print("\nPower Tip: Energy consumption also depends")
                print("on how long the device operates.")

        # Special feature 3: Display previous calculations
        elif choice == "5":
            if not history:
                print("No calculations yet. Try calculating first!")
            else:
                print("\n===== CALCULATION HISTORY =====")

                for number, item in enumerate(history, start=1):
                    print(f"{number}. {item}")

        # Exit the program
        elif choice == "6":
            print("\nThank you for using the calculator!")
            print("Keep learning Python and electrical engineering!")
            return "quit"

        # Handle invalid menu choices
        else:
            print("Invalid choice! Enter a number from 1 to 6.")

    except (ValueError, OverflowError):
        print("Error: The calculation could not be completed.")
        print("Check your input values and try again.")


# Special feature 4: Repeat until the user chooses to quit
while True:
    outcome = calculate()

    if outcome == "quit":
        break