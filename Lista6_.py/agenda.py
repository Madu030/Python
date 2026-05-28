from contato import Contato
from evento import Evento


class Agenda:
    _contatos: list[Contato] = []
    _eventos: list[Evento] = []

    def __init__(self, item: Contato | Evento | None = None):
        if isinstance(item, Contato):
            Agenda._contatos.append(item)
        elif isinstance(item, Evento):
            Agenda._eventos.append(item)

    # ── métodos estáticos ─────────────────────────────
    @staticmethod
    def contatos() -> list[Contato]:
        return Agenda._contatos

    @staticmethod
    def eventos() -> list[Evento]:
        return Agenda._eventos

    @staticmethod
    def adicionar_contato(contato: Contato):
        Agenda._contatos.append(contato)

    @staticmethod
    def adicionar_evento(evento: Evento):
        Agenda._eventos.append(evento)