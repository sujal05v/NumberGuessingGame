import random
n = random.randint(1,100)
chance = 5
i = 1
while(i<=5):
 print(f"Guess the number you have {chance} chance: ")
 user = int(input())
 if(user==n):
  print("wow you won the game")
  break
 else:
    print("Number is wrong ....try again")
    if(user>n):
     print("Your number is big")
    else:
     print("Your number is small")

 i=i+1
 chance-=1

if(chance==0):
 print("Oops you loss the game....correct number is: ",n)
