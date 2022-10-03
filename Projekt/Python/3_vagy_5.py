szam = int(input("Szam: "))

harom = szam % 3
öt = szam % 5

if harom == 0 or öt == 0:
    print("Igen")
else:
    print("Nem")