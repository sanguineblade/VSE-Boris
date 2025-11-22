n=int(input("Entrer n: "))
list=[]
for i in range(n):
    x=int(input("Enter an element: "))
    list.append(x)
list.sort()
print(list)