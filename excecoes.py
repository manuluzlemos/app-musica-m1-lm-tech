# Estudante: Emanuelle da Luz Lemos (manuluz.lemos@gmail.com)
# Exceções de situações específicas

class DadoExiste(Exception):
    def __init__(self, message = "Não é possível cadastrar, pois o dado já existe na base de dados!"):
        self.message = message
        super().__init__(self.message)


class OpcaoInvalida(Exception):
    def __init__(self, message = "Opção inválida!"):
        self.message = message
        super().__init__(self.message)

class DadoInexistente(Exception):
    def __init__(self, message = "O dado não existe na base de dados!"):
        self.message = message
        super().__init__(self.message)
