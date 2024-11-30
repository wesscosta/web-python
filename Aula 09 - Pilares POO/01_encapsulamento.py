class ContaBancaria:
    def __init__(self, saldo_inicial,nome):
        self.__saldo = saldo_inicial
        self.__titular = nome

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def __str__(self):
         return self.__titular

conta = ContaBancaria(1000, 'weslley')
print(conta.__titular)