
while True:
    osztalyzat = int(input("Add meg az osztályzatot: "))
    if osztalyzat <= 20 and osztalyzat >= 11:
        print("Nem bukott")
    elif osztalyzat >= 1 and osztalyzat <= 10:
        print("Bukott")
    else:
        print("Hibás paraméter!")
        exit