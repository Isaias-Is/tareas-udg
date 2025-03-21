from random import randint
class Bici:
    _id = 0
    def __init__(self, horasUso = 0, metrosRecorridos = 0, id = None):
        if id is not None:
            self._id = id
        else:
            Bici._id += 1
            self._id = Bici._id
        self.horasUso = horasUso
        self.metrosRecorridos = metrosRecorridos

    def __repr__(self):
        return f"{self._id},{self.horasUso},{self.metrosRecorridos}"

    def to_dict(self):
        return {
            "id": self._id,
            "horasUso": self.horasUso,
            "metrosRecorridos": self.metrosRecorridos
        }
    
def generarBiciAleatoria():
    return Bici(randint(0, 100), randint(0, 10000))
