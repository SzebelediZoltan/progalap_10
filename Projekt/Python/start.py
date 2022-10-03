szokoz = int((input("Ird be a számot: ")))

if type(szokoz) != int or szokoz > 20 or szokoz < 0:
    print("Szar lehet :(")
else:
    print(" " * szokoz, "START!", sep=(""))  