def welcome():
    print ('Enter name')
    name = input ()
    print ("Hello " + name + " and welcome to the world Of Game (WOG) "
                             "here you can find many cool games to play")
    


def Load_game():
    print ("please choose a game to play")
    print ("1-memory game-a sequence of numbers will appear for 1 second and you have to"
           "guess it back")
    print ("2-Guess Game - guess a number and see if you chose like the computer")
    print ("3-Currency Roulette - try and guess the value of a random amount of USD in ILS")
    print ("Enter your choose: ")
    choose=input ()
    print ("please choose game difficulty from 1 to 5")
    difficulty=input ()
    print("you choose level "+ choose)
    print("difficulty " +difficulty)
    list_1=[choose,difficulty]
    return list_1



