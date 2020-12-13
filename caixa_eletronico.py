from ficha_bancaria import FichaBancaria

class CaixaEletronico:
    
    def __init__(self, banco):
        self.__banco = banco
        self.__cedulas = {
            2: 0,
            5: 0,
            10: 0,
            20: 0,
            50: 0,
            100: 0
        }
        
    def saque(self, numero_conta, valor):
        ''' Realiza um saque numa conta '''
        if self.__banco.saldo(numero_conta) >= valor:
            # Verifica se existe as cedulas necessárias para debitar
            valor_saque = valor

            qtd_notas_100 = int(valor / 100)
            valor -= qtd_notas_100 * 100
            
            qtd_notas_50 = int(valor / 50)
            valor -= qtd_notas_50 * 50
            
            qtd_notas_20 = int(valor / 20)
            valor -= qtd_notas_20 * 20

            qtd_notas_10 = int(valor / 10)
            valor -= qtd_notas_10 * 10

            qtd_notas_5 = int(valor / 5)
            valor -= qtd_notas_5 * 5

            qtd_notas_2 = int(valor / 2)
            valor -= qtd_notas_2 * 2

            if self.tem_quantidade_cedulas(100, qtd_notas_100) and self.tem_quantidade_cedulas(50, qtd_notas_50) and self.tem_quantidade_cedulas(20, qtd_notas_20) and self.tem_quantidade_cedulas(10, qtd_notas_10) and self.tem_quantidade_cedulas(5, qtd_notas_5) and self.tem_quantidade_cedulas(2, qtd_notas_2):
                self.remove_cedulas(100, qtd_notas_100)
                self.remove_cedulas(50, qtd_notas_50)
                self.remove_cedulas(20, qtd_notas_20)
                self.remove_cedulas(10, qtd_notas_10)
                self.remove_cedulas(5, qtd_notas_5)
                self.remove_cedulas(2, qtd_notas_2)

                self.__banco.saque(numero_conta, valor_saque)
                return True
            else:
                return False
        else: 
            return False

    def deposito(self, numero_conta, valor):
        ''' Realiza um depósito numa conta '''
        return self.__banco.deposito(numero_conta, valor)

    def transferencia(self, nct_origem, nct_destino, valor):
        ''' Realiza transferência entre duas contas '''
        return self.__banco.transferencia(nct_origem, nct_destino, valor)
    
    def saldo(self, numero_conta):
        ''' Obtém o saldo de uma conta '''
        return self.__banco.saldo(numero_conta)

    def adicionar_cedulas(self, tipo_cedula, quantidade):
        self.__cedulas[tipo_cedula] += quantidade

    def remove_cedulas(self, tipo_cedula, quantidade):
        if self.__cedulas[tipo_cedula] >= quantidade:
            self.__cedulas[tipo_cedula] -= quantidade
            return True
        else:
            return False
    
    def tem_quantidade_cedulas(self, tipo_cedula, quantidade):
        return self.__cedulas[tipo_cedula] >= quantidade