# Refactor game

import random

def choose_options():

  # Creamos una tupla de opciones
  options = ("piedra", "papel", "tijera")

  # Solicitamos la opcion al usuario
  user_option = input("Piedra, Papel o Tijera => ")
  
  # Convertimos a minúscula el texto ingresado por el usuario
  user_option = user_option.lower()
   #print(user_option)
  
  if user_option not in options:
    print(f"La opcion {user_option} no es válida")
    #continue
    return None, None
  
  # Seleccionamos la opción de manera aleatoria
  computer_option = random.choice(options)
  print("computer => ", computer_option)

  # La funcion retorna multiples valores
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option and (user_option != None and computer_option != None):
    print("Empate!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print(f"{user_option} gana a {computer_option}. User ganó!")
      user_wins += 1
    else:
      print(f"{computer_option} gana a {user_option}. Computer ganó!")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "piedra":
      print(f"{user_option} gana a {computer_option}. User ganó!")
      user_wins += 1
    else:
      print(f"{computer_option} gana a {user_option}. Computer ganó!")
      computer_wins += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print(f"{user_option} gana a {computer_option}. User ganó!")
      user_wins += 1
    else:
      print(f"{computer_option} gana a {user_option}. Computer ganó!")
      computer_wins += 1
  
  return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
  if computer_wins == 2:
      print("El ganador es la computadora!")
      exit()
  if user_wins == 2:
      print("El ganador es el usuario!")
      exit()

def run_game():
  # Contadores de rondas ganadas
  computer_wins = 0
  user_wins = 0
  # Contador de rondas
  rounds = 1
  
  while True:

    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)
  
    print("computer_wins =>", computer_wins)
    print("user_wins =>", user_wins)

    # Incrementamos el contador de rondas
    rounds += 1
  
    # Almacenamos los valores retornados por la funcion
    user_option, computer_option = choose_options()
  
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    check_winner(user_wins, computer_wins)

run_game()
        