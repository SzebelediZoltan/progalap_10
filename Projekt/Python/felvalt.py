szam = int(input("Add meg a szamot: "))
valto = 0

for i in range(szam):
    if valto == 0:
        print(0, end="")
        valto += 1
    elif valto == 1:
        print(1, end="")
        valto -= 1