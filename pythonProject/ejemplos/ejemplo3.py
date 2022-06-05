class Persona:
    def __init__(self,edad):
        self.edad = edad

    def hablar(self, mensaje):
        print (self.edad)
        print (mensaje)

juan = Persona(34)
mario = Persona(22)

print ('Soy Juan y tengo ', juan.edad)
print ('Soy Mario y tengo ', mario.edad)

