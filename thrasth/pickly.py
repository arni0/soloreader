import pickle

player = "kurosai"
level_state = "bruh"

# saving
with open('savefile.dat', 'wb') as f:
    pickle.dump([player, level_state], f, protocol=2)
print(player + level_state)

# loading
with open('savefile.dat', 'rb') as f:
    player, level_state = pickle.load(f)
print("done " + player + level_state)