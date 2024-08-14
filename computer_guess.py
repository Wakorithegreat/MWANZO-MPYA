import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low

        feedback = input(f"Vile nimeguess {guess} niko chini,(L), niko juu,(H) ama niko bie,(C)! ").lower()
        if feedback == 'l':
            guess = guess + 1
        elif feedback == 'h':
            guess = guess - 1
    print(f"AI imezidi! hiyo guess {guess} iko best.")

computer_guess(10)