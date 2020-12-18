words = ["tree", "pc", "alice", "sam", "sam"]
count = 0

for word in words:
    if word == "sam":
        break
    count += 1
print(count)