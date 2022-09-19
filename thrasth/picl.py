import pickle as pk

# initializing data to be stored in db
Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
'age' : 21, 'pay' : 40000}
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}
  
# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish
  
# For storing
b = pk.dumps(db)       # type(b) gives <class 'bytes'>
  
# For loading
myEntry = pk.loads(b)
#print(myEntry)

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
