from operator import attrgetter
from functools import total_ordering

nomes = ["Guilherme", "Daniela", "Paulo"]
print(nomes)
print(sorted(nomes))

@total_ordering
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
        if self._saldo != outro._saldo:        
            return self._saldo < outro._saldo
        self._codigo < outro._codigo

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
print(conta_do_guilherme < conta_da_daniela)
print(conta_do_guilherme <= conta_da_daniela)
print(conta_do_guilherme > conta_da_daniela)

print("----------")

for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)

print("----------")