import random
def game(comp, me):
    if(me == comp):
        return None
    elif(me == 'g' and comp == 's'):
        return True
    elif(me == 'w' and comp == 'g'):
        return True
    elif(me == 's' and comp == 'w'):
        return True
    else:
        return False
me = input("Enter s, w or g for Snake, Water and Gun: ")
choice = ('s', 'w', 'g')
num = random.randint(0,2)
comp = choice[num]
print(f"You choose {me} and comp choose {comp}")
if(game(comp,me)):
    print("YOU WON")
elif(game(comp,me) == None):
    print("GAME DRAW")
else:
    print("YOU LOOSE")