#Getting first input from the user and initialising the sum and counter with 0
num = float(input("Please insert a number: "))
sum = 0
counter = 0 

#While block to continuously ask the user for a number, until they enter -1
#The number is added to the sum of all the number introduced and the counter increases with every input
while num != -1:
    sum += num
    num = float(input("Please insert another number: "))
    counter += 1

#If block to avoid the dividing by zero error (if the user enters -1 as first number)
#Calculating the average, rounding it for a more user-friendly output and printing it
if counter != 0:
    average = round(float(sum/counter), 2) 
    print(f"The average of the numberes you entered is: {average}")
else:
    print("You didn't enter any valid number for calculating the average.")