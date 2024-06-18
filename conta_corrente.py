from conta import Conta


class Conta_corrente(Conta):
    def __init__(self, limite, limite_saques):
        self.limite = float(500)
        self.limite_saques = int(3) 