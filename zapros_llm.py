import requests
from datetime import datetime

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
        if "tool_calls" in otvet["message"]:
            istoriya.append(otvet["message"])
            sey_chas = skolko_vremeni()
            istoriya.append({"role": "tool", "content": sey_chas, "tool_name": "skolko_vremeni"})
            otvet = razgovor(istoriya)
        print(otvet)
        tekst = otvet["message"]["content"]
        istoriya.append({"role": "assistant", "content": tekst})
        print(tekst)

if __name__ == "__main__":
    main()