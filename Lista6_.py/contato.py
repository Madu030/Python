import datetime


class Contato:
    __slots__ = ("_nome", "_telefone", "_datanasc", "_email")

    def __init__(self, nome: str, telefone: str, datanasc: datetime.date, email: str):
        self._nome = nome
        self._telefone = telefone
        self._datanasc = datanasc
        self._email = email

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor.strip():
            raise ValueError("Nome não pode ser vazio.")
        self._nome = valor.strip()

    @property
    def telefone(self) -> str:
        return self._telefone

    @telefone.setter
    def telefone(self, valor: str):
        if not valor.strip():
            raise ValueError("Telefone não pode ser vazio.")
        self._telefone = valor.strip()

    @property
    def datanasc(self) -> datetime.date:
        return self._datanasc

    @datanasc.setter
    def datanasc(self, valor: datetime.date):
        if not isinstance(valor, datetime.date):
            raise TypeError("Data de nascimento deve ser um datetime.date.")
        self._datanasc = valor

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str):
        if "@" not in valor:
            raise ValueError("E-mail inválido.")
        self._email = valor.strip()

    def __str__(self) -> str:
        return (
            f"Nome:            {self._nome}\n"
            f"Telefone:        {self._telefone}\n"
            f"Data de nasc.:   {self._datanasc.strftime('%d/%m/%Y')}\n"
            f"E-mail:          {self._email}"
        )