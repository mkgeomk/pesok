import requests
from datetime import datetime

def segodnya():
    data_seg = datetime.now().strftime("%d.%m.%Y")
    return data_seg

def skolko_vremeni():
    vremya = datetime.now().strftime("%H:%M")
    return vremya

instrumenty = [
    {
        "type": "function",
        "function": {
            "name": "skolko_vremeni",
            "description": "Получает текущее время, которое установлено на компьютере и возвращает его в формате чч:мм ",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
            "type": "function",
            "function": {
                "name": "segodnya",
                "description": "Получает текущую дату, которая установлена на компьютере и возвращает ее в формате дд.мм.гггг ",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        }
]
    
def razgovor(istoriya):
    slovar = { 
        "model": "granite4.2:8b",
        "messages": istoriya,
        "stream": False, 
        "options": {"num_predict": 500},
        "tools": instrumenty
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
    limit_krugov = 5
    while True:
        vopros = input("Вопрос: ")
        if vopros.strip() == "":
            continue
        if vopros.lower().strip() == "выход":
            break
        dlina = len(istoriya)
        istoriya.append({"role": "user", "content": vopros})
        otvet = razgovor(istoriya)
        if otvet is None:
            istoriya.pop()
            continue
        print(otvet["message"])
        krugi = 0
        while "tool_calls" in otvet["message"]:
            krugi = krugi + 1
            if krugi > limit_krugov:
                print("Извините, к сожалению модель не успела обработать вопрос за отведенное количество кругов!")
                otvet = None
                break
            imya = otvet["message"]["tool_calls"][0]["function"]["name"]
            if imya == "skolko_vremeni":
                otvet_tulza = skolko_vremeni()
            elif imya == "segodnya":
                otvet_tulza = segodnya()
            else:
                otvet_tulza = "Инструмента " + imya + " не существует!"
            istoriya.append(otvet["message"])
            istoriya.append({"role": "tool", "content": otvet_tulza, "tool_name": imya})
            otvet = razgovor(istoriya)
            if otvet is None:
                break
        if otvet is None:
            while len(istoriya) > dlina:
                istoriya.pop()
            continue
        print(otvet["message"])
        tekst = otvet["message"]["content"]
        istoriya.append({"role": "assistant", "content": tekst})
        print(tekst)

if __name__ == "__main__":
    main()