#assign lists
driverNames = ['Sebastian Vettels', 'Charles Leclercs', 'Kevin Magnussens', 'Lando Norriss']
wages = ['21', '17', '3', '5']

totalWage = 0


#variable takes the length of the driverNames list.
x = len(driverNames)


#i is temp value.
for i in range(x):

    names = driverNames[i] #loops through the driverNames list and outputs each driver name.
    driverWages = wages[i] #loops through the wages list and outputs each number in order.
    
    print(names, 'wage is', driverWages, 'million')



for j in wages:
    totalWage += int(j) #loops through the wages list and calculates the total wage by adding each list element together.
    
print('\nThe total wage bill for the drivers is',totalWage, 'million')


