# Dennis Meier 
# 9th MAR 2026
# Find out who is the oldest 

# Initiate variables
people = int(input('how many people? '))

# first question | initial name and date
name = input('Name pls: ')
date = input('And the date: ')

# loop
for i in range(people):
    current_name = input('Next name pls: ')
    current_date = input('And next date: ')

    # override the date if older 
    if current_date < date:
        name = current_name
        date = current_date

    # counter -1 
    people -= 1

    # orientation text how many people left to add
    if i > 1:
        print('there are still', people, 'left')
    elif i == 1:
        print('there is still', people, 'left')
    else:
        print('error')

# output who is the oldest
print('the oldest person is ' + name + 'they were born on the ' + date)