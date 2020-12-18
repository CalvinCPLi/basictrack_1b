numbers = [1, 3, 3, 3, 61, 1]

tot = sum(numbers) - next((x for x in numbers if x % 2 == 0), 0)
print(tot)

print(sum(numbers))