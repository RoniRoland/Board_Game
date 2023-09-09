import subprocess
from os import startfile
from lista import ListaEnlazada


def display_menu():
    print("\n===================================================================")
    print("Practica 1 - Introduccion a la Programacion y Computacion 2")
    print("===================================================================")
    print("\n -*-*-*-*-*-*-* # Colorealo: *-*-*-*-*-*-*-*-* \n")
    print("1.- Crear Tablero")
    print("2.- Mostrar datos del estudiante")
    print("0.- Salir")
    print("\n.........................Guatematel.................................\n")


def input_option_range(min_value, max_value, message):
    while True:
        option = input(message)
        try:
            option = int(option)
            if min_value <= option <= max_value:
                return option
            else:
                print(
                    f"Opción incorrecta. Debe ser un número del rango {min_value} a {max_value}"
                )
        except ValueError:
            print("Opción incorrecta. Debe ser un número.")


def datos_estudiante():
    print("\n..................................................................")
    print("Edgar Rolando Ramirez Lopez")
    print("201212891")
    print("Introduccion a la Programacion y Computacion 2")
    print("Ingenieria en Ciencias y Sistemas")
    print("4to Semestre")
    print("...................................................................\n")


def color_to_code(color):
    color = color.lower()
    if color == "azul":
        return "A"
    elif color == "rojo":
        return "R"
    elif color == "verde":
        return "V"
    elif color == "purpura":
        return "P"
    elif color == "naranja":
        return "N"
    else:
        return None


def generateGraphvizCode(matriz, alto, file_name="lista"):
    # archivo de entrada DOT
    fullNameTxt = file_name + ".dot"

    # imagen de salida
    fullNameImg = file_name + ".jpg"

    try:
        # Generando código de graphviz en un archivo txt
        f = open(fullNameTxt, "w")
        f.write("digraph G {\n")
        f.write("rankdir=TB;\n")
        f.write('nodeRoot [shape=circle, label=" Colorealo \nGuatematel  "]\n')

        for i in range(alto):
            salida = matriz.get_by_index(
                i
            ).obtenerNodos()  # Generando nodos de la lista
            f.write(salida[0])
            f.write("nodeRoot -> node" + str(salida[1]) + "\n")

        f.write("}")
        f.close()

        # Ejecutando comando para crear la imagen
        command = ["dot", "-Tjpg", fullNameTxt, "-o", fullNameImg]
        subprocess.call(command)

        # Abriendo la imagen
        startfile(fullNameImg)
    except:
        print("Error: .")
        f.close()


def create_tablero():
    print("\n===============CREACION DE TABLERO====================\n")
    ancho = int(input("Ancho del tablero: "))
    alto = int(input("Alto del tablero: "))

    matriz = ListaEnlazada()

    for i in range(alto):
        fila = ListaEnlazada()
        for j in range(ancho):
            fila.add_node(" ")
        matriz.add_node(fila)

    print("\nTablero creado correctamente\n")
    matriz.display()

    while True:
        print("\n =======OPCIONES DE JUEGO========\n")
        print("1.- Ingreso de Colores")
        print("2.- Generar Grafica de tablero")
        print("3.- Regresar menu principal")
        opcion2 = input("\nIngrese una opción: ")

        if opcion2 == "1":
            color = input(
                "\nColores disponibles: \n-AZUL \n-ROJO \n-VERDE \n-PURPURA \n-NARANJA\n \nElegir Color: "
            ).lower()
            color_code = color_to_code(color)

            if color_code is not None:
                try:
                    print("\n")
                    print("Ingrese coordenadas donde desea colocar la ficha")
                    fila = int(input("Ingrese Fila: "))
                    columna = int(input("Ingrese Columna: "))

                    if 1 <= fila <= alto and 1 <= columna <= ancho:
                        matriz.get_by_index(fila - 1).modify_by_index(
                            columna - 1, color_code
                        )
                        print("\n")
                        matriz.display()
                    else:
                        print("La fila o columna no existe en el tablero")
                except ValueError:
                    print("Debe ingresar un número en fila y columna")
            else:
                print("Color no válido.")

        elif opcion2 == "2":
            matriz_invertida = ListaEnlazada()
            for x in range(ancho):
                fila = ListaEnlazada()
                for y in range(alto):
                    fila.add_node(matriz.get_by_index(y).get_by_index(x))
                matriz_invertida.add_node(fila)
            generateGraphvizCode(matriz_invertida, ancho)

        elif opcion2 == "3":
            break


def main():
    while True:
        display_menu()
        option = input_option_range(0, 2, "Ingrese una opción: ")

        if option == 1:
            create_tablero()
        elif option == 2:
            datos_estudiante()
        elif option == 0:
            print("\nSaliendo del Programa\n")
            break
        else:
            print("Opción incorrecta")


if __name__ == "__main__":
    main()
