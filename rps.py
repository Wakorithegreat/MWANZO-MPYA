import random
import math

def play():
    print("Mchezo wa rock(vile mpoa yako hupenda vitu ngumu), paper(juu ya nini?) na scissors(manzi wenu) \n")
    user = input("Choose between rock 'r', paper 'p', and scissors 's'! \n")
    user = user.lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return (0,user,computer)
    
    # r > s, s > p, p > r
    if is_win(user,computer):
        return( 1,user,computer)
    
    return (-1,user,computer)

def is_win(player,opponent):
    #return true if player beats opponent
    #winning conditions r > s, s > p, p > r
    if (player =='r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # play against computer until someone win best of n games
    #to win, you must play ceil(n/2) ie(2/3,4/7,3/5)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result,user,computer = play()

        if result == 0:
            # draw
            print("You and computer chose {}, and its a tie! \n".format(computer))
            
        elif result == 1:
            #user wins
            player_wins += 1
            print("You have choosen {} and the computer has choosen {}, Sawa winner! \n".format(user,computer))

        else:
            #user lost
            computer_wins += 1
            print("You have choosen {} and the computer has choosen {}, Soma sana, loser! \n".format(user,computer))
        print('\n')

    if player_wins > computer_wins:
        print("Congrats you have won best out of {} games, against the computer! ".format(n))
    else:
        print("Unfortunately you have lost out of {} games, against the computer, next time buda! ".format(n))

if __name__ == '__main__':
    play_best_of(3)