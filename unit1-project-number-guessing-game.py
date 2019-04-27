"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

# Printing the welcome message
print("\n##########################################\n  WELCOME TO WILL'S NUMBER GUESSING GAME\n##########################################")

# Defining the start_game() function
def start_game():
	attempts = 1
	random_number = random.randint(1,10)
	user_try = 0
	while user_try != random_number:
		try:
			user_try = int(input("\nPick a number between 1 and 10: "))
			if user_try < 1 or user_try > 10:
				 print("\nWoops, your number must be between 1 and 10. Try again!")
		except ValueError:
			print("\nThe number must be an integer between 1 and 10. Try again!")
		else:
			if user_try > random_number:
				attempts += 1
				print("\nToo high! Try again: ")
			elif user_try < random_number:
				attempts += 1
				print("\nToo low! Try again: ")	
	else:
		print("\nYou guessed it, {}! The number was {} and it took you {} tries. Good job!".format(player_name, random_number, attempts))
	return attempts

# Giving the game a personal touch by asking the player's name
player_name = input("\nHi! What is your name?: ")	
print("\nAlright, {}! Let's begin!".format(player_name))

# Running the game and storing the number of attempts as the new highscore
highscore = start_game()

# Block of code that asks the user if they want to play again, as well as storing the new highscore if lower than the previous one
user_decision = "yes"
while user_decision == "yes":
	user_decision = input("\nWant to play again? (Yes/No): ").lower()
	if user_decision == "yes":
		print("\nThe HIGHSCORE is {}".format(highscore))
		new_highscore = start_game()
		if new_highscore < highscore:
			highscore = new_highscore
		else:
			highscore
else:
	print("\nSee you next time, {}!\n".format(player_name))