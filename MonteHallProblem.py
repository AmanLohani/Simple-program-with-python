import random
door = [0]*3
goatdoor = [0]*2
swap = 0
dont_swap = 0
j = 0
games = int(input("Enter number of games to play"))
while j<games:
    x = random.randint(0,2)
    door[x] = '1 billion dollars'
    for i in range(0, 3):
        if (i==x):
            continue
        else:
            door[i] = 'Goat'
            goatdoor.append(i)
    choice = int(input("Enter your choice"))
    door_open = random.choice(goatdoor)
    while(door_open == choice):
        door_open = random.choice(goatdoor)
    ch = input("Do you want to swap?:y/n")
    if ch == 'y':
        if(door[choice] == 'Goat'):
            print("Player won")
            swap = swap+1
        else:
            print("Player lost")
    else:
        if(door[choice] == 'Goat'):
            print("Player lost")
        else:
            print("Player won")
            dont_swap = dont_swap+1
    j = j+1

print("Games played: ", games)
print("Victories after swapping", swap)
print("Victories without swapping", dont_swap)
