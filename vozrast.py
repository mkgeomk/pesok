import sys

try: 
    vozrast = int(input("Сколько тебе лет? "))
except ValueError:
    print("Напишите число арабскими цифрами")
    sys.exit(1)
else:
    print("Через 10 лет тебе будет:", vozrast + 10)
