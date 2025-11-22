car1 = {
    "brand": input("Enter car brand;"),
    "model": input("Enter car model:"),
    "horesepower": int(input("Enter car horsepower:"))
}

car2 = {
    "brand": input("Enter car brand;"),
    "model": input("Enter car model:"),
    "horesepower": int(input("Enter car horsepower:"))
}

if car1["horesepower"] > car2["horesepower"]:
    print(car1["brand"])