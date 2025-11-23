kozi=[]

while True:
    n=int(input("enter n: "))
    if n in range(1,1000):
        break
    else:
        print("Invalid n")

while True:
    k=int(input("enter k: "))
    if k in range(1,1000):
        break
    else:
        print("Invalid k")

for i in range(n):
    while True:
        weight=int(input("enter weight: "))
        if weight in range(1,1000):
            break
        else:
            print("Invalid weight")
    kozi.append(weight)

kozi.sort(reverse = True)

def check(capacity):
    used = [False] * n
    count = 0
    for trip in range(k):
        currentLoad = 0
        for i in range(n):
            if not used[i]:
                if currentLoad + kozi[i] <= capacity:
                    currentLoad += kozi[i]
                    used[i] = True
                    count += 1
        if count is n:
            return True
    return False
low = max(kozi)
high = sum(kozi)
ans = high
while low <= high:
    mid = (low + high) // 2
    if check(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print("lowimal capacity = ",ans)
