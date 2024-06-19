from transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self, conta):
        pass

    @property
    def valor(self):
        return self._valor
    
    
