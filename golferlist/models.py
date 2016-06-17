from django.db import models


from golferlist import golfers

teamnames=["Blackpool","Blackburn","Arsenal"]

user_input = models.TextField()

# You have to handle the case where 2 or more teams starts with the same string.
# For example the user input is 'B'. So you have to select between "Blackpool" and
# "Blackburn"
filtered_teams = filter(lambda x: x.startswith(user_input), golfers)

if len(filtered_teams) > 1:
    # Deal with more that one team.
    print('There are more than one team starting with "{0}"'.format(user_input))
    print('Select the team from choices: ')
    for index, name in enumerate(filtered_teams):
        print("{0}: {1}".format(index, name))

    index = input("Enter choice number: ")
    # You might want to handle IndexError exception here.
    print('Selected team: {0}'.format(filtered_teams[index]))

else:
    # Only one team found, so print that team.
	print filtere_teams[0]