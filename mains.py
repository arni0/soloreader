#tell em wassup

import pickle as pk

timer_prop = True
timer_dumps = pk.dumps(timer_prop)
timer_loads = pk.loads(timer_dumps)
print(timer_loads)
timer_prop = False
timer_dumps = pk.dumps(timer_prop)
timer_loads = pk.loads(timer_dumps)
print(timer_loads)