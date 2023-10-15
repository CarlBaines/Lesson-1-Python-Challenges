
#create dictionary
numbers = {'FirstNum': 9, 'SecondNum': 5, 'ThirdNum': 1, 'FourthNum': 3, 'FifthNum': 7}


#sorts the values in the list, ignores the keys which are strings. 1 in the lambda function represents the indexes of the values.
ascendingToDescendingNums = sorted(numbers.items(), key = lambda x:x[1])

print('Dictionary values sorted from ascending and descending: ')
print(str(ascendingToDescendingNums)[1:-1]) #slice deletes the first and last characters from the being outputted which is the curly brackets.






print('Adds a key to a dictionary')
#example dictionary
sampleDict = {'FirstNum': 1, 'SecondNum': 2}

print('')
print('Original dict is ', str(sampleDict)[1:-1])


#adds new key and value to the dict.
sampleDict['ThirdNum'] = 3

print('')
#outputs updated dictionary.
print('Updated dict is ', str(sampleDict)[1:-1])



print('Concatenates three dictionaries to create a new one')
#example dictionaries

dict1 = {1: 1, 2: 2}
dict2 = {3: 3, 4: 4}
dict3 = {5: 5, 6: 6}

print('')


#converts each dictionary to a list as they are mutable and can be added together.
result = dict(list(dict1.items()) + list(dict2.items()) + list(dict3.items()))

print(result)


