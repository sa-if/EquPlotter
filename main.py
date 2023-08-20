import matplotlib.pyplot as plt
import numpy as np
import math

# Define a function that evaluates an equation in x
def f(x):
    return eval(equation)

# Check if the script is run directly
if __name__ == '__main__':
    # Ask the user for an equation
    equation = input("Enter an equation in x: ")

    # Create an array of x values
    x = np.linspace(-5, 5, 100)

    # Try to evaluate the equation for each x value
    try:
        y = f(x)
    # Catch any exceptions that might occur
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        exit()
    except ValueError:
        print("Error: Invalid value for math function.")
        exit()
    except NameError:
        print("Error: Unknown variable or function name.")
        exit()
    except SyntaxError:
        print("Error: Invalid syntax for equation.")
        exit()

    # Plot the equation
    plt.plot(x, y, 'r--')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Plot of f(x) = ' + equation)
    plt.show()
