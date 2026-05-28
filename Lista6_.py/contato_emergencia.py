import datetime
from contato import Contato

class ContatoEmergencia(Contato):
    __slots__ = ("_prioridade",)

    def __init__(self, nome: str, telefone: str, datanasc: datetime.date, email: str, prioridade: bool = True):
        super().__init__(nome, telefone, datanasc, email)
        self._prioridade = prioridade

    @property
    def prioridade(self) -> bool:
        return self._prioridade

    def __str__(self) -> str:
        prioridade_str = "Alta" if self._prioridade else "Normal"
        return f"{super().__str__()}\nPrioridade:      {prioridade_str}"