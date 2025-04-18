# 🕵️ Keylogger Educativo com Python

Este projeto é um **keylogger educativo**, desenvolvido em Python, com o objetivo de ensinar como funciona a captura de teclas em segundo plano, incluindo o tratamento correto de **acentos e teclas mortas** (`´`, `~`, `^`) em teclados com layout **ABNT2 (Português do Brasil)**.

> ⚠️ **Atenção:** Este projeto é apenas para fins educacionais. Não use este código para invadir a privacidade de ninguém. O uso indevido pode ser considerado crime conforme as leis da sua jurisdição.

---

## 🎯 Funcionalidades

✅ Captura todas as teclas digitadas em tempo real  
✅ Interpreta acentos corretamente (ex: `´ + a = á`)  
✅ Respeita letras maiúsculas/minúsculas  
✅ Funciona com teclado ABNT2 (brasileiro)  
✅ Registra frases completas ao pressionar `Enter`  
✅ Executa em segundo plano até que `ESC` seja pressionado  

---

## 📷 Exemplo de uso

- Digite: Olá, meu nome é João
- Saída: Frase registrada: Olá, meu nome é João

---

## 🛠️ Requisitos

- Python 3.7+
- Biblioteca `pynput`

Instale as dependências com:

```bash
pip install pynput
```

## 👨‍🏫 Passo a Passo — Criando uma senha de app no Gmail
1. Entre em https://myaccount.google.com/security
2. Role até “Verificação em duas etapas” e ative (se ainda não tiver feito isso).
3. Depois que estiver ativado, você verá a opção chamada “Senhas de app”. Clique nela.

**No menu:**

4. Escolha "Outro (nome personalizado)"
5. Digite algo como: Keylogger Demo
6. Clique em Gerar

### O Google vai te dar uma senha de 16 caracteres, algo assim:
`abcd efgh ijkl mnop`
<br></br>Use essa senha no lugar da senha normal no seu script.

## 🚀 Como rodar
### Clone o repositório:

```bash
git clone https://github.com/Paulo19961944/Keylooger-Python.git
cd Keylooger-Python
```

### Execute o script:

```bash
python main.py
```

- Digite livremente no teclado.
- Pressione Enter para registrar a frase.
- Pressione ESC para encerrar o programa.

## 📁 Estrutura
```bash
📦 Keylooger-Python/
├── main.py         # Código principal do keylogger
└── README.md       # Este arquivo de documentação
```
## 👨‍🏫 Sobre teclas mortas (Dead Keys)
Dead keys são teclas como ´, ~, ^, que não produzem um caractere por si só, mas combinam com a próxima letra para formar um caractere acentuado (ex: ´ + a = á). Este keylogger reconhece essas combinações e gera os acentos corretamente.

## 🤝 Licença
- Este projeto é distribuído sob a licença MIT.
- Use com responsabilidade.

## 🧠 Objetivo educacional
Este código é ideal para quem quer aprender sobre:

- Manipulação de eventos de teclado com Python
- Funcionamento de teclados com layout brasileiro
- Composição de caracteres com teclas mortas
- Criação de scripts que rodam em segundo plano

## ✍️ Autor
- Feito com 💻 por Paulo Henrique Azevedo do Nascimento
- Entre em contato: nascimentopaulo804@gmail.com
