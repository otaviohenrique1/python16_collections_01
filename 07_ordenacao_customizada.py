from operator import attrgetter

nomes = ["Guilherme", "Daniela", "Paulo"]
print(nomes)
print(sorted(nomes))


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        # igualdade (mesma coisa que ==)
        if type(outro) != ContaSalario:
            return False
        # return self._codigo == outro._codigo
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        # menor que (mesma coisa que <)
        return self._saldo < outro._saldo

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
print(conta_do_guilherme < conta_da_daniela)
print(conta_do_guilherme > conta_da_daniela)

print("----------")


def extrai_saldo(conta: ContaSalario):
    return conta._saldo


for conta in sorted(contas, key=extrai_saldo):
    print(conta)

print("----------")
for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

print("----------")
for conta in sorted(contas):
    print(conta)
    
print("----------")
for conta in sorted(contas, reverse=True):
    print(conta)

