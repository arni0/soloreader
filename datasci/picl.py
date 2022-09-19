import pickle as pk

bb = 0

dumps = pk.dumps(bb)
breh = pk.loads(dumps)
print(breh)

def cringe(bb):
    
    if input() == "truee":
        bb += 1
    else:
        bb += 0
    
    print(bb)

cringe(bb)
dumps = pk.dumps(bb)
breh = pk.loads(dumps)