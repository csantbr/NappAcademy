class Conta:
    def __init__(self, **kwargs):
        self.extrato = []
        self.limite = kwargs.get('limite', 500)
        self.nome = kwargs.get('nome', None)
        self.empresa = kwargs.get('empresa', '')
        self.profissao = kwargs.get('profissao', '')
        saldo = kwargs.get('saldo', 0)
        if saldo < 0:
            raise ValueError('Saldo negativo')
        self.saldo = saldo
        self.extrato.append(('I', saldo))

    def saque(self, valor):
        if isinstance(valor, (float, int)):
            if valor > (self.saldo + self.limite):
                raise ValueError('Valor do saque supera seu saldo e seu limite')
                return
            self.saldo -= valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')

    def deposito(self, valor):
        if isinstance(valor, (float, int)):
            if valor <= 0:
                raise ValueError('Valor do depósito precisa ser maior que zero')
            self.saldo += valor
            self.extrato.append(('D', valor))
            return
        raise TypeError('O depósito precisa ser numérico')

    def get_extrato(self):
        return self.extrato