from tarefa import Tarefa

class Recorrente(Tarefa):
    def __init__(self, nome : str, descricao : str, status : bool, prioridade : list, periodicidade : str):
        super().__init__(nome, descricao, status, prioridade)
        self._periodicidade = periodicidade