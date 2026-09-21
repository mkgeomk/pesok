import requests

def razgovor(istoriya):
    slovar = { 
        "model": "granite4.2:8b",
        "messages": istoriya,
        "stream": False
    }
    try:
        otvet=requests.post("http://localhost:11434/api/chat", json=slovar)
    except requests.exceptions.RequestException:
        print("Нет связи с сервером")
        return None
    if otvet.status_code != 200:
        print("Код ошибки: ", otvet.status_code)
        return None
    return otvet.json()
def main():
    istoriya = [{"role": "system", "content": "Отвечай кратко, одним-двумя предложениями. Без эмодзи."}]
    while True:
        vopros = input("Вопрос: ")
        if vopros.strip() == "":
            continue
        if vopros.lower().strip() == "выход":
            break
        istoriya.append({"role": "user", "content": vopros})
        otvet = razgovor(istoriya)
        if otvet is None:
            istoriya.pop()
            continue
        tekst = otvet["message"]["content"]
        istoriya.append({"role": "assistant", "content": tekst})
        print(tekst)

if __name__ == "__main__":
    main()