#Összes listának a helye lefoglalása
össz_lista = []

#Listák létrehozása
Minecraft = ["Minecraft", "Mojang Studios", "126 millió", "11.441Ft"]
Terraria = ["Terraria", "Re-Logic", "44 millió", "3.814Ft"]

#Listák behelyezése
össz_lista.append(Minecraft) 
össz_lista.append(Terraria)

#Kettő segéd lista helyének lefoglalása
nevek = []
mit = []

#A listák neveinek behelyezése
for i in össz_lista:
    nevek.append(i[0])

#Felhasználó adatainak beolvasása    
print("Elérhető játékok:", end=" ")
print(nevek)
mit = input("Minek az adatait akarod látni?:")

#Adatok kiírása
for i in össz_lista:
    if mit == i[0]:
        print("\nNév: "+i[0], "Fejlesztő: "+i[1], "Eladott példány: "+i[2], "Ár: "+i[3], sep="\n")
    else:
        continue

#KÉSSSSZSZSZS!!!
print("\nKÉSSSSZSZSZS!!!")

    
