from tarefa import Tarefa
from datetime import datetime
from prioridade import Prioridade

class Pontual(Tarefa):
    def __init__(self, nome : str, descricao : str, status : bool, prioridade : list[Prioridade], datainicio : datetime.date, prazo : datetime.date):
        super().__init__(nome, descricao, status, prioridade)
        self._datainicio = datainicio
        self._prazo = prazo

    