import pickle

timer_prop = True

# saving
with open('savefile.dat', 'wb') as f:
    pickle.dump((timer_prop), f, protocol=2)
print(timer_prop)

# loading
with open('savefile.dat', 'rb') as f:
    timer_prop = pickle.load(f)
print("done " + str(timer_prop))