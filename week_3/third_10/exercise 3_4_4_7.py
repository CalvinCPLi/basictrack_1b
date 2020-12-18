string_format = "{0:1} {1:2.0f}"

for i in range(int(input("pick a number"))):
    print(string_format.format(i, (i**2 + i) / 2))