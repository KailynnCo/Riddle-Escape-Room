import hashlib
import string 
from random import *
#using def function to make my code cleaner. The def function will now carry the password function.
def password_function():
 print("\n \nNow you will be given a password you will need to decrypt. This password is the different every round.You will only have 1 attempt to solve this password.")

 characters = string.ascii_letters + string.digits + string.punctuation 
#we use the import funtion "string" to get these

 password = "".join(choice(characters) for x in range(randint(3,8)))
 print("Testing to seperate section 3")
 print(password)
#ranint means random integer
#side note: make sure everything is tabbed between the def functions or else it wont run
#print(password) #password will not be shown in the future 

def MD5_function():
  print("\n \n Hint:MD5 Hash")
  hash_obj = hashlib.md5(b'Hello, Python!')
  print(hash_obj.hexdigest())

#First part of program:

teamname = [] #emtpy list,this will store the teams name

print("Welcome to the cyber game. Please input your team name: \n")
teamname.append(input("Team Name: ")) #.append to add input to the list

print("\nWellcome", teamname) #the \n adds a space
print("During this game you will be given a scenario based on solving encrpytion/ciphers, passwords and riddles.")

#Second part of program: 
#I looked up simple questions about the basics of what is cryptography
print("\nWelcome to part one of the game. You have 3 attempts in order to get the correct answer. \n \nQuestion 1: What is the study of secure communications techniques that allow only the sender and intended recipient of a message to view its contents.")

#assign variables 
part1_word = "cryptography"
answer = ""
answer_number = 0
answer_limit = 3
out = False 


while answer != part1_word and not out:
  if answer_number < answer_limit:
      answer = str(input("Enter your answer: "))
      answer_number += 1
  else:
    out = True

if out:
  print("oh no you loose")
else:
  print("Awesome Job! Its now time to go into Question # 2")
  

 #password will not be shown in the future , P.S make sure the password_function() is within the else: and print command. Or else it will not run the program because it is no within the command

#Third part of program:
#this having the person guess the password once its encrypted
  password_function()
  
#Fourth part of program:MD5 hash password 
  MD5_function()

#5th part: ask user to decrpyt the password


