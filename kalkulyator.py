print("Внутри kalkulyator __name__= ", __name__)

def slozhit(a,b):
    return a + b

if __name__ == "__main__":
    print("файл", __file__)
    print("Считаю 2 + 2 =", slozhit(2,2))

