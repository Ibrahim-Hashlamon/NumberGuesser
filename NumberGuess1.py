import random

a = random.randrange(0, 100)

print(a)


def myrightguess():
    guess = int(input("Please input a number: "))
    while guess:
        if guess == a:
            print("Nice")
            break
        else:
            myrightguess()
            break
            
myrightguess()