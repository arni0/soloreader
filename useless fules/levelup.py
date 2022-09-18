xpdaily = 15
xptest = 50

notest = int(input("no. of tests: "))
nodays = int(input("no. of days: "))

xp = ((notest * 6) * xptest) + (nodays * xpdaily)
print(xp)


"""
XP levels
{
    daily task rewarding 7xp after 300 days: 2100, lvl 32
               -//-      12xp, after 300 days: 3600, lvl 42
    level 40 (job change): 3120 xp

    daily xp: 15
    test xp: 50
}
"""
#xp = int(input("xp = "))
lvl = 0
remxp = 0

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

checkxp(lvl, xp, remxp)
