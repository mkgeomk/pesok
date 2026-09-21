naselenie = {
    "Москва": 13.1,
    "Казань": 1.3,
    "Сочи": 0.5,
}

print(naselenie)
print(len(naselenie))
print(naselenie["Казань"])

naselenie["Тверь"] = 0.4
naselenie["Сочи"] = 0.55
print(naselenie)
print(len(naselenie))

print(naselenie.get("Пермь"))
print(naselenie.get("Пермь", 0))

for gorod, chislo in naselenie.items():
    print(gorod, chislo)

print(naselenie["Пермь"])
