words = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]
count = 0
for word in words:
    if int(len(word)) == 5:
        count += 1
print(count)