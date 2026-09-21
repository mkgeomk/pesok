import json

goroda = ["Москва", "Казань", "Сочи"]

with open("goroda.json", "w", encoding="utf-8") as f:
    json.dump(goroda, f, ensure_ascii=False, indent=2)

with open("goroda.json", "r", encoding="utf-8") as f:
    prochitano = json.load(f)

print(prochitano)
print(type(prochitano))
print(len(prochitano))
print(prochitano[0])
