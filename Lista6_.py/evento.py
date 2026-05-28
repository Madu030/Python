import datetime
from contato import Contato


class Evento:
    _total_eventos: int = 0

    def __init__(self, descricao: str, data_inicio: datetime.date, data_fim: datetime.date, contato: Contato):
        if data_fim < data_inicio:
            raise ValueError("A data de fim não pode ser anterior à data de início.")
        self._descricao = descricao
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._contato = contato
        Evento._total_eventos += 1

    def get_informacoes(self) -> str:
        return (
            f"Descrição:   {self._descricao}\n"
            f"Início:      {self._data_inicio.strftime('%d/%m/%Y')}\n"
            f"Fim:         {self._data_fim.strftime('%d/%m/%Y')}\n"
            f"Contato:     {self._contato.nome}"
        )

    @staticmethod
    def get_total_eventos() -> int:
        return Evento._total_eventos

    def __str__(self) -> str:
        return self.get_informacoes()