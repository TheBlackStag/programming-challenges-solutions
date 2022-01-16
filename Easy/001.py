# Easy #1 
# 
# Solution By: github.com/krishnan-tech
# Let's solve daily programming challenges together, Join with us.
# discord https://discord.gg/NFJP6tjt2u

### problem statement ############################################################################################################
# create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:#
# your name is (blank), you are (blank) years old, and your username is (blank)                                                  #
#                                                                                                                                #
# for extra credit, have the program log this information in a file to be accessed later.                                        #
##################################################################################################################################

username = input("Enter Username: ")
age = input("Enter your age: ")
reddit_username = input("Enter reddit username: ")

print(f"your name is {username}, you are {age} years old, and your username is {reddit_username}")


# Extra bonus
f = open("file.txt", "w")
f.write(f"your name is {username}, you are {age} years old, and your username is {reddit_username}")
f.close()
