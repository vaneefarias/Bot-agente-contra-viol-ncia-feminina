import random

# definindolistas

respostas_oi = [
    "olá, como vai?",
    "Oi! Sou o Robo, prazer.",
    "Opa, beleza?",
    "Salve! Em que posso ajudar?",
]

respostas_erro = [
    "Não entendi...",
    "Pode repetir? Meus circuitos falharam.",
    "Essa eu ainda não aprendi.",
    "Hã? Tente digitar 'ajuda'.",
]

nome_bot = "Robo"

print(f"-{nome_bot} Iniciado (digite 'sair' para fechar) ---")

while True:
    # 1. Captura a entrada e padroniza
    comando = input("Você: ").lower().strip()

    # 2. Condição de saída (essencial vir primeiro)
    if comando == "sair":
        print(f"{nome_bot}: {random.choice(['Tchau!', 'Até a próxima!', 'Fui!'])}")
        break

    # 3. Lógica de Processamento (A "Mente" do Bot)
    if "olá" in comando or "oi" in comando:
        escolha = random.choice(respostas_oi)
        print(f"{nome_bot}: {escolha}")

    elif "horas" in comando:
        print(f"{nome_bot}: Agora é hora de aprender Python!")

    elif "ajuda" in comando:
        print(f"{nome_bot}: Eu entendo: 'oi', 'horas' e 'sair'.")

    elif "legal" in comando:
        print(f"{nome_bot}:Muito!")

    else:
        # Resposta padrão para comandos desconhecidos
        print(f"{nome_bot}: {random.choice(respostas_erro)}")