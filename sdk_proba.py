from ollama import chat
istoriya = [
    {"role": "system", "content": "Отвечай кратко, одним-двумя предложениями. Без эмодзи."}, 
    {"role": "user", "content": "Назови столицу России"}
]

otvet = chat(model="granite4.2:8b", messages=istoriya)

print(otvet["message"]["content"])