import pickle as pk
import sample
import useless_fules.levelup as lp

x = 23
y = 90

sample.func(x, y)
sample.checkxp(0, 2453, 0)

lvl = 0
remxp = 0

xpdaily = 15
xptest = 50

notest = int(input("no. of tests: "))
nodays = int(input("no. of days: "))

xp = ((notest * 6) * xptest) + (nodays * xpdaily)

lp.checkxp(lvl, xp, remxp)
