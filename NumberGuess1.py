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
            if guess > a:
                print("Too high")
            else:   
                print("Too Low")
        myrightguess()
        break
            
myrightguess()