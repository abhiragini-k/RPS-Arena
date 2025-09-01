import random

'''userScore=0
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
    print("Choose series length (best of N, N must be odd):")
    print("1) Best of 3")
    print("2) Best of 5")
    print("3) Best of 7")
    print("4) Custom odd number")

    n = int(input("Enter choice [1-4] : "))

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
        self.m=mainDashboard()
        self.n=numberOfRounds()

    def rounds(self):
        for i in range(self.n):
            play()
    


def mainDashboard():
    print("========= RPS-Arena ==========")
    print("1) Quick Match vs CPU")
    print("2) Local PvP")
    print("3) Show Leaderboard")
    print("4) Reset Leaderboard")
    print("5) Quit")

    go = int(input("Choose an option [1-5]"))

    if go==1:
        name = input("Enter you name")
        print("Choose the difficulty level")
        print("1) Easy (random)")
        print("2) Medium (Frequency)")
        print("3) Hard (Predictive)")
        difficulty = int(input("Enter choice [1-3]"))

        






run = Rounds()
run.rounds()
'''

class Player:
    def __init__(self,name="bot"):
        self.name = name
        self.score = 0

    def addPoints(self):
        self.score += 1

class Game:
    valid_moves = ["rock","paper","scissor"]

    def __init__(self,user,bot):
        self.user = user
        self.bot = bot
        self.draws = 0

    def play_round(self):
        move = input("Enter your choice (r/p/s) : ").lower()
        rps = {"r":"rock","p":"paper","s":"scissor"}
        user_choice = rps.get(move)
        if move not in rps:
            print("Invalid input!")
            return
        bot_choice = random.choice(self.valid_moves)
        print(f"{self.user.name} : {user_choice}")
        print(f"{self.bot.name} : {bot_choice}")
        
        if(user_choice==bot_choice):
            print("It is a draw!")
            self.draws+=1
        elif((user_choice=="rock" and bot_choice=="scissor") or 
             (user_choice=="paper" and bot_choice=="rock") or
             (user_choice=="scissor" and bot_choice=="paper")):
            print(f"{self.user.name} wins!")
            self.user.addPoints()
        else:
            print("Bot wins!")
            self.bot.addPoints()

        self.show_score()

    def show_score(self):
        print(f"Score => {self.user.name} : {self.user.score} , {self.bot.name} : {self.bot.score}, Draws : {self.draws}")

    def play_series(self):
        for i in range(self.no_of_rounds()):
            self.play_round()
        print("=== Final Score ===")
        self.show_score()

    def no_of_rounds(self):
        print("Enter the no of rounds")
        print("1) Best of 3")
        print("2) Best of 5")
        print("3) Best of 7")
        print("4) Custom choice")
        n = int(input("Enter choice [1-4] : "))
        if(n==1):
            return 3
        elif(n==2):
            return 5
        elif(n==3):
            return 7
        elif(n==4):
            m = int(input("Enter your custom number"))
            return m

if __name__ == "__main__":
    user = Player(input("Enter your name"))
    bot = Player("Bot")
    game = Game(user, bot)
    game.play_series()
        