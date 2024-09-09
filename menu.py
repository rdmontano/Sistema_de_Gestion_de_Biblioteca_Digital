import os
from biblioteca import Libro, Usuario, Biblioteca


def limpiar_pantalla():
    #Limpia la pantalla según el sistema operativo
    sistema = os.name
    if sistema == 'posix':  # Unix, Linux, MacOS
        os.system('clear')
    elif sistema == 'nt':  # Windows
        os.system('cls')


def menu():
    biblioteca = Biblioteca()

    while True:
        limpiar_pantalla()
        print("\n--- MENU DE GESTION DE BIBLIOTECA ---\n")
        print("1. AÑADIR LIBRO")
        print("2. QUITAR LIBRO")
        print("3. REGISTRAR USUARIO")
        print("4. DAR DE BAJA A USUARIO")
        print("5. PRESTAR LIBRO")
        print("6. DEVOLVER LIBRO")
        print("7. BUSCAR LIBRO")
        print("8. LISTAR LIBROS PRESTADOS")
        print("9. SALIR")
        print("--------------------------------------\n")

        opcion = input("SELECCIONA UNA OPCION: ")

        if opcion == "1":
            titulo = input("TITULO: ")
            autor = input("AUTOR: ")
            categoria = input("CATEGORIA: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)
        elif opcion == "2":
            isbn = input("ISBN DEL LIBRO A QUITAR: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == "3":
            nombre = input("NOMBRE DE USUARIO: ")
            id_usuario = input("ID DE USUARIO: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)
        elif opcion == "4":
            id_usuario = input("ID DE USUARIO A DAR DE BAJA: ")
            biblioteca.dar_baja_usuario(id_usuario)
        elif opcion == "5":
            id_usuario = input("ID DE USUARIO: ")
            isbn = input("ISBN DEL LIBRO A PRESTAR: ")
            usuario = Usuario("", id_usuario)  # En una implementación completa, deberías obtener el usuario real
            biblioteca.prestar_libro(isbn, usuario)
        elif opcion == "6":
            id_usuario = input("ID DE USUARIO: ")
            isbn = input("ISBN DEL LIBRO A DEVOLVER: ")
            usuario = Usuario("", id_usuario)  # En una implementación completa, deberías obtener el usuario real
            biblioteca.devolver_libro(isbn, usuario)
        elif opcion == "7":
            criterio = input("BUSCAR POR (titulo/autor/categoria): ")
            valor = input(f"INTRODUCE EL {criterio}: ")
            biblioteca.buscar_libro(criterio, valor)
        elif opcion == "8":
            id_usuario = input("ID DE USUARIO: ")
            usuario = Usuario("", id_usuario)  # En una implementación completa, deberías obtener el usuario real
            biblioteca.listar_libros_prestados(usuario)
        elif opcion == "9":
            print("SALIENDO...")
            biblioteca.guardar_datos()
            break
        else:
            print("OPCION NO VALIDA, INTENTA DE NUEVO.")

        input("PRESIONA ENTER PARA CONTINUAR...")


if __name__ == "__main__":
    menu()
