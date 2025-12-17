goats=[]

while True:
    n=int(input("enter n: "))
    if n in range(1,1000):
        break
    else:
        print("enter valid n")

while True:
    k=int(input("enter k: "))
    if k in range(1,1000):
        break
    else:
        print("enter valid k")

for i in range(n):
    while True:
        weight=int(input("enter weight: "))
        if weight in range(1,1000):
            break
        else:
            print("enter valid weight")
    goats.append(weight)

goats.sort(reverse=True)

def check(capacity):
    used_goats = [False] * n
    count = 0
    for trip in range(k):
        current_load = 0
        for i in range(n):
            if not used_goats[i]:
                if current_load + goats[i] <= capacity:
                    current_load += goats[i]
                    used_goats[i] = True
                    count += 1
        if count == n:
            return True
    return False
low = max(goats)
high = sum(goats)
ans = high
while low <= high:
    mid = (low + high) // 2
    if check(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print("Lowest capacity for the boat is: ", ans)