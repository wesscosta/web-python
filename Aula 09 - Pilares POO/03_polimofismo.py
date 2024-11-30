###### POLIMOFISMO ######

class Animal:
    def comer():
        print('O animal está comendo!')

    def falar():
        return ('O animal está falando!')


class Cachorro(Animal):
    def falar():
        return ('Au Au')

class Gato(Animal):
    def falar():
        return ('Miau')

class Peixe(Animal):
    def andar():
        return('O peixe está nadando!')
    
    def falar():
        return('blu blu')

# felix = Gato
# toto = Cachorro
# nemo = Peixe

# print(felix.falar())
# print(toto.falar())
# print(nemo.falar())

animais = [Gato, Cachorro, Peixe]
for animal in animais:
    print(animal.falar())