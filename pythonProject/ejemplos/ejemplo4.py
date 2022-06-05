class Personall:
    pass


class Personall:
    pass

    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año

    def descripcion(self):
        return ' {} tiene {} años'.format(self.nombre, self.año)

    def comentario(self, frase):
        return '{} dice : {}'.format(self.nombre, frase)

    enjermera = Personall('Maria', 22)
    print(enjermera.descripcion())
    print(enjermera.comentario(' Hola como esta'))
