class Conta:

    num_contas = 1  # atributo de classe

    def __init__(self, numero, saldo, limite):
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.saldo_disponivel = saldo + limite
        # incrementa o atributo de class sempre que um objeto for criado
        Conta.num_contas += 1

    # definindo um metodo de classe
    @classmethod
    def gera_novo_numero(cls):
        novo_numero = cls.num_contas
        return novo_numero

    def creditar(self,valor):
        self.saldo += valor

    def debitar(self, valor):
        self.saldo -= valor

    def get_numero(self):
        return self.numero

    def get_saldo(self):
        return self.saldo

    def get_limite(self):
        return self.limite

    def set_limite(self, limite):
        if limite < 0:
            print('O limite nao pode ser negativo!')
        else:
            self.limite = limite


class Poupanca:

    _num_contas = 1

    def __init__(self, saldo, taxa_juros):
        self_numero = Poupanca.gera_novo_numero()
        self_saldo = saldo
        self_taxa_juros = taxa_juros
        Poupanca._num_contas += 1

    @classmethod
    def gera_novo_numero(cls):
        novo_numero = cls._num_contas * 1234
        return novo_numero

    @classmethod
    def get_num_contas(cls):
        return cls._num_contas * 1234

    # novo metodo
    def render_juros(self):
        self.creditar(self.saldo * self.taxa_juros )

    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        self.saldo -= valor








# # Criando o objeto
# conta = Conta('123-x', 0.00, 0.00)
# print('VALOR INICIAL')
# print(conta.__dict__)
# print('---------')
#
# #  realizando credito em conta
# conta.creditar(20.0)
#
# print('APOS CREDITO')
# print(conta.__dict__)
# print('---------')
#
# #  realizando debito em conta
# conta.debitar(5.0)
#
# print("APOS DEBITO")
# print(conta.__dict__)

# conta_a = Conta('1234', 50, 1000)
# conta_b = Conta('1235', 75, 1000)
# conta_c = Conta('1236', 0, 1000)
#
# conta_a.debitar(15)
# conta_b.debitar(15)
# conta_c.creditar(30)
#
# print(conta_c.__dict__)
#

