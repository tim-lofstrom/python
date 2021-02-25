


def bounce():

    n = 10
    turn = 1

    while turn <= 4:
        while n >= 4:
            print n
            n -= turn
        n = 10
        turn += 1
        if turn == 5:
            print 2
        
        

    
bounce()
