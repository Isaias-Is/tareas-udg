from typing import List
from bici import Bici

class Bicipuerto:
    def __init__(self):
        self.bicis : List[Bici] = []

    def agregar_bici(self, bici: Bici):
        self.bicis.append(bici)