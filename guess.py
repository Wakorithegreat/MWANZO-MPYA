import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"enter a random number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print("uko chini ya value, kaa pipes za shonde!")
        elif guess > random_number:
            print("umepita value, Usain")
    print(f"Sawa boss we ndio unajiona yesu! Umepata nambari kama: {random_number}, juu hauna maisha!")

guess(10)