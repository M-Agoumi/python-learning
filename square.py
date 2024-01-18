squares = [i ** 2 for i in range(1,12)]

print(squares)

print([i for i in range(1,11)])

million = range(1, 1000001)

print("min: " + str(min(million)))
print("max: " + str(max(million)))

oddNumbers = range(2, 21, 2)

print("odd numbers from 1 to 20:")
for number in oddNumbers:
    print("- " + str(number))

inThree = [i * 3 for i in range (3, 31)]
print("numbers x 3 from 3 to 30:")
for number in inThree:
    print("- " + str(number))

cubes = [i ** 3 for i in range (3, 11)]
print("cube numbers from 3 to 30:")
for number in cubes:
    print("- " + str(number))