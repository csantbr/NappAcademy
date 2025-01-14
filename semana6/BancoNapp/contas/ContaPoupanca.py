from BancoNapp.contas.Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, **kwargs):
        self.limite = kwargs.setdefault('limite', 0)
        super(ContaPoupanca, self).__init__(**kwargs)

    def rendimento_aniversario(self, juros):
        if juros < 0 or juros > 1:
            raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
        juros = self.saldo * juros
        self.saldo += juros
        return self.saldo

    def saque(self, valor):
        if isinstance(valor, (float, int)):
            if valor > self.saldo:
                raise ValueError('Valor do saque supera seu saldo.')
                return
            self.saldo -= valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')