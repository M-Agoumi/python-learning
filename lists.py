fruits = ['appel', 'orange', 'banana', 'peach']
fruits.insert(-1, 'greps') # insert new element at the giving index
fruits.append('watermelon') # insert new element at the end of the array

last_fruite = fruits.pop() # pop get an element from the array and remove it, in case no index provided the last element is used then
del fruits[0] # delete by index
fruits.remove('banana') # delete by value

sortedList = sorted(fruits) # sort and return the value, not touching the original list
fruits.sort() # sort the list accepts argument (reverse=True) to order DESC

fruits.reverse() # reverse the order of the list

listLenght = len(fruits) # get list coutn

print(listLenght)
for fruit in fruits:
    fruit = fruit.title()
    print("- " + fruit)

print('  ___________________')
for fruit in fruits:
    print("- " + fruit)

print('  ___________________')

numbers = list(range(0,5))
print(numbers)