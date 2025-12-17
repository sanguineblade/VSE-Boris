salaries = []
while True:
    n = int(input("Enter n: "))
    if n in range(1,1000):
        break
    else:
        print("Invalid n")
    for i in range(n):
        salary = int(input("Enter salary: "))
        salaries.append(salary)

p1_count = 0
p2_count = 0 
p3_count = 0 
p4_count = 0
p5_count = 0 

for salary in salaries:
    if salary < 200:
        p1_count += 1
    elif 200 <= salary <= 399:
        p2_count += 1
    elif 400 <= salary <= 599:
        p3_count += 1
    elif 600 <= salary <= 799:
        p4_count += 1
    else:  
        p5_count += 1

print(f"p1 = {p1_count / n * 100:.2f}%")
print(f"p2 = {p2_count / n * 100:.2f}%")
print(f"p3 = {p3_count / n * 100:.2f}%")
print(f"p4 = {p4_count / n * 100:.2f}%")
print(f"p5 = {p5_count / n * 100:.2f}%")
