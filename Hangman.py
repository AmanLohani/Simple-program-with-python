import random
def hangman():
    words = random.choice(["dark", "trek", "black", "green", "pink", "red", "jack"])
    validinput = 'abcdefghijklmnopqrstuvwxyz'
    guessmade = ''
    turns = 10
    while len(words) > 0:
        main = ""
        for letter in words:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == words:
            print(main)
            print("You won")
            break
        print("Guess the word", main)
        guess = input()
        if guess in validinput:
            guessmade = guessmade + guess
        else:
            print("Enter valid characters")
            guess = input()
        if guess not in words:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("  ________  ")
            if turns == 8:
                print("8 turns left")
                print("  _________  ")
                print("      O      ")
            if turns == 7:
                print("7 turns left")
                print("  _________  ")
                print("      O /   ")
            if turns == 6:
                print("6 turns left")
                print("  _________  ")
                print("    \ O /   ")
            if turns == 5:
                print("5 turns left")
                print("  _________  ")
                print("    \ O /   ")
                print("      |      ")
            if turns == 4:
                print("4 turns left")
                print("  _________  ")
                print("    \ O /   ")
                print("      |      ")
                print("       \    ")
            if turns == 3:
                print("3 turns left")
                print("  _________  ")
                print("    \ O /   ")
                print("      |      ")
                print("     / \    ")
            if turns == 2:
                print("2 turns left")
                print("  _________  ")
                print("    \ O /|  ")
                print("      |      ")
                print("     / \    ")
            if turns == 1:
                print("1 turns left")
                print("Only 1 last turn")
                print("  _________  ")
                print("    \ O_|/   ")
                print("      |      ")
                print("     / \    ")
            if turns == 0:
                print("You lost")
                print("An innocent man died because of you")
                print("  _________  ")
                print("      O_|     ")
                print("     /|\      ")
                print("     / \    ")
                break


name = input("Enter your name")
print("Welcome %s"%name)
print("-------------")
print("Guess the word in 10 turns")
hangman()
print()
