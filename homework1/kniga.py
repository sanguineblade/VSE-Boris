k=int(input("Enter k: "))
n, i = 0, 0
while k > 0:
    digits = 9 * (10**i) * (i + 1)
    if k - digits > 0:
        k -= digits
        n += digits / (i + 1)
    else:
        n += k / (i+1)
        break
    i += 1
print("Pages = ", round(n))