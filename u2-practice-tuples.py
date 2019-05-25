# Tuples are immutable lists that are created by adding a comma between values:
my_tuple = (1, 2, 3)
my_second_tuple = 4, 5, 6

# Tuples can also be created by using the 'tuples()' function:
my_third_tuple = tuple([7, 8, 9])

# Tuples allow for value swapping:
a = 5
b = 20
a, b = b, a #this will change the values of a to 20 and b to 5

# Other uses of tuples:

"""
In python, the use of *args or *nums (the naming doesn't matter here) 
is a way to let function accept any number of arguments.
"""
def add(*nums):
    # this function accepts 0 or more arguments
    # and the arguments are stored in a tuple named nums
    result = 0
    for i in nums:
        result += i
    return result

print(add())       # => 0
print(add(1,2,3))  # => 6
print(add(9))      # => 9

""" 
def add(base, *args) on the other hand, accepts 1 or more arguments, 
base is the required argument here, any more argument provided after 
the 1st one will be stored in the tuple named args.
"""

def add(base, *args):
    # this function accepts 1 (minimum) or more arguments
    result = base
    for i in args:
        result += i
    return result

print(add())      # => syntax error (expected at least 1 argument, 0 given)
print(add(2))     # => 2
print(add(2,5,3)) # => 10

# First challenge: creating a 'multiply' function that takes any number or arguments:
def multiply(*args):
    product = 1
    for number in args:
        product *= number
    return product

# Second challenge: Create a function named stringcases that takes a single string but returns a tuple of different string formats.:
def stringcases(string):
    uppercase = string.upper()
    lowercase = string.lower()
    titlecase = string.title()
    reverse = string[::-1]
    return uppercase, lowercase, titlecase, reverse

# Third challenge: Create a function named combo that takes two ordered iterables and returns a list of tuples:

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(first_iterable,second_iterable):
    list_of_things = []
    first_iterable_list = list(first_iterable)
    second_iterable_list = list(second_iterable)
    index = 0
    for value in first_iterable_list:
        first_iterable_value = first_iterable_list[index]
        second_iterable_value = second_iterable_list[index]
        tuple_value = (first_iterable_value, second_iterable_value)
        list_of_things.append(tuple_value)
        index += 1
    return list_of_things