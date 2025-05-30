"""
Universidad Carlemany, ejercicio 1, Semana 2. Laura Tomé Laguna.
Este es un ejercicio hecho en python para dibujar una estrella de n puntas.
"""

import turtle

# Función para dibujar una estrella con un número de puntas y grosor de trazo especificados.
# Toma dos argumentos: puntas (número de puntas de la estrella) y trazo (grosor del trazo).
def dibujar_estrella(puntas, trazo):
    turtle.showturtle()
    turtle.title(f"Estrella de {puntas} Puntas")
    turtle.pensize(trazo)

    extent = 360 / puntas

    # Dividimos entre estrellas con número par e impar de puntas.
    if puntas % 2 == 0:
        coords = []
        for a in range(0, puntas):
            turtle.penup()
            coords.append(turtle.pos())
            turtle.circle(puntas * 20, extent)
        for b in range(0, len(coords)):
            if b % 2 == 0:
                turtle.pendown()
                turtle.goto(coords[b][0], coords[b][1])
            else:
                continue
        turtle.goto(coords[0][0], coords[0][1])
        turtle.penup()
        for c in range(0, (len(coords) + 1)):
            if c % 2 != 0:
                turtle.goto(coords[c][0], coords[c][1])
                turtle.pendown()
            else:
                continue
        turtle.goto(coords[1][0], coords[1][1])
    else:
        angle = 180 - (180 / puntas)
        for a in range(puntas):
            turtle.forward(400)
            turtle.right(angle)
    turtle.end_fill()

    print(f"\n¡Estrella de {puntas} puntas dibujada con éxito!")
    turtle.done()        

# Función para pedir y verificar la entrada del usuario.
# Toma tres argumentos: mensaje, valor mínimo y valor máximo de la entrada.
def pedir_entero(msg, minimo, maximo):
    while True:
        try:
            valor = int(input(msg))
            if minimo <= valor <= maximo:
                return valor
            print(f"Debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Entrada inválida. Intenta con un número entero.")

def main():
    print("\n¡Bienvenido! Vamos a dibujar una estrella.")
    puntas = pedir_entero("Elige un número de puntas (5 a 12): ", 5, 12)
    trazo = pedir_entero("Elige el grosor del trazo (10 a 50): ", 10, 50)
    dibujar_estrella(puntas, trazo)

if __name__ == "__main__":
    main()
