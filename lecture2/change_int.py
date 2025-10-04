a=20
b=30
def change(a, b):
    a, b = b, a
    return a
print(change(a, b))