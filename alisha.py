
#Assignment 1
def main():
    print("This program adds two numbers.")
    
    # Prompt the user to enter the first number
    num1 = input("Enter first number: ")
    num1 = int(num1)  # Convert the input to an integer
    
    # Prompt the user to enter the second number
    num2 = input("Enter second number: ")
    num2 = int(num2)  # Convert the input to an integer
    
    # Calculate the sum of the two numbers
    total = num1 + num2
    
    # Print the total sum with an appropriate message
    print("The total is " + str(total) + ".")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
#Assignment 2
def main():
    # Ask the user for their favorite animal
    favorite_animal = input("What's your favorite animal? ")
    
    # Respond with the favorite animal
    print("My favorite animal is also " + favorite_animal + "!")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

#Assignment 3

def main():
    # Prompt the user for the temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Output the temperature in Celsius
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

#Assignment 4
def main():
    anton = 21  # Anton's age is given as 21 years old
    beth = 6 + anton  # Beth is 6 years older than Anton, so add 6 to Anton's age to get Beth's
    chen = 20 + beth  # Chen is 20 years older than Beth, so add 20 to Beth's age to get Chen's
    drew = chen + anton  # Drew is as old as Chen's age plus Anton's age, so add them together
    ethan = chen  # Ethan is the same age as Chen, so set Ethan's age equal to Chen's

    # Print out all of the ages!
    print("Anton is " + str(anton))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))



if __name__ == '__main__':
    main()

# Assignment 5
def main():
    # Get the 3 side lengths of the triangle
    side1: float = float(input("What is the length of side 1 of triangle? "))
    side2: float = float(input("What is the length of side 2 of triangle? "))
    side3: float = float(input("What is the length of side 3 of triangle? "))

    # Calculate the perimeter (sum of the sides) and print the result
    perimeter = side1 + side2 + side3
    print("The perimeter of the triangle is " + str(perimeter))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
# Assignment 6
def main():
    # Ask the user for a number and convert the input to a float
    num: float = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number and print the result
    print(str(num) + " squared is " + str(num ** 2))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

