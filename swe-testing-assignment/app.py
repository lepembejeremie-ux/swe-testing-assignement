"""
Quick-Calc: Simple Calculator Application

A command-line calculator that supports basic arithmetic operations.
This application demonstrates the Calculator class in a practical use case.
"""

from calculator import Calculator, DivisionByZeroError


def display_menu():
    """Display the calculator menu."""
    print("\n" + "="*50)
    print("  Quick-Calc - Simple Calculator")
    print("="*50)
    print("Operations:")
    print("  1. Add")
    print("  2. Subtract")
    print("  3. Multiply")
    print("  4. Divide")
    print("  5. Clear")
    print("  6. Exit")
    print("="*50)


def get_two_numbers(operation_name: str) -> tuple:
    """
    Prompt the user for two numbers.
    
    Args:
        operation_name: Name of the operation (for display)
        
    Returns:
        Tuple of (first_number, second_number)
    """
    try:
        a = float(input(f"Enter first number: "))
        b = float(input(f"Enter second number: "))
        return a, b
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None, None


def main():
    """Main application loop."""
    calc = Calculator()
    
    print("\nWelcome to Quick-Calc!")
    print("A simple calculator for basic arithmetic operations.")
    
    while True:
        display_menu()
        choice = input("Select an operation (1-6): ").strip()
        
        if choice == "1":  # Add
            a, b = get_two_numbers("Add")
            if a is not None and b is not None:
                result = calc.add(a, b)
                print(f"\nResult: {a} + {b} = {result}")
        
        elif choice == "2":  # Subtract
            a, b = get_two_numbers("Subtract")
            if a is not None and b is not None:
                result = calc.subtract(a, b)
                print(f"\nResult: {a} - {b} = {result}")
        
        elif choice == "3":  # Multiply
            a, b = get_two_numbers("Multiply")
            if a is not None and b is not None:
                result = calc.multiply(a, b)
                print(f"\nResult: {a} × {b} = {result}")
        
        elif choice == "4":  # Divide
            a, b = get_two_numbers("Divide")
            if a is not None and b is not None:
                try:
                    result = calc.divide(a, b)
                    print(f"\nResult: {a} ÷ {b} = {result}")
                except DivisionByZeroError as e:
                    print(f"\nError: {e}")
        
        elif choice == "5":  # Clear
            calc.clear()
            print("\nCalculator cleared. Result reset to 0.")
        
        elif choice == "6":  # Exit
            print("\nThank you for using Quick-Calc. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
