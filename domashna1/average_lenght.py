n = int(input("Enter n: "))
str = []
lenght = 0
for i in range(n):
    text = input("Enter string: ")
    str.append(text)

for j in str:
    lenght += len(j)

print("Avrage lenght: ", lenght/n)