'''#This is a comment
This is a comment too
#Flip a coin program
from random import choice, random

#1st Method use random.random()
#coin_flip_with_random = "Head" if random() > 0.5 else "Tails"

#2nd Method random.choice()
coin_flip_with_choice = choice(["New York", "LA", "Dubai", "Australia", "Miami", "North Carolina", "Las Vegas", "Cancun", "Brasil", "Madrid"])
print(coin_flip_with_choice)'''
#Roll a dice
# 1st import your libraries
from random import randint
repeat = True
while repeat:
  print("You rolled", randint (1,6))
  print ("Do you want to try again?")
  repeat = ("y" or "yes") in input().lower()

  

