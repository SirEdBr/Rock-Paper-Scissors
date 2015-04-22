import random

def find_choice(a):
    if a == 1:
        return 'rock!'
    elif a == 2:
        return 'paper!'
    elif a == 3:
        return 'scissors!'

print("Welcome to 'Rock, Paper, Scissors' !")
print("Press Ctrl and C to stop this program")
while True:
    choice=input("What do you want to choose? Type 1 for rock, 2 for paper and 3 for scissors: ")
    if choice == '1':
        cc = find_choice(random.randint(1,3))
        print("You have chosen 'rock' !")
        print("The computer chooses...")
        print(cc)
    elif choice == '2':
        cc = find_choice(random.randint(1,3))
        print("You have chosen 'paper' !")
        print("The computer chooses...")
        print(cc)
    elif choice == '3':
        cc = find_choice(random.randint(1,3))
        print("You have chosen 'scissors' !")
        print("The computer chooses...")
        print(cc)
    else:
        print("That's not a choice! Try again.")
        pass
    
