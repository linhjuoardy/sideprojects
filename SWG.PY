
import random 
#functions
b = random.randint(1,3)
def rule(a,b):
  if a == b :
    print("DRAW!")
  elif a == 1 and b == 2 : 
    print("YOU WON")
  elif a == 1 and b == 3 : 
    print("YOU LOSE")    
  elif a == 2 and b == 1 : 
    print("YOU LOSE")
  elif a == 2 and b == 3 : 
    print("YOU WON")
  elif a == 3 and b == 1 : 
    print("YOU WON")
  else :
    print('YOU LOSE')  
def com(b):
  if b == 1 :
    print("COMPUTER PICKED SNAKE")
  elif b == 2 :
    print('COMPUTER PICKED WATER')
  else :
    print("COMPUTER PICKED GUN")        
er = "PLEASE ENTER GIVEN INT ONLY"

#user-input
a = int(input("WELCOME TO SNAKE WATER GUN GAME \nPLEASE SELECT THE GIVEN INT \n1 for Snake\n2 for Water\n3 for Gun\nYour Pick :-"))    
#game-computation
if a == 1 or a == 2 or a == 3 :
  rule(a,b)
  com(b)
else :
  print(er)              
