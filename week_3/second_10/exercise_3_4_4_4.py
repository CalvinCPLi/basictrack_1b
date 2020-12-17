numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
added = 0

string_format = "{0:3} {1:4}"
for number in numbers:
    print(string_format.format(number, number ** 2))

for number in numbers:
    added += number
    print(added)

product = 1
for number in numbers:
    product *= number
    print(product)
