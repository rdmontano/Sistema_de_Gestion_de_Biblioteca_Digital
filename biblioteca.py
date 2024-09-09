import os


# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"TITULO: {self.titulo_autor[0]}, AUTOR: {self.titulo_autor[1]}, CATEGORIA: {self.categoria}, ISBN: {self.isbn}"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"USUARIO: {self.nombre}, ID: {self.id_usuario}, LIBROS PRESTADOS: {[libro.titulo_autor[0] for libro in self.libros_prestados]}"


# Clase Biblioteca con manipulación de archivos
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = {}  # Diccionario para almacenar usuarios con ID como clave
        self.historial_prestamos = []  # Historial de préstamos
        self.cargar_datos()

    def cargar_datos(self):
        #Carga los datos de los archivos al iniciar el programa
        if os.path.exists('libros.txt'):
            with open('libros.txt', 'r') as file:
                for linea in file:
                    titulo, autor, categoria, isbn = linea.strip().split(';')
                    self.libros_disponibles[isbn] = Libro(titulo, autor, categoria, isbn)

        if os.path.exists('usuarios.txt'):
            with open('usuarios.txt', 'r') as file:
                for linea in file:
                    nombre, id_usuario = linea.strip().split(';')
                    usuario = Usuario(nombre, id_usuario)
                    self.usuarios_registrados[id_usuario] = usuario

        if os.path.exists('historial_prestamos.txt'):
            with open('historial_prestamos.txt', 'r') as file:
                self.historial_prestamos = [tuple(linea.strip().split(';')) for linea in file]

    def guardar_datos(self):
        #Guarda los datos de los libros, usuarios y préstamos en archivos de texto
        with open('libros.txt', 'w') as file:
            for libro in self.libros_disponibles.values():
                file.write(f"{libro.titulo_autor[0]};{libro.titulo_autor[1]};{libro.categoria};{libro.isbn}\n")

        with open('usuarios.txt', 'w') as file:
            for usuario in self.usuarios_registrados.values():
                file.write(f"{usuario.nombre};{usuario.id_usuario}\n")

        with open('historial_prestamos.txt', 'w') as file:
            for prestamo in self.historial_prestamos:
                file.write(f"{prestamo[0]};{prestamo[1]}\n")

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            self.guardar_datos()
            print(f"LIBRO '{libro.titulo_autor[0]}' AGREGADO A LA BIBLIOTECA.")
        else:
            print(f"EL LIBRO CON ISBN {libro.isbn} YA EXISTE.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            self.guardar_datos()
            print(f"LIBRO CON ISBN {isbn} ELIMINADO DE LA BIBLIOTECA.")
        else:
            print(f"NO SE ENCONTRO UN LIBRO CON ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.guardar_datos()
            print(f"USUARIO '{usuario.nombre}' REGISTRADO.")
        else:
            print(f"EL ID DE USUARIO {usuario.id_usuario} YA ESTA REGISTRADO.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[id_usuario]
            self.guardar_datos()
            print(f"USUARIO CON ID {id_usuario} DADO DE BAJA.")
        else:
            print(f"NO SE ENCONTRO UN USUARIO CON ID {id_usuario}.")

    def prestar_libro(self, isbn, usuario):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles[isbn]
            usuario.prestar_libro(libro)
            self.historial_prestamos.append((usuario.id_usuario, libro.isbn))
            del self.libros_disponibles[isbn]
            self.guardar_datos()
            print(f"LIBRO '{libro.titulo_autor[0]}' PRESTADO A {usuario.nombre}.")
        else:
            print(f"EL LIBRO CON ISBN {isbn} NO ESTA DISPONIBLE.")

    def devolver_libro(self, isbn, usuario):
        libro = usuario.devolver_libro(isbn)
        if libro:
            self.libros_disponibles[isbn] = libro
            self.guardar_datos()
            print(f"LIBRO '{libro.titulo_autor[0]}' DEVUELTO POR {usuario.nombre}.")
        else:
            print(f"EL USUARIO NO TIENE PRESTADO UN LIBRO CON ISBN {isbn}.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "TITULO" and valor.lower() in libro.titulo_autor[0].lower():
                resultados.append(libro)
            elif criterio == "AUTOR" and valor.lower() in libro.titulo_autor[1].lower():
                resultados.append(libro)
            elif criterio == "CATEGORIA" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print(f"NO SE ENCONTRARON LIBROS QUE COINDIDAN CON {criterio}: {valor}.")

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print(f"EL USUARIO '{usuario.nombre}' NO TIENE LIBROS PRESTADOS.")
