
'''
1 for snake
-1 for water
0 for gun

'''
import random
computer=random.choice([-1,0,1])
youstr=input("Enter the your choice:")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"Water",0:"Gun"}

#print(f"computr chioce {reverseDict}")
you=youDict[youstr]
## by now we have 2 numbers(variales),you and computer
print(f"You choice {reverseDict[you]}\nComputer choice {reverseDict[computer]}")

if (computer==you):
  print("Its a draw")
  
else:
  ##yah code pura if loop ke liye hai jo short kar diya gya hai
  '''if ((computer-you)==-1 or (computer-you)==2):
  print("you lose!")
  
    else: 
       print("you win!")
  
  '''

  if(computer==-1 and you==1):
    print("You win!")
  
  elif(computer==-1 and you==0):
    print("You Lose!")
  
  elif(computer==1 and you==-1):
   print("You Lose!")
    
  elif(computer==1 and you==0):
   print("You win!")
 
  elif(computer==0 and you==-1):
    print("You Lose!")
  
  elif(computer==0 and you==1):
    print("You Lose!")
  
  else:
    print("something want worng")