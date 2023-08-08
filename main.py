import keyboard
import time

sentences = []
current_sentence = ""
last_key_time = time.time()

def on_key_press(key):
    global current_sentence, last_key_time

    if key.name == "backspace":
        if current_sentence:
            current_sentence = current_sentence[:-1]  # Remove o último caractere da frase
    elif key.name == "enter":
        if current_sentence:
            sentences.append(current_sentence)  # Adiciona a frase à lista de frases
            current_sentence = ""  # Reseta a frase atual
    elif key.name not in ["caps lock", "up", "left", "down", "right", "´", "^", "~", "`"]:
        if key.name == "space":
            current_sentence += " "
        else:
            current_sentence += key.name

        current_time = time.time()
        if current_time - last_key_time > 0.2:
            last_key_time = current_time
            if current_sentence:
                print("Current Sentence:", current_sentence)
                if sentences:
                    print("Previous Sentences:", sentences)

keyboard.on_press(on_key_press)

while True:
    time.sleep(0.1)
