print("Welcome to this amazing quiz")
playing=input("Are you intrested in playing this game?   ")
if playing.lower()=="yes":
    print("playing.. ")
  
else:
    print("lets play")
    quit()

score=0

QUESTION1= input("What is the full form of CPU?   ")
if QUESTION1.lower() == "central processing unit":
    print("correct")
    score+=1
else:
    print("incorrect answer")
QUESTION2= input("What is the full form of RAM?   ")
if QUESTION2.lower() == "random access memory":
    print("correct")
    score+=1
else:
    print("incorrect answer")
QUESTION3= input("What is the full form of AI?   ")
if QUESTION3.lower()== "artificial intelligence":
    print("correct")
    score+=1
else:
    print("incorrect answer")
QUESTION4= input("What is the full form of GPU?   ")
if QUESTION4.lower() == "graphic processing unit":
    print("correct")
    score+=1
else:
    print("incorrect answer")

print("you got" + str(score)+  "questions correct")
print("Your final score is",(4/score)*100, "%")


