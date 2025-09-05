from datetime import datetime
from prioridade import Prioridade

class Tarefa:
    def __init__(self, nome : str, descricao : str, status : bool, prioridade : list[Prioridade], datainicio : datetime.date, prazo : datetime.date):
        self._nome = nome
        self._descricao = descricao
        self._status = status
        self._prioridade = prioridade
        self._datainicio = datainicio
        self._prazo = prazo