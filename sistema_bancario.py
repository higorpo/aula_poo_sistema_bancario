from banco import Banco
from caixa_eletronico import CaixaEletronico

bc = Banco("Banco do Brejo", 999)

nj = bc.abre_conta("Joãozinho", 987234)
nm = bc.abre_conta("Mariazinha", 135793)

bc.deposito(nm, 150.00)
bc.deposito(nj, 80.00)
bc.transferencia(nm, nj, 40.00)
bc.saque(nm, 70.00)
bc.saque(nj, 10.00)

caixa = CaixaEletronico(bc)

caixa.adicionar_cedulas(2, 13)
caixa.adicionar_cedulas(5, 2)
caixa.adicionar_cedulas(10, 1)
caixa.adicionar_cedulas(50, 6)
caixa.adicionar_cedulas(100, 2)

caixa.saque(nm, 6)

print(bc.saldo(nm))
print(bc.saldo(nj))