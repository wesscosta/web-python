#Listas  e Dicionarios

# LISTAS ou Arrays
numeros = [1,2,3,4,5,6]
aleatorios = ['arroz', 'feijão','frutas','carro','animais']

#Inserir elementos
numeros.append(7)
numeros.insert(2,7)
numeros.insert(0,8)
numeros.insert(-1,3)


#Remover Elementos
numeros.pop(1) # remove pelo indece
numeros.remove(7) # remover o primeiro elemento que bate com o valor informado

# numeros.sort()
# numeros.reverse()



# print(numeros[0]) # Primeiro elemento
# print(numeros[-1]) # Último elemento
# print(numeros)

# # Deseja remover algum elemento da lista? (s/n)
# valid = input('digite um valor').lower() 
# # 
# print(valid)

pessoa1 = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}
pessoa2 = {'nome': 'Carlo', 'idade': 18, 'cidade': 'Timon'}
pessoa3 = {'nome': 'Ana', 'idade': 22, 'cidade': 'Teresina'}

# pessoas = [pessoa1,pessoa2,pessoa3]
# print(pessoa1)

# print(pessoa1.keys())
# print(pessoa1.values())
print(pessoa1.items())

for chaves, valor in pessoa1.items():
    print(chaves,'-' ,valor)
