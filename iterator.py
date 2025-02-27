from collections.abc import Iterator, Iterable

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} de {self.autor}"
    

class LibroIterator(Iterator):
    def __init__(self, libros):
        self.libros = libros
        self.index = 0

    def __next__(self):
        if self.index < len(self.libros):
            libro = self.libros[self.index]
            self.index += 1
            return libro
        else:
            raise StopIteration
    

class Biblioteca(Iterable):
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def __iter__(self):
        return LibroIterator(self.libros)

biblioteca = Biblioteca()

biblioteca.agregar_libro(Libro("El señor de los anillos", "JRR Tolkien"))
biblioteca.agregar_libro(Libro("El HOBBIT", "JRR Tolkien"))
biblioteca.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez"))

for libro in biblioteca:
    print(libro)
