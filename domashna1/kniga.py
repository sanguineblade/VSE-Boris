k=int(input("Enter k: "))
page, digits, count = 0, 1, 9

while k > count * digits:
    k -= count * digits
    page += count
    digits += 1
    count *= 10
    
page += k // digits
print("Pages = ", page)