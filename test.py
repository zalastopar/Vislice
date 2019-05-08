n = 200
prastevila = []

for el in range(2,200):
    for stevilka in range(2, el):
        if el%stevilka == 0:
            break
    prastevila.append(el)