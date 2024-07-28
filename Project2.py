print("************Number guessing game*************** ")
import random #default module
top_of_the_range=input("Type a number: ")

if top_of_the_range.isdigit():
    top_of_the_range=int(top_of_the_range)
    if top_of_the_range<=0:
        print("type a number >0")
        quit()
    
else:
    print("please type a number next time")
    quit()

random_number=random.randint(0,top_of_the_range)
guesses=0

while True: #till below contions are not become true this program will continuously run
    guesses+=1
    user_guess=input("make a guess")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("type a number next time ")
        continue
    if user_guess==random_number:
        print("you got it correct")
        break
    else:
        if user_guess>random_number:
            print("you are above the number")
        else:
            print("you are below the number")
        
print("you got it in",guesses,"guesses")
print("Finish")
