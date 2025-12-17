comment = input("Write a comment: ")
words = comment.split()
if len(words) > 8:
    print("No")
else:
    print("Yes")
    print(comment.capitalize())