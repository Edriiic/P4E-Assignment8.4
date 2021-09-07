fname = input ("Enter Name of File: ")
fhand = open (fname)
lot =list()
for line in fhand:
    ok = line.rstrip()
    ok = ok.split()
    for element in ok:
        if element in lot:
            continue
        else:
            lot.append(element)
lot.sort()
print(lot)
