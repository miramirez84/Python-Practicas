''' Piedra, Papel o Tijera vs CPU
    ***Lógica del resultado de restar player - cpu, según las opciones 1(Piedra), 2(Papel) y 3(Tijera)***
    
    Lógica para Jugador Gana 
    (fórmula player-cpu):
    piedra-tijera ( 1 - 3 = -2 )
    papel-piedra  ( 2 - 1 =  1 ) 
    tijera-papel  ( 3 - 2 =  1 ) > resultados (-2, 1)
    
    Lógica para CPU Gana 
    (fórmula player-cpu):
    piedra-papel  ( 1 - 2 = -1 )
    papel-tijera  ( 2 - 3 = -1 )
    tijera-piedra ( 3 - 1 =  2 ) > resultado (-1, 2)
    
    Resumen:
    player-cpu -> (-2, 1) resultado jugador gana
    player-cpu -> (-1, 2) resultado cpu gana
'''
import random

def playCPU() -> int: #retorna la jugada realizada por la CPU
    rand = random.randint(1,3)
    return rand 



def resultado(player:int, cpu:int) -> int: #player y cpu son parametros que reciben la opción el jugador y el generado para la cpu
    resultado = 0 #empate, se asume que el resultado inicial es empate
    juego = {"1": "Piedra", "2": "Papel", "3": "Tijera"}
    texto = "Usted jugó {} y la CPU {}".format( juego[ str(player) ], juego[ str(cpu) ]) 
    print(">"*len(texto)+"\n"+texto)
    
    if player != cpu:
        resultado = -1 #Se asume que CPU gana si las jugadas son distintas
        if player - cpu in (-2, 1) : #se comprueba la formula, y se altera el resultado según el mismo.
            resultado = 1 #Jugador Gana, en atención a los posibles resultados según la lógica definida para player-cpu
    
    return resultado



jugador ={"1": "Jugador", "-1": "CPU"}
marcador = { "1": 0, "-1": 0, "0": 0} #keys en función del jugador, el key "0" respresenta empate
opcion = "0" #se usa el string para no tener que validar la conversión INT del input con valores no numéricos
titulo = "Juego del Piedra, Papel o Tijera vs CPU"

print("\n"+"#"*len(titulo) + "\n" + titulo + "\n"+ "#"*len(titulo))

while opcion != "4":
    print("Opciones: \n1- Piedra \n2- Papel \n3- Tijera \n4- Salir")
    opcion = input("Elige la opción que quieres jugar: ")
    
    if opcion in ["1","2","3"]:
        cpu = playCPU()
        player = int(opcion) 
        
        result = resultado(player,cpu)
        marcador[str(result)] += 1
        texto = "Empate"
        
        if result != 0:
            texto = "{} gana".format(jugador[str(result)]) #Jugado o CPU gana
        
        print("-"*len(titulo)+"\n"+texto+"\n"+"-"*len(titulo)+"\n")
        
    
texto ="Fin del juego, resultado del juego: Jugador {} vs CPU {}; Empates: {}".format(marcador["1"],marcador["-1"],marcador["0"])
print("*"*len(texto)+"\n"+texto+"\n"+"*"*len(texto))
