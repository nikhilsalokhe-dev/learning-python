# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Enter your post: ")

if "harry" in post.lower():
    print("The given post is talking about Harry.")

else:
    print("The given post is not talking about Harry.")
