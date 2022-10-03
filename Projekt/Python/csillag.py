x = int(input("Add meg az oszlopokat: "))
y = int(input("Add meg a sorokat: "))

def oszlopsor(x, y):
    for m in range(y):
        print("*" * x)

oszlopsor(x, y)
    