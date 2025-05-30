"""
Universidad Carlemany, ejercicio 2, Semana 2. Laura Tomé Laguna.
Este es un ejercicio hecho en Python para dibujar una serie de barras según números introducidos por el usuario.
"""

import turtle

#Función para graficar números en un gráfico de barras.
# Toma una lista de números como argumento.
def graficar_numeros(numeros):
    
    # Configuración de la ventana de Turtle.
    turtle.setup(800, 600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-300, 250)
    turtle.pendown()
    turtle.hideturtle()
    turtle.color("black")

    # Definir el espacio entre barras y la altura total del gráfico.
    espacio = 5
    total_altura = 500  
    altura_barra = (total_altura / len(numeros)) - espacio


    for i, num in enumerate(numeros):
        
        longitud_barra = num * 5  
        
        y = 250 - i * (altura_barra + espacio)
        x_start = -300

        # Dibujar barra
        turtle.penup()
        turtle.goto(x_start, y)
        turtle.pendown()
        turtle.fillcolor("purple")
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(longitud_barra)
            turtle.right(90)
            turtle.forward(altura_barra)
            turtle.right(90)
        turtle.end_fill()

        # Escribir índice al lado izquierdo de la barra
        turtle.penup()
        turtle.goto(x_start - 30, y - altura_barra / 2 + 5)
        turtle.write(str(num), font=("Arial", 12, "normal"), align="right")


    print("\n¡Gráfico creado con éxito!")
    turtle.done()

# Función para pedir los valores al usuario y verificar la entrada.
def pedir_numeros():
    list_numbers = []
    while len(list_numbers) < 5:
        try:
            number= float(input("\nDime el número que deseas graficar: "))
            if number < 0:
                print("\nEl número debe ser positivo. Intenta de nuevo.")
                continue
            elif number != 0:
                list_numbers.append(number)
                print(f"\nNúmeros introducidos de momento: {list_numbers}")
                continue
            elif number == 0:
                break
        except ValueError:
            print("\nEntrada inválida. Intenta con un número natural.")

    print("\nProcediendo a graficar...")
    graficar_numeros(list_numbers)
    

def main():
    print("\n¡Bienvenido! Creemos un gráfico.")
    print("\nIntroduce números positivos para graficar con un máximo de 5.")
    print("\nCuando hayas terminado de introducir números usa el 0 como último número")
    
    pedir_numeros()
  

if __name__ == "__main__":
    main()