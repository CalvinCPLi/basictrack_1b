#string format

string_format = "{0:2} {2:3} {3:4} {1:5.2f}"

for i in range(10):
    print(string_format.format(i, i ** .5, i ** 2, i **3))
