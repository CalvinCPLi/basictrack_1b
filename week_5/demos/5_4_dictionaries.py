# key value pairs
fruit_bowl = {}
fruit_bowl["apple"] = 2
fruit_bowl["bananas"] = 4

print(fruit_bowl)
# get()
print(fruit_bowl["bananas"])
print(fruit_bowl.get("orange", 0))
user_input = input("What kind of fruit will you add?")
fruit_bowl[user_input] = fruit_bowl.get(user_input, 0) + 1
print(fruit_bowl)

#iterate over all keys

for fruit, quantity in fruit_bowl.items():
    fruit_bowl[fruit] += 1
    print(fruit, quantity)

# in tests keys (not values
if "pineapple" in fruit_bowl:
    print("What an exotic fruit bowl!")
else:
    print("What a dull fruit bowl :(")