tuple=("apple","banana","cherry","apple")
for i in range(len(tuple)):
    if tuple.count(tuple[i]) > 1:
        print(f"{tuple[i]} repeted")
        break