n = int(input("Enter n: "))
spisuk = []
sum = 0

for i in range(n):
    chislo = int(input("Enter number: "))
    spisuk.append(chislo)

for j in spisuk: 
    sum += j ** 2

print("The sum of squares is:", sum)