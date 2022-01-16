username = input("Enter Username: ")
age = input("Enter your age: ")
reddit_username = input("Enter reddit username: ")

print(f"your name is {username}, you are {age} years old, and your username is {reddit_username}")


# Extra bonus
f = open("file.txt", "w")
f.write(f"your name is {username}, you are {age} years old, and your username is {reddit_username}")
f.close()
