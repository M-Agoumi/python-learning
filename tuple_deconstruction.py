def min_and_max(numbers):
    min_nb = min(numbers)
    max_nb = max(numbers)
    return (min_nb, max_nb)

numbers = [10, 5, 2, 21, 25, 16]
(a, b) = min_and_max(numbers)
print(str(a) + " " + str(b)) 
