import keyboard
import time

keys_pressed = []
last_key_time = time.time()

def on_key_press(key):
    global last_key_time

    if key.name not in ["caps lock", "up", "left", "down", "right", "enter" ,"´", "^", ":", ";", "~","`"]:
        if key.name == "space":  # Verifica se a tecla pressionada é a tecla de espaço
            keys_pressed.append(" ")  # Adiciona um espaço em branco
        else:
            keys_pressed.append(key.name)

        # Imprimir a lista de teclas pressionadas se o tempo desde a última tecla for maior que 5 segundos
        current_time = time.time()
        if current_time - last_key_time > 5:
            last_key_time = current_time
            if keys_pressed:
                keys_str = " ".join(keys_pressed)
                print(keys_str)

keyboard.on_press(on_key_press)

while True:
    time.sleep(0.1)
