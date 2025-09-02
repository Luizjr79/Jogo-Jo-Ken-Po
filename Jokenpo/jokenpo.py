import random # Importa o módulo random para gerar escolhas aleatórias do computador

jogada = input("Escolha entre PEDRA, PAPEL ou TESOURA: ").upper()
# Solicita a escolha do usuário e converte para maiúsculas para padronizar

print(f"Você escolheu {jogada}")
# Mostra a escolha do usuário

lista_jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
# Lista com as opções possíveis de jogadas

jogada_bot = random.choice(lista_jogadas)
# Seleciona aleatoriamente a jogada do computador

print(f"O computador escolhe {jogada_bot}")
# Mostra a escolha do computador

if jogada == jogada_bot:
    print('EMPATE!')
# Verifica se houve empate

elif (jogada == 'PEDRA' and jogada_bot == 'TESOURA') or \
     (jogada == 'TESOURA' and jogada_bot == 'PAPEL') or \
     (jogada == 'PAPEL' and jogada_bot == 'PEDRA'):
    print("Você VENCEU!!!")
# Condições em que o usuário vence

else:
    print("Você PERDEU :/")
# Se não for empate nem vitória, o usuário perde