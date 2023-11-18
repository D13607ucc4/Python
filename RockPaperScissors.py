
# Tendria que utilizar numeros al azar entre 1 y 3 y utilizar diccionarios dandole valores a la Piedra, Tijera y Papel

import random

Objects = {
    1 : "rock",
    2 : "paper",
    3 : "scissors"
}

Selections = ["rock", "paper", "scissors"]

Entry1 = input("Choose one of Rock, Paper or Scissors: ")
Entry = Entry1.lower()
contadorWin = 0
contadorLose = 0
win = False

#while not Entry in Selections:
#    print("Error! Por favor elige entre piedra, papel o tijera")
#    Entry = input("Elija entre Piedra, Papel o Tijera: ")


while not win:
    number = random.randint(1, 3)
    if (Objects[number] == Entry):
        print ("Empate")
    elif (Objects[number] == "rock" and Entry == "paper"):
        print ("Ganaste!")
        contadorWin += 1
    elif Objects[number] == "rock" and Entry == "scissors":
        print ("Perdiste!")
        contadorLose += 1
    elif Objects[number] == "paper" and Entry == "rock":
        print ("Perdiste!")
        contadorLose += 1
    elif Objects[number] == "paper" and Entry == "scissors":
        print ("Ganaste!")
        contadorWin += 1
    elif Objects[number] == "scissors" and Entry == "rock":
        print ("Ganaste!")
        contadorWin += 1
    elif Objects[number] == "scissors" and Entry == "paper":
        print ("Perdiste!")
        contadorLose += 1

    if (contadorWin + contadorLose == 5) or (contadorWin == 3) or (contadorLose == 3):
        win = True
    else:
        Entry1 = input("Choose one of Rock, Paper or Scissors: ")
        Entry = Entry1.lower()

if (contadorWin > contadorLose):
    print ("Ganaste ", contadorWin, " a ", contadorLose)
else:
    print ("Perdiste ", contadorLose, " a ", contadorWin)