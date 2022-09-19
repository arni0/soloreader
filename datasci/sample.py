import pickle as pk
import picl as pc

def func(x, y):
    print(x + y)

def checkxp(lvl, xp, remxp):
    while True:
        if xp < ((1*(lvl**2)) + (1*(lvl))):
            break
        lvl +=1
    print(lvl)
    remxp = xp - ((1*((lvl-1)**2)) + (1*(lvl-1)))
    print(remxp)
    if remxp == 0:
        print("You hit a new level " + str(lvl))

b = pc.bb

pc.cringe(b)
