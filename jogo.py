import random
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

print(f"🎮✨ BEM-VINDO A PYTHEMATICA: O DESAFIO DO LABIRINTO! 🌟🎲")
time.sleep(1)
print(f"⛓️  Você e outro jogador foram lançados em um labirinto mortal cheio de enigmas. 💀")
time.sleep(2)
print(f"🧠 Somente o mais sábio conseguirá escapar vivo e vencer o desafio! 🏆")
time.sleep(2)
print(f"❓ Responda corretamente para avançar... mas cuidado: errar pode ser fatal! 💣")
time.sleep(2)
print(f"⚔️  Que comecem os desafios! Boa sorte, jogadores! 🍀")
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')

pergunta = {
    1: {"Pergunta": "Qual é o resultado de 10 - 4?"},
    2: {"Pergunta": "Quanto é 3 x 5?"},
    3: {"Pergunta": "Qual é o quociente de 15 dividido por 3?"},
    4: {"Pergunta": "Qual é o menor número primo?"},
    5: {"Pergunta": "Quanto é 7 elevado ao quadrado?"},
    6: {"Pergunta": "Qual é a raiz quadrada de 81?"},
    7: {"Pergunta": "Quantos lados tem um hexágono?"},
    8: {"Pergunta": "Qual é o maior divisor comum de 18 e 24?"},
    9: {"Pergunta": "Qual é o valor de π arredondado para duas casas decimais?"},
    10: {"Pergunta": "Qual é a soma dos ângulos internos de um triângulo?"},
    11: {"Pergunta": "Qual é a função usada para imprimir algo na tela em Python?"},
    12: {"Pergunta": "Qual símbolo é usado para comentar uma linha de código em Python?"},
    13: {"Pergunta": "Qual é o operador de igualdade em Python?"},
    14: {"Pergunta": "Como você importa uma biblioteca em Python?"},
    15: {"Pergunta": "Qual é o índice inicial de uma lista em Python?"},
    16: {"Pergunta": "Qual palavra-chave é usada para definir uma condição em Python?"},
    17: {"Pergunta": "Qual é o operador usado para divisão inteira em Python?"},
    18: {"Pergunta": "Qual é o operador lógico para 'e' em Python?"},
    19: {"Pergunta": "Qual é o operador lógico para 'ou' em Python?"},
    20: {"Pergunta": "Qual palavra-chave encerra um loop em Python?"},
}

resposta = {
    1: {"Resposta": "6"},
    2: {"Resposta": "15"},
    3: {"Resposta": "5"},
    4: {"Resposta": "2"},
    5: {"Resposta": "49"},
    6: {"Resposta": "9"},
    7: {"Resposta": "6"},
    8: {"Resposta": "6"},
    9: {"Resposta": "3.14"},
    10: {"Resposta": "180"},
    11: {"Resposta": "print"},
    12: {"Resposta": "#"},
    13: {"Resposta": "=="},
    14: {"Resposta": "import"},
    15: {"Resposta": "0"},
    16: {"Resposta": "if"},
    17: {"Resposta": "//"},
    18: {"Resposta": "and"},
    19: {"Resposta": "or"},
    20: {"Resposta": "break"},
}

dado = 0
casajog1 = 0
casajog2 = 0
respostaa = 0
casaatual = 0

while True:

    print(f"É a vez do Jogador 1!")
    input("Aperte ENTER para jogar o dado 🎲")
    os.system('cls' if os.name == 'nt' else 'clear')
    dado = random.randint(1,6)
    print(f"Jogador 1:")
    print (f"O dado parou no 🎲 {dado} 🎲")
    print(f"🏠 Sua casa atual é {casajog1} 📍")
    casaatual = casajog1 + dado

    if casaatual > 20:
        casaatual = 20 - (casaatual - 20)

    print(pergunta[casaatual])
    respostaa = str(input("Resposta: "))
    if respostaa == resposta[casaatual]["Resposta"]:
        casajog1 = casaatual
        print("😁 Parabéns, você acertou ✅")
        print(f"🚀 Avançou para a casa {casajog1} 🏠✨")
    else:
        print("😭 Você errou ❌")
        print(f"📌 Você continua na mesma casa: {casajog1} 🏠")

    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')



    print(f"É a vez do Jogador 2!")
    input("Aperte ENTER para jogar o dado 🎲")
    os.system('cls' if os.name == 'nt' else 'clear')
    dado = random.randint(1,6)
    print(f"Jogador 2:")
    print (f"O dado parou no 🎲 {dado} 🎲")
    print(f"🏠 Sua casa atual é {casajog2} 📍")
    casaatual = casajog2 + dado

    if casaatual > 20:
        casaatual = 20 - (casaatual - 20)

    print(pergunta[casaatual])
    respostaa = str(input("Resposta: "))
    if respostaa == resposta[casaatual]["Resposta"]:
        casajog2 = casaatual
        print("😁 Parabéns, você acertou ✅")
        print(f"🚀 Avançou para a casa {casajog2} 🏠✨")
    else:
        print("😭 Você errou ❌")
        print(f"📌 Você continua na mesma casa: {casajog2} 🏠")

    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    if casajog1 == 20 and casajog2 == 20:
        print(f"🤝 Empate! Ambos os jogadores voltarão à casa 15 para desempatar. 🏠↩️15")
        casajog1 = 15
        casajog2 = 15
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    if casajog1 == 20 or casajog2 == 20:
        break

if casajog1 == 20:
    print(f"🏆 Parabéns, Jogador 1! Você venceu o desafio do labirinto! 🎉")
else:
    print(f"🏆 Parabéns, Jogador 2! Você venceu o desafio do labirinto! 🎉")