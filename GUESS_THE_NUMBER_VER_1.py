import random
a = random.randint(1,100)
c = "PICK ONE NUMBER BETWEEN 1-100\n"
print(c)
chance = 1
while chance < 6: 
	print(f"TRY NO. - {chance}")
	b = int(input("ENTER YOUR GUESS :- "))
	print(b)
	if b == a :
		print("CORRECT!")
	elif b < a : 
		print("YOUR GUESS IS LOW TRY AGAIN")
		chance+= 1 	
	elif b > a :
		print("YOUR GUESS IS HIGH TRY AGAIN")
		chance+=1	
	else :
		print("YOU LOST THE GAME")





