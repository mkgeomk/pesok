goroda = ["Москва", "Казань", "Сочи"]

for gorod in goroda:
    gorod = gorod.upper()

print("после первого цикла:", goroda)

for i in range(len(goroda)):
    goroda[i] = goroda[i].upper()

print("после второго цикла:", goroda)
