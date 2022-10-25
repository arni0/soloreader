import pickle as pk


# saving
#with open('savefile.dat', 'wb') as f:
#    pk.dump((timer_prop), f, protocol=2)
#print(timer_prop)

# loading
#with open('savefile.dat', 'rb') as f:
#    timer_prop = pk.load(f)
#print("done " + str(timer_prop))

with open('savefile.dat', 'rb') as f:
    timer_prop = pk.load(f)
print(timer_prop)

def proTime(timer_prop):
    
    with open('savefile.dat', 'rb') as f:
        timer_prop = pk.load(f)

    if timer_prop == True:
        ask = str(input("stop timer? \n -> "))
        print(" ")
        
        if ask == "y":
            print("delta time calculated.")
            
            timer_prop = False
            with open('savefile.dat', 'wb') as f:
                pk.dump((timer_prop), f, protocol=2)

        elif ask == "n":
            print("timer is still running.")

            timer_prop = True
            with open('savefile.dat', 'wb') as f:
                pk.dump((timer_prop), f, protocol=2)
            
            exit()
        else:
            print("Invalid statement.")
    
    elif timer_prop == False:
        ask = str(input("start timer? \n -> "))
        print(" ")

        if ask == "y":
            print("timer started.")
            
            timer_prop = True
            with open('savefile.dat', 'wb') as f:
                pk.dump((timer_prop), f, protocol=2)
        
        elif ask == "n":
            print("timer is not started.")
            
            timer_prop = False
            with open('savefile.dat', 'wb') as f:
                pk.dump((timer_prop), f, protocol=2)

        else:
            print("Invalid statement.")
    
    else:
        print("Invalid statement.")

if timer_prop == True:
    print("timer is running. \n")
elif timer_prop == False:
    print("timer is not running. \n")
else:
    print("Invalid statement. \n")

proTime(timer_prop)
