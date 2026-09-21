goroda = ["Москва", "Казань", "Сочи", "Тверь"]

for gorod in goroda:
    print(gorod)

print("---")

for gorod in goroda:
   print(gorod, len(gorod))

print("---")

for i in range(3):
    print(i)

print("---")

for i in range(len(goroda)):
    print(i, goroda[i])
