import random

def start():
    name = input("Hello! What is your name?\n")
    san = random.randint(0, 20)
    jauap = int(input(f"Well, {name}, i am thinking of a number between 1 and 20.\nTake a guess\n"))
    cnt = 1
    while(jauap != san):
        if(jauap < san):
            print("Your guess is too low. Take other guess\n")
            jauap = int(input())
        else:
            print("Your guess is too high. Take other guess\n")
            jauap = int(input())
        cnt += 1
    print(f"Good job, {name}! You guessed my number in {cnt} guesses!")

start()
        
    
    