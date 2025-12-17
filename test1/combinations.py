n = int(input("Enter n: "))
k = int(input("Enter k:" ))
numbers = []
for i in range(n):
    number = int(input("Enter number: "))
    numbers.append(number)
for i in range(n):
    for j in range(i+1, n):
        if numbers[i] + numbers[j] > k:
            print(f"Combination is {numbers[i]} and {numbers[j]}")