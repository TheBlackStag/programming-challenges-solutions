import math
user = 0
result = 50
num = 1
print ("Type 'h' for higher and 'l' for lower and 'r' if I'm right")
print ("I'm ready to play!")
while True:
 
	print (result)
	user = input("Higher (h), Lower (l) or Right (r)?")
	if user == "h":
		result = math.ceil(result * (50 / num / 100 + 1))
	elif user == "l":
		result = math.floor(result * (1 - 50 / num / 100))		
	elif user == "r":
		break
	num = num + 1
print ("Number found in %d tries, not bad!" %(num))
