# Code originally from teamtreehouse.com
# 
# Unit 1 Practice 2:
# FizzBuzz - Practice Comparisons

name = input("Please enter your name:  ")
number = input("Please enter a number:  ")

# TODO: Make sure the number is an integer
number = int(number)

# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.
print("Hello, {}!\nThe number {} is...".format(name,number))

# TODO: Compare the number the user gave with the different
# FizzBuzz conditions. 
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************




# TODO: Define variables for is_fizz and is_buzz that stores 
# a Boolean value of the condition. Remember that the modulo operator, %, 
# can be used to check if there is a remainder.
is_fizz = number % 3 == 0
is_buzz = number % 5 == 0


# Using the variables, check the condition of the value, and print the necessary
# string

if is_fizz * is_buzz == 1:
    print("is a FizzBuzz number.")
elif is_fizz == 1:
    print("is a Fizz number.")
elif is_buzz == 1:
    print("is a Buzz number.")
else:
    print("is neither a fizzy nor a buzzy number.")
    