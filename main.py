import random
from replit import clear
from art import logo

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

numero_escolhido = random.choice(numero)
dificuldade = ""
chances = 0
chute = 0


def jogar():
  print(logo)
  dificuldade = input ("Qual a dificuldade que você quer? Digite Para Difícil = d ou para Fácil = f: ")
  if dificuldade == "d":
    chances = 5
  else:
    chances = 10
  print (f"Voce vai ter {chances} chances para acertar. Boa sorte")
  acertou = False

  while not acertou:
    while chances > 0:
      chute = int(input("Chute um número de 1 a 100 : "))
      if chute == numero_escolhido:
        print("Acertou mizeravi")
        acertou = True
        chances = -1
      elif chute > numero_escolhido and chances > 0:
        print("Número muito alto, tente denovo")
        chances -= 1
        print(f"Voce tem {chances} chances!")
      elif chute < numero_escolhido and chances > 0:
        print("Número muito baixo, tente denovo")
        chances -= 1
        print(f"Voce tem {chances} chances!")
      if chances == 0:
        acertou = True
        print (f"Errrrrrou. O número era {numero_escolhido}")

while input ("Quer tentar adivinhar o número que eu estou pensando? Digite s ou n: ") == "s":
  clear()
  jogar()
  
  


