numbers = [2, 3, 3, 1, 123, 3, 5, 31, 23, 32, 36]
total = 0

for number in numbers:
    if number % 2 == 0:
        total += number
print(total)