from conta import Conta


class Conta_corrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    def _obter_quantidade_saques() -> int:
        
        pass
    
    def sacar(self, valor,numero_saques):
        conseguiu_sacar = False
        
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self._saldo:
            print("Valor de saque inválido.")
        
        elif numero_saques >= self._limite_saques:
            print("Número de saques diários excedido.")
        
        else: 
            self._saldo -= valor
            conseguiu_sacar = True
            
        return conseguiu_sacar