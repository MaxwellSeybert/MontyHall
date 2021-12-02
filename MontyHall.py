#Maxwell Seybert
#Monty Hall Extra Credit
import random
#creates a door object that has an attribute of if it is the winning door or not
class door:
    def __init__(self, isWinning):
        self.isWinning = isWinning




def playGame():
    #picks a random number between 1 and 3 to detirmine which door the prize is behind
    winDoor = random.randint(1,3)
    if(winDoor == 1):
        print("Winning door is door 1")
        door1 = door(True)
        door2 = door(False)
        door3 = door(False)
    elif(winDoor == 2):
        print("Winning door is door 2")
        door1 = door(False)
        door2 = door(True)
        door3 = door(False)
    elif(winDoor == 3):
        print("Winning door is door 3")
        door1 = door(False)
        door2 = door(False)
        door3 = door(True)
    #since the player always picks door 1 the playerDoor equals door 1
    #then the host opens a door that is not the winning door and not the player door
    playerDoor = door1
    print("Player picked door 1")
    #if the winning door is door 1 then a random number is picked to determine which door the host will open
    #since the host can open either door
    if(door1.isWinning):
        hostPick = random.randint(1,2)
        if(hostPick == 1):
            hostDoor = door2
            print("Host opened door 2")
        elif(hostPick ==2):
            hostDoor = door3
            print("Host opened door 3")

    #if door 2 is the winning door then the host will open door 3, since door 1 is picked by the player
    #and the host cannot open a winning door
    elif(door2.isWinning):
        hostDoor = door3
        print("Host opened door 3")

    #if door 3 is the winning door then the host will open door 2, since door 1 is picked by the player
    #and the host cannot open a winning door
    elif(door3.isWinning):
        hostDoor = door2
        print("Host opened door 2")

    #Now the function will simulate the player switching doors by seeing which door the host picked and changing the player door

    if(hostDoor == door3):
        playerDoor = door2
        print("Player switched to door 2")
    elif(hostDoor == door2):
        playerDoor = door3
        print("Player switched to door 3")
    #if the player door is the winning door then the function returns true, if the player picked a losing door it returns false
    if(playerDoor.isWinning):
        print("Player won")
        return True
    else:
        print("Player lost")
        return False

    

keepPlaying = "y"
while(keepPlaying == "y"):
    
    #counts how many wins the player has
    winCount = 0
    numGames = 1000
    #a loop that plays 1,000 games
    for i in range(numGames):
        # the play game method returns true if the player won the game, if the player won, it adds 1 to the win count
        print("Game number: " +str(i+1))
        if(playGame()):
            winCount += 1
    #prints out the win count 
    print("The player who always switched won " +str(winCount)+" games out of "+str(numGames))
    keepPlaying = input("Would you like to keep playing? Enter y to keep playing, enter anything else to stop: ")
    
        




