import random 
#functions
b = random.randint(1,3)
def rule(a,b):
  if a == b :
    print("RESULT :- DRAW!")
  elif a == 1 and b == 2 : 
    print("RESULT :- YOU WON")
  elif a == 1 and b == 3 : 
    print("RESULT :- YOU LOSE")    
  elif a == 2 and b == 1 : 
    print("RESULT :- YOU LOSE")
  elif a == 2 and b == 3 : 
    print("RESULT :- YOU WON")
  elif a == 3 and b == 1 : 
    print("RESULT :- YOU WON")
  else :
    print('RESULT :- YOU LOSE')  
def com(b):
  picks = {1 : "SNAKE", 2 : "WATER", 3 : 'GUN'}
  print(f"COMPUTER's PICK WAS {picks[b]}")      
er = "PLEASE ENTER GIVEN INT ONLY"

#user-input
a = int(input("WELCOME TO SNAKE WATER GUN GAME \nPLEASE SELECT THE GIVEN INT \n1 for Snake\n2 for Water\n3 for Gun\nYour Pick :-"))    
b = random.randint(1,3)
#game-computation
if a == 1 or a == 2 or a == 3 :
  picks2 = {1 : "SNAKE", 2 : "WATER", 3 : 'GUN'}
  print(f"YOUR PICK WAS {picks2[a]}")
  com(b)
  rule(a,b)

else :
  print(er)   
