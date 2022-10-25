#from pickle import TRUE
import time as tm
import pickle as pk

# Get current date and time
#print(time.ctime(0))
#print(time.time())

#print(tm.ctime(tm.time()))

# get time, make timer property as true
# if timer is true, ask if you want to continue or stop timer from input
# when timer stopped, get final time and calculate delta time
# if it is paused, get delta pause from final and initial time

fruct = input(">> ")

iTime = int(0)
fTime = int(0)
dTime = int(0)

def initTime(iTime, dTime, fTime):
    iTime = tm.time()
    print("iTime: " + str(iTime))
    
    ask = input("Stop timer [Y/N] \n -> ")

    if ask.lower() == "y":
        timer_prop = False
        print(timer_prop)

        fTime = tm.time()
        print("fTime: " + str(fTime))
        dTime = round(fTime - iTime)
        print("delta time: " + str(dTime))
    elif ask.lower() == "n" or "no":
        timer_prop = True
        print(timer_prop)
        exit()
    else:
        print("Invalid statemtent.")

def getTime(iTime, dTime):

    inputTime = str(input("Start timer [Y/N] \n -> "))
    
    if inputTime.lower() == "y":
        timer_prop = True
        print(timer_prop)

        initTime(iTime, fTime, dTime)
    elif inputTime.lower() == "n":
        timer_prop = False
        print(timer_prop)
        
        exit()
    else:
        print("Invalid statement.")

if fruct.lower() == "timer":
    getTime(iTime, dTime)
else:
    print("Invalid input")

#if timer prop != True, store fTime
#else timer prop == True, store iTime
#summin like that bruv

def time_convert(dTime):
    True
