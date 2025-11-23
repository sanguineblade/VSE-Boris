s = input("Enter text: ")
i, j = 0, len(s)-1
palindrom = True

while i < j:
    if s[i] is not s[j]:
        palindrom = False
        break
    i += 1
    j -= 1

if palindrom:
    print("Palindrom")
else:
    print("Not palindrom")