from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def actualizar(self, sujeto):
        pass

class CanalDeNoticias:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nuevas_noticias = ""
        self.suscriptores = []

    def agregar_suscriptor(self, suscriptor):
        self.suscriptores.append(suscriptor)

    def eliminar_suscriptor(self, suscriptor):
        self.suscriptores.remove(suscriptor)

    def notificar_suscriptores(self):
        for suscriptor in self.suscriptores:
            suscriptor.actualizar(self)

    def establecer_noticias(self, noticias):
        self.nuevas_noticias = noticias
        self.notificar_suscriptores()
        print(f"Actualización de noticias en {self.nombre}: {self.nuevas_noticias}")

class Suscriptor(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, sujeto):
        print(f"El suscriptor {self.nombre} recibió noticias de {sujeto.nombre}")
        print(f"Noticias: {sujeto.nuevas_noticias}")

cnn = CanalDeNoticias("CNN")
bbc = CanalDeNoticias("BBC")

suscriptor1 = Suscriptor("Alice")
suscriptor2 = Suscriptor("Bob")

cnn.agregar_suscriptor(suscriptor1)
bbc.agregar_suscriptor(suscriptor2)

cnn.establecer_noticias("Última hora: Nuevo descubrimiento en el espacio.")
bbc.establecer_noticias("Últimas noticias: Crisis política en el país.")
