# Code originally from teamtreehouse.com
# 
# Unit 1 Practice 4:
# Team Creator - Practice Creating and Indexing Lists

# TODO Create an empty list to maintain the player names
team = []

# TODO Ask the user if they'd like to add players to the list
add_player = input("Would you like to add players to the team? (Yes/No): ")
# If the user answers "Yes", let them type in a name and add it to the list

while add_player.lower() == "yes":
    team.append(input("What's the new player's name?: "))
    add_player = input("Would you like to add another player? (Yes/No): ")

# If the user answers "No", print out the team 'roster'
else:
    print("There are {} players in the team:".format(len(team)))


# TODO print the number of players on the team
# TODO Print the player number and the player name
# The player number should start at the number one

for player in team:
    print("Player {}:".format(team.index(player) + 1),player)




# TODO Select a goalkeeper from the above roster
goal_keeper = int(input("Please select who the goalkeeper will be by selecting the player number (1-{}):".format(len(team))))

# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Great! The goalkeeper will be {}! Have fun!".format(team[goal_keeper - 1]))

