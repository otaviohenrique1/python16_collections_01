class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)

conta1 = ContaCorrente(15)
conta1.deposita(500)
print(conta1)

conta2 = ContaCorrente(47685)
conta2.deposita(1000)
print(conta2)

# Lista => mutavel
contas = [conta1, conta2]
for conta in contas:
    print(conta)

# Tupla => imutavel
guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

def deposita(conta): # variação "funcional" (separando o comportamento dos dados) 
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

conta3 = deposita((18, 1000))
print(conta3)

contas2 = (conta1, conta2)
contas2[0].deposita(100)
for conta in contas2:
    print(conta)
