#This carries out the management of the game itself.

def query(queryMsg, acceptedMsgs = []):
    moveon = False
    while not moveon:
        x = input(queryMsg)
        if acceptedMsgs:
            if x in acceptedMsgs:
                return x
            else:
                print(x + ' not valid, accepted: ' + str(acceptedMsgs))
        else:
            return x

if __name__ == '__main__':
    #Query the number of players (1-4)
    numPlayers = int(query('Enter number of players(1-4): ', ['1', '2', '3', '4']))
    from lib import descentmodel
    gameBoard = descentmodel.DescentGame(numPlayers)