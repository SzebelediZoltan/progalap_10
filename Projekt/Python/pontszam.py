x = int(input(("Írd be a pontszámod: ")))

also = [0, 50, 60, 70, 85]
felso = [50, 60, 70, 85, 999]
jegy = [1, 2, 3, 4, 5]

for i in range(5):
    if also[i] <= x and x < felso[i]:
        print("Az érdemjegyed:", jegy[i])
    else:
        continue