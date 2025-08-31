import random

userScore=0
botScore=0
drawScore=0


#print(userChoice)
#print(botChoice)

def play():
    userChoice = input("Enter your choice r p s").lower()
    rps = ["paper","scissor","rock"]
    botChoice = random.choice(rps)

    if(userChoice=="r"):
        choice="rock"
    elif(userChoice=="p"):
        choice="paper"
    else:
        choice="scissor"

    while(True):
        global userScore,botScore,drawScore
        if(choice==botChoice):
            print("Your choice : ",choice)
            print("Bot choice : ",botChoice)
            print("It is a draw")
            drawScore+=1
            print(f"Score : User - {userScore} | {botScore} - bot | draw - {drawScore}")
            break
            
        elif((choice=="rock" and botChoice=="paper")or(choice=="paper" and botChoice=="scissor") or (choice=="scissor" and botChoice=="rock")):
            print("Your choice : ",choice)
            print("Bot choice : ",botChoice)
            print("Bot wins")
            botScore+=1
            print(f"Score : User - {userScore} | {botScore} - bot | draw - {drawScore}")
            break
            
        elif((choice=="rock" and botChoice=="scissor")or(choice=="paper" and botChoice=="rock") or (choice=="scissor" and botChoice=="paper")):
            print("Your choice : ",choice)
            print("Bot choice : ",botChoice)
            print("You win")
            userScore+=1
            print(f"Score : User - {userScore} | {botScore} - bot | draw - {drawScore}")   
            break




def numberOfRounds():
    print("Best out of how many times")
    print("press 1 for best out of 3")
    print("press 2 for best out of 5")
    print("press 3 for best out of 7")
    print("press 4 for custom number of rounds")

    n = int(input())

    if(n==1):
        return 3
    elif(n==2):
        return 5
    elif(n==3):
        return 7
    elif(n==4):
        m=int(input("Enter the number"))
        return m
    
class Rounds:

    def __init__(self):
        self.n=numberOfRounds()

    def rounds(self):
        for i in range(self.n):
            play()
    

run = Rounds()
run.rounds()