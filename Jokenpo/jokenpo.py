"""
Jogo de Jokenpô (Pedra, Papel e Tesoura)
O usuário joga contra o computador, que faz uma escolha aleatória.
"""

import random # Importa o módulo random para gerar escolhas aleatórias do computador
import time # Importa o módulo time para criar um pequeno delay e dar mais dinamismo ao jogo

placar = {"vitorias": 0, "derrotas": 0, "empates": 0}

lista_jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
# Lista com as opções possíveis de jogadas

while True:

  jogada = input("Escolha entre PEDRA, PAPEL ou TESOURA: ").upper()
# Solicita a escolha do usuário e converte para maiúsculas para padronizar

  while jogada not in lista_jogadas:
      jogada = input("Jogada inválida! Escolha entre PEDRA, PAPEL ou TESOURA: ").upper()
    # Mantém pedindo até que seja digitada uma jogada válida

  print("JO")
  time.sleep(0.5) # Pausa de meio segundo
  print("KEN")
  time.sleep(0.5)
  print("PÔ!")
  time.sleep(0.7)

  print(f"Você escolheu {jogada}")
# Mostra a escolha do usuário

  jogada_bot = random.choice(lista_jogadas)
# Seleciona aleatoriamente a jogada do computador

  print(f"O computador escolhe {jogada_bot}")
# Mostra a escolha do computador

  if jogada == jogada_bot:
      print('EMPATE!')
      placar["empates"] += 1 # Adiciona + 1 ao placar
  # Verifica se houve empate

  elif (jogada == 'PEDRA' and jogada_bot == 'TESOURA') or \
       (jogada == 'TESOURA' and jogada_bot == 'PAPEL') or \
       (jogada == 'PAPEL' and jogada_bot == 'PEDRA'):
      print("Você VENCEU!!!")
      placar["vitorias"] += 1 
  # Condições em que o usuário vence

  else:
      print("Você PERDEU :/")
      placar["derrotas"] += 1
  # Se não for empate nem vitória, o usuário perde


# Jogo irá rodar novamente, caso o jogador deseje

  resposta = input("Deseja jogar novamente? (S/N): ").upper()
  if resposta == "N": 
     print("===== PLACAR FINAL =====")
     time.sleep(0.2)
     print(f"Vitórias: {placar['vitorias']}")
     time.sleep(0.2)
     print(f"Derrotas: {placar['derrotas']}")
     time.sleep(0.2)
     print(f"Empates: {placar['empates']}")
     print("Obrigado por jogar. Até mais!")
     break
