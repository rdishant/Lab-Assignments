import random                                   #to take random num
total_guesses=4                                       #Total no of chances to be given
win=False                                       #initially win is taken as false
welcome = input("LETS PLAY")
name=str(input("ENTER YOUR NAME"))
sname=name.upper()
print("HELLO",sname,"WELCOME")
print(sname,"YOU ARE SET TO ROAR")
die1=random.randint(1,7)                        #random input1
die2=random.randint(1,7)                        #random input2
total=die1+die2                                 #adding iboth the random inputs
try: 
 while total_guesses>0:                               #condition for total no of chances
  guess=int(input("GUESS A NUMBER"))
  total_guesses=total_guesses-1                             #decreasing the total number of chances
  if guess>total:
        print(" HEY",sname,"The guessed number is too big," , "total guesses remaining are",total_guesses)     
  elif guess<total:
        print(" HEY",sname,"The guessed number is too low","total guesses remaining are",total_guesses)         
  else:
        print(sname,"CONGRATS YOU HAVE WON THE GAME")
        win=True                                                                        #if guessed right condition of win becomes true
        total_guesses=0
except  ValueError as e :
 print(e)        

if win==False:                                                                          #showing the actual value generated by random variables
 print(sname,"your guesses were incorrect , the no is",total,"Computer has won this time")
