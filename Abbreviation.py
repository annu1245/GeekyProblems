# Abbreviation

x = 'aBcdhf'
y = 'ABCDL'
x = x.upper()
i = 0
while i<len(x):
    if x[i] not in y:
        x = x.strip(x[i])
    i+=1
if x == y:
    print("yes")
else:
    print("no")