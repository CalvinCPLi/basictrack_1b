numbers = [1, 3, 5, 61, 123, 34, 22, -2222]
total = 0

for i in numbers:
    if i < 0:
        total += i
print(total)