# Initialising the sum and counter with 0
sum = 0
counter = 0

# While block to continuously ask the user for a number, until they enter -1
# The number is added to the sum of all the number introduced and the counter increases with every input
while True:
    try:
        num = float(input("Please insert a number (or -1 to stop): "))
        if num == -1:
            break # Exit the loop if the input is -1
        counter += 1
        sum += num
# Catching non-float inputs
    except ValueError:
        print("""You didn't introduce a valid input.
Please enter a numerical value.""")

# If block to avoid the dividing by zero error (if the user enters -1 as first number)
# Calculating the average, rounding it for a more user-friendly output and printing it
if counter != 0:
    average = round(float(sum/counter), 2) 
    print(f"The average of the numbers you entered is: {average}")
else:
    print("You didn't enter any valid number for calculating the average.")