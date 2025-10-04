n = int(input("Enter km:"))
dayNight = input("Day or Night? (d/n): ")
if n < 20:
    print("Your best option is taxi.")
    if dayNight == "d":
        totalPrice = (n * 0.79) + 0.70
    else:
        totalPrice = (n * 0.90) + 0.70
elif n >= 20 and n < 100:
    print("Your best option is bus.")
    totalPrice = n * 0.09
elif n >= 100:
    print("Your best option is train.")
    totalPrice = n * 0.06
print("Total price is:", totalPrice)