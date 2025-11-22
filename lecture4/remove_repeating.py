set = {'peach', 'chpis', 'pizza', 'orange', 'apple', 'banana', 'cherry'}
list = ["apple", "pizza"]
for i in range(len(list)):
    set.discard(list[i])

print(set)