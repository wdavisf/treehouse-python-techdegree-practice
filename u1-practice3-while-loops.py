# Code originally from teamtreehouse.com
# 
# Unit 1 Practice 3:
# Understanding Loops - Practice Python While Loops

name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
question = input("Hello, {}! Do you understand Python while loops? Answer with yes/no: ".format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops

while question.lower() == "no":
# TODO: Since the user doesn't understand while loops, let's explain them.
    print("A loop is something that continues running until a different condition is met.")
# TODO: Ask the user again, by name, if they understand while loops.
    question = input("Do you understand loops now? Answer yes/no: ")   
# TODO: Outside the while loop, congratulate the user for understanding while loops
print("Congrats, {}! You finally got Python loops. Happy coding!".format(name)) 
