
#assign list
teams = ['Ferrari', 'Williams', 'Haas', 'Racing Point']

#print first element
print('Current bonus payment:',teams[0])

print('')

print(teams[0], 's rivals are',teams[1])

#Change element
teams[3] = 'Aston Martin'

#Add more teams to the list
teams.append('Ford')
teams.append('Mercedes')

#output list
print('')
print(teams)

replaceTeam = int(input('What team do you want to replace (enter a number from 0 to 5) '))
newTeamName = input('What is the name of the new team that you want to add to the list ')


del teams[replaceTeam]
teams.append(newTeamName)
print(teams)






