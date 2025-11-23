n = int(input("Enter n: "))
spisuk = []

for i in range(n):
    chislo = int(input("Enter number: "))
    spisuk.append(chislo)

sum = 0
for j in spisuk: 
    sum += j ** 2

print("The sum of squares is:", sum)