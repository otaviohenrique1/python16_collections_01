class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        # return self._codigo == outro._codigo
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


conta1 = ContaSalario(37)
print(conta1)

conta3 = ContaSalario(37)
conta4 = ContaSalario(37)
print(conta3 == conta4)

print(isinstance(ContaSalario(34), ContaSalario))
