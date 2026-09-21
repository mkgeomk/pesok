goroda = ["Москва", "Казань","Сочи" ]

with open("goroda.txt", "w", encoding= "utf-8") as f:
    f.write(str(goroda))
    

with open("goroda.txt", "r", encoding="utf-8") as f:
    prochitano = f.read()

print(prochitano)
print(type(prochitano))
print(len(prochitano))
print(prochitano[0])

