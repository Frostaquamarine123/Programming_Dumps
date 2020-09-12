# Python3 program to add two numbers
print("enter two number to find the sum")
number1 = input("First number: ")
number2 = input("\nSecond number: ")

# Adding two numbers
# User might also enter float numbers
numbertype1 = type(number1)
numbertype2 = type(number2)

sum = float(number1) + float(number2)


# Display the sum
# will print value in float
print("The sum of {0} and {1} is {2}".format(number1, number2, sum))
