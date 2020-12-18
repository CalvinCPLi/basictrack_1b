number = int(input("Pick a number: "))

# prime numbers are greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime")
            break
    else:
        print(number, "is a prime")
else:
    print(number, "is not a prime number")