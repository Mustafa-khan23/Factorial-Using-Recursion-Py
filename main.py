# Project: Factorial and Fibonacci using Recursion
# A simple college practical / mini project demonstrating recursive functions in Python.

# Recursive function to calculate factorial of a number
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n - 1)!
    else:
        return n * factorial(n - 1)


# Recursive function to find the nth Fibonacci number
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: fib(n) = fib(n - 1) + fib(n - 2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Main function with menu-driven interface
def main():
    while True:
        print("\n=================================")
        print("  Factorial & Fibonacci Program  ")
        print("=================================")
        print("1. Find Factorial")
        print("2. Generate Fibonacci Series")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            try:
                num = int(input("Enter a number: "))
                if num < 0:
                    print("Please enter a non-negative number.")
                else:
                    result = factorial(num)
                    print(f"Factorial of {num} = {result}")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                terms = int(input("Enter number of terms: "))
                if terms <= 0:
                    print("Please enter a positive number.")
                else:
                    print("Fibonacci Series:")
                    for i in range(terms):
                        print(fibonacci(i), end=" ")
                    print()
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            print("Thank you!")
            break

        else:
            print("Invalid choice! Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
