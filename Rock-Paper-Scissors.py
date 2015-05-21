import random

def stats():

def find_choice(a):
    if a == 1:
        return 'rock!'
    elif a == 2:
        return 'paper!'
    elif a == 3:
        return 'scissors!'

def who_won(cc, choice):
    if choice == '1':
        if cc == 'rock!':
            return "It's a tie!"
            results = 'tie'
        elif cc == 'paper!':
            return 'You lost!'
            results = 'lost'
        elif cc == 'scissors!':
            return 'You won!'
            results = 'won'
    elif choice == '2':
        if cc == 'paper!':
            return "It's a tie!"
            results = 'tie'
        elif cc == 'scissors!':
            return 'You lost!'
            results = 'lost'
        elif cc == 'rock!':
            return 'You won!'
            results = 'won'
    elif choice == '3':
        if cc == 'scissors!':
            return "It's a tie!"
            results = 'tie'
        elif cc == 'rock!':
            return 'You lost!'
            results = 'lost'
        elif cc == 'paper!':
            return 'You won!'
            results = 'won'

print("Welcome to 'Rock, Paper, Scissors' !")
print("Press Ctrl and C to stop this program")
while True:
    print('')
    choice=input("What do you want to choose? Type 1 for rock, 2 for paper and 3 for scissors. Alternatively, you can ask how many times you have won, lost and drawn by typing stats: ")
    if choice == '1':
        cc = find_choice(random.randint(1,3))
        print("You have chosen 'rock' !")
        print("The computer chooses...")
        print(cc)
        print (who_won(cc, choice))
    elif choice == '2':
        cc = find_choice(random.randint(1,3))
        print("You have chosen 'paper' !")
        print("The computer chooses...")
        print(cc)
        print(who_won(cc, choice))
    elif choice == '3':
        cc = find_choice(random.randint(1,3))
        print("You have chosen 'scissors' !")
        print("The computer chooses...")
        print(cc)
        print(who_won(cc, choice))
    elif choice == 'stats':
        print(stats)
    else:
        print("That's not a choice! Try again.")
        pass
