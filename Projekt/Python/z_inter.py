also = int(input("Add meg az alsó határt: "))
felso = int(input("Add meg a felső határt: "))

for i in range(felso - also - 1):
    also += 1
    if also % 2 == 0:
        print(also, end=" ")
    else:
        continue