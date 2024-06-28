idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

print(list(range(len(idades))))
print(list(enumerate(idades)))

for indice, idade in enumerate(idades):
    print(indice, "x", idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979),
]

for nome, idade, nascimento in usuarios:
    print(nome)
