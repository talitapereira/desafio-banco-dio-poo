
from transacao import Transacao


class Cliente():
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.resgistrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)