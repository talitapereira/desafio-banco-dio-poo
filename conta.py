from historico import Historico


class Conta:
    
    AGENCIA = "0001"

    def __init__(self, numero, agencia, cliente):
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._saldo = 0
        self._historico = Historico()
        
    @property    
    def saldo (self):
        return self._saldo
    
    @property
    def agencia(self):
        return Conta.AGENCIA
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, Conta.AGENCIA, cliente)
    
    def sacar(self, valor):
        conseguiu_sacar = False
        
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self._saldo:
            print("Valor de saque inválido.")
        else: 
            self._saldo -= valor
            conseguiu_sacar = True
            
        return conseguiu_sacar

    
    def depositar(self, valor):
        return self.valor
    

   
