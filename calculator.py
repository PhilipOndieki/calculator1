# Reusable Calculator with Input Validation and Looping

class Calculator:
    def get_number(self, prompt):
        # Prompt until a valid number is entered.
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def format_number(self, num):
        # Return int if number is whole, else float.
        return int(num) if num.is_integer() else num

    def calculate(self):
        # Main calculation logic.
        num1 = self.get_number("Enter the first number: ")
        operation = input("Enter operation (+, -, *, /): ")
        num2 = self.get_number("Enter the second number: ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                return "Error: Division by zero"
            result = num1 / num2
        else:
            return "Invalid operation"

        # Format numbers for clean output
        num1_fmt = self.format_number(num1)
        num2_fmt = self.format_number(num2)
        result_fmt = self.format_number(result)

        return f"{num1_fmt} {operation} {num2_fmt} = {result_fmt}"


# Main Program Loop
if __name__ == "__main__":
    calculator = Calculator()

    while True:
        print("\n--- Simple Calculator ---")
        print("Type 'exit' at any time to quit.\n")

        # Ask user if they want to perform a calculation or exit
        choice = input("Press Enter to continue or type 'exit' to quit: ").strip().lower()
        if choice == 'exit':
            print("Goodbye! 👋")
            break

        # Perform a calculation
        print(calculator.calculate())
