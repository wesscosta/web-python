class Animal:
    def comer():
        print('O animal está comendo!')

class Terrestre():
    def andar():
        print('Se locomove na terra!')
        
    def comer():
        print('Come qualquer coisa!')
        
        
class Cachorro(Animal, Terrestre):
    def latir():
        print('O cachorro está latindo!')
        
    def comer():
        print('o Toto come alimentos da Terra!')
        
        
toto  = Cachorro
toto.latir() 
toto.comer() 
toto.andar()