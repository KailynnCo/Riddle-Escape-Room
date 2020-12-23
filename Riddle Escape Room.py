#this is my intro
print("Wellcome to my escape room. You must guess the serect word in order to win \n ")

#clue 
print("Clue: There was a castastrpohic cyber attack recently. \n The governemt is still searching for the hacker. \n They think he .??? \n ")

#assign variables 
secret_word = "ransomeware"
guess = ""
guess_number = 0
guess_limit = 3
out_guess = False 


while guess != secret_word and not out_guess:
  if guess_number < guess_limit:
      guess = str(input("Enter your guess: "))
      guess_number += 1
  else:
    out_guess = True

if out_guess:
  print("oh no you loose")
else:
  print("Yai you win!!")

