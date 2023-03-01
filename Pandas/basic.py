l=[10,6,7,4,9,8]
minl=sorted(l)[0]
maxl=-1
pr=0
n=0
for val in range(l.index(minl),len(l)):
    n=l[val]-minl
    if n>pr:
        maxl=l[val]
        pr=n

print(f"maximum gap is between {minl} and {maxl} which is {maxl-minl}")
    