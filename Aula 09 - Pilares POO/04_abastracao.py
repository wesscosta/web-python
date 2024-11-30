from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def desenhar(self):
        pass

class Circulo(Forma):
    def desenhar(self):
        print("Desenhando um círculo.")

forma = Forma()
forma.desenhar()
