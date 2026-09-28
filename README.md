# Factorial and Fibonacci Using Recursion

A simple, beginner-friendly Python CLI mini project demonstrating the concept of recursive functions.

---

## 1. Project Title
**Factorial and Fibonacci Generator Using Recursion**

---

## 2. Aim
To develop a menu-driven Python command-line program that calculates the factorial of a given number and generates the Fibonacci sequence up to $N$ terms using recursion.

---

## 3. Problem Statement
Iterative solutions using loops are common, but understanding recursion is fundamental in computer science. The challenge is to implement mathematical operations—specifically factorial calculation and Fibonacci series generation—strictly using self-referential (recursive) functions without relying on iterative calculation loops or built-in helper functions like `math.factorial()`.

---

## 4. Objectives
- To understand and demonstrate the concept of **recursion** in Python.
- To identify and implement **base cases** and **recursive cases** correctly.
- To build a clean, interactive, menu-driven CLI interface.
- To handle invalid inputs such as negative numbers and non-integer values gracefully.

---

## 5. Concepts Used
1. **Recursion:** A programming technique where a function calls itself directly or indirectly to solve a smaller instance of the same problem.
2. **Base Case:** The terminating condition that prevents infinite function calls and stack overflow.
3. **Recursive Case:** The condition where the function calls itself with modified parameters moving toward the base case.
4. **Conditional Statements (`if-elif-else`):** Used for branching logic and input validation.
5. **Exception Handling (`try-except`):** Used to capture `ValueError` when non-integer input is entered.
6. **While Loop:** Keeps the menu active until the user chooses to exit.

---

## 6. Algorithm

### Algorithm for Factorial (`factorial(n)`):
1. **Start**
2. **Input:** Take an integer $n$.
3. **Check Base Case:**
   - If $n == 0$ or $n == 1$, return $1$.
4. **Recursive Step:**
   - If $n > 1$, return $n \times \text{factorial}(n - 1)$.
5. **End**

### Algorithm for Fibonacci (`fibonacci(n)`):
1. **Start**
2. **Input:** Take index $n$ (0-indexed).
3. **Check Base Cases:**
   - If $n == 0$, return $0$.
   - If $n == 1$, return $1$.
4. **Recursive Step:**
   - If $n > 1$, return $\text{fibonacci}(n - 1) + \text{fibonacci}(n - 2)$.
5. **End**

---

## 7. How the Program Works
1. The program starts inside the `main()` function and enters an infinite `while True` loop presenting a menu with 3 options:
   - `1. Find Factorial`
   - `2. Generate Fibonacci Series`
   - `3. Exit`
2. **Option 1 (Factorial):**
   - Asks the user for an integer.
   - Validates that the number is non-negative ($n \ge 0$).
   - Calls the recursive `factorial(n)` function and prints the result.
3. **Option 2 (Fibonacci):**
   - Asks the user for the number of terms.
   - Validates that the number of terms is positive ($\text{terms} > 0$).
   - Runs a display loop from $i = 0$ to $\text{terms} - 1$, invoking `fibonacci(i)` recursively for each term and printing the sequence.
4. **Option 3 (Exit):**
   - Prints a exit message `"Thank you!"` and terminates the program loop.
5. Any invalid menu choice or non-integer input is caught and an appropriate friendly error message is shown.

---

## 8. Sample Output

```text
=================================
  Factorial & Fibonacci Program  
=================================
1. Find Factorial
2. Generate Fibonacci Series
3. Exit

Enter your choice: 1
Enter a number: 5
Factorial of 5 = 120

=================================
  Factorial & Fibonacci Program  
=================================
1. Find Factorial
2. Generate Fibonacci Series
3. Exit

Enter your choice: 2
Enter number of terms: 7
Fibonacci Series:
0 1 1 2 3 5 8 

=================================
  Factorial & Fibonacci Program  
=================================
1. Find Factorial
2. Generate Fibonacci Series
3. Exit

Enter your choice: 3
Thank you!
```

---

## 9. How to Run

### Prerequisites
- Python 3.x installed on your computer.

### Execution Steps
1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd /path/to/Factorial-Using-Recursion-Py
   ```
3. Run the script:
   ```bash
   python3 main.py
   ```
   *(or `python main.py` on Windows)*

---

## 10. Conclusion
This project successfully demonstrates the implementation of recursion in Python through mathematical algorithms: factorial and Fibonacci series. It clearly separates base cases from recursive cases and emphasizes memory-efficient, clean, and beginner-friendly programming practices suitable for viva explanations and academic practical assessments.
