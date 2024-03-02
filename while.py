# Initialising a list to store all numbers introduced by the user
numbers = []

# While block to continuously ask the user for a number, until they enter -1
# The number is added to the list of all the numbers introduced
while True:
    try:
        num = float(input("Please insert a number (or -1 to stop): "))
        if num == -1:
            break # Exit the loop if the input is -1
        numbers.append(num) # Add number to the list
# Catching non-float inputs
    except ValueError:
        print("""You didn't introduce a valid input.
Please enter a numerical value.""")

# If block to avoid the dividing by zero error (if the user enters -1 as first number)
# Calculating the average, rounding it for a more user-friendly output and printing it
if numbers:
    average = round(sum(numbers)/len(numbers), 2) # Using built-in sum and len functions
    print(f"The average of the numbers you entered is: {average}")
else:
    print("You didn't enter any valid number for calculating the average.")