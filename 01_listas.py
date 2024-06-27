idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [39, 30, 27, 18]
print(type(idades))
print(idades)
print(len(idades))
print(idades[0])

idades.append(15)
print(idades)

if 27 in idades:
    idades.remove(27)

print(idades)
idades.insert(0, 20)
print(idades)

for elemento in idades:
    print(elemento)

idades.extend([27, 19])
print(idades)

idades2 = [(idade + 1) for idade in idades]
print(idades2)

idades3 = [(idade) for idade in idades if idade > 21]
print(idades3)


def proximo_ano(idade):
    return idade + 1


# list comprehension
idades4 = [proximo_ano(idade) for idade in idades if idade > 21]
print(idades4)


def faz_processamento_de_visualizacao(lista=None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)


faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
