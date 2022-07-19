class Libro:
    def __init__(self, titulo, autor, nPaginas, calificacion):
        self.titulo = titulo 
        self.autor = autor
        self.nPaginas = nPaginas 
        self.calificacion = calificacion

    def modificar_libro (self, titulo, autor, nPaginas, calificacion ):
        self.titulo = titulo 
        self.autor = autor
        self.nPaginas = nPaginas 
        self.calificacion = calificacion

    def __str__(self):
        return f'Título: {self.titulo} | Autor: {self.autor} | {self.nPaginas} | Calificaion: {self.calificacion}'


class ConjuntoLibros:
    def __init__(self) -> None:
        self.libros = []

    def agregar_libro(self, libro):
        if isinstance(libro, Libro) and libro not in self.libros:
            self.libros.append(libro)
    
    def eliminar_libro(self, titulo = '', autor = ''):
        for libro in self.libros:
            if libro.titulo == titulo or libro.autor == autor:
                self.libros.remove(libro)
                print('Libro eliminado')
                return
        print('El libro no existe')

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

    def mayor_y_menor_calificacion(self):
        mayor = self.libros[0].calificacion
        menor = self.libros[0].calificacion
        mayor_libro = self.libros[0]
        menor_libro = self.libros[0]
        for libro in self.libros:
            if libro.calificacion > mayor:
                mayor = libro.calificacion
                mayor_libro = libro
            if libro.calificacion < menor:
                menor = libro.calificacion
                menor_libro = libro
        print(f'Mayor calificación: {mayor_libro.titulo} ({mayor})')
        print(f'Menor calificación: {menor_libro.titulo} ({menor})')


libreria = ConjuntoLibros()

libreria.agregar_libro(Libro('El señor de los anillos', 'J.R.R. Tolkien', '352', '9'))
libreria.mostrar_libros()
print('********************************************************')
libreria.agregar_libro(Libro('Alicia en el país de las maravillas', 'Lewis Carroll', '128', '4'))
libreria.mostrar_libros()
print('********************************************************')
libreria.agregar_libro(Libro('Harry Potter y la piedra filosofal', 'J.K. Rowling', '320', '5'))
libreria.agregar_libro(Libro('Harry Potter y la piedra filosofal', 'J.K. Rowling', '320', '5'))
libreria.eliminar_libro('', 'J.K. Rowling')
libreria.eliminar_libro('Harry Potter y la piedra filosofal')
libreria.mostrar_libros()
print('********************************************************')
libreria.mayor_y_menor_calificacion()
print()
print(libreria)