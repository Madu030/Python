import datetime
from contato import Contato
from contato_emergencia import ContatoEmergencia
from evento import Evento
from agenda import Agenda

def ler_data(prompt: str) -> datetime.date:
    while True:
        try:
            raw = input(prompt)
            return datetime.datetime.strptime(raw, "%d/%m/%Y").date()
        except ValueError:
            print("  Data inválida. Use o formato dd/mm/aaaa.")


def ler_nao_vazio(prompt: str) -> str:
    while True:
        valor = input(prompt).strip()
        if valor:
            return valor
        print("  Campo obrigatório.")


def ler_email(prompt: str) -> str:
    while True:
        valor = input(prompt).strip()
        if "@" in valor:
            return valor
        print("  E-mail inválido.")


def selecionar_contato() -> Contato | None:
    contatos = Agenda.contatos()
    if not contatos:
        print("  Nenhum contato cadastrado.")
        return None
    print("\n  Contatos disponíveis:")
    for i, c in enumerate(contatos, 1):
        print(f"    [{i}] {c.nome}")
    while True:
        try:
            idx = int(input("  Escolha o número do contato: ")) - 1
            if 0 <= idx < len(contatos):
                return contatos[idx]
            print("  Número inválido.")
        except ValueError:
            print("  Digite um número.")

def menu_contatos():
    while True:
        print("\n  --- Contatos ---")
        print("  1 - Criar contato")
        print("  2 - Editar contato")
        print("  3 - Listar contatos")
        print("  0 - Voltar")
        opcao = input("  Opção: ").strip()

        match opcao:
            case "1":
                nome     = ler_nao_vazio("  Nome: ")
                telefone = ler_nao_vazio("  Telefone: ")
                nasc     = ler_data("  Data de nascimento (dd/mm/aaaa): ")
                email    = ler_email("  E-mail: ")
                c = Contato(nome, telefone, nasc, email)
                Agenda.adicionar_contato(c)
                print(f"\n  Contato '{c.nome}' cadastrado com sucesso!")

            case "2":
                c = selecionar_contato()
                if not c:
                    continue
                print("\n  O que deseja editar?")
                print("  1 - Nome  2 - Telefone  3 - Data de nasc.  4 - E-mail")
                campo = input("  Campo: ").strip()
                match campo:
                    case "1":
                        c.nome = ler_nao_vazio("  Novo nome: ")
                    case "2":
                        c.telefone = ler_nao_vazio("  Novo telefone: ")
                    case "3":
                        c.datanasc = ler_data("  Nova data (dd/mm/aaaa): ")
                    case "4":
                        c.email = ler_email("  Novo e-mail: ")
                    case _:
                        print("  Opção inválida.")
                        continue
                print("  Contato atualizado!")

            case "3":
                contatos = Agenda.contatos()
                if not contatos:
                    print("  Nenhum contato cadastrado.")
                else:
                    for i, c in enumerate(contatos, 1):
                        print(f"\n  [{i}]")
                        print(f"  {c}")
                        print("  " + "-" * 40)

            case "0":
                break

            case _:
                print("  Opção inválida.")


def menu_emergencia():
    print("\n  --- Novo Contato de Emergência ---")
    nome     = ler_nao_vazio("  Nome: ")
    telefone = ler_nao_vazio("  Telefone: ")
    nasc     = ler_data("  Data de nascimento (dd/mm/aaaa): ")
    email    = ler_email("  E-mail: ")
    prior    = input("  Alta prioridade? (s/n): ").strip().lower() == "s"
    c = ContatoEmergencia(nome, telefone, nasc, email, prior)
    Agenda.adicionar_contato(c)
    print(f"\n  Contato de emergência '{c.nome}' cadastrado!")
    print(f"  {c}")


def menu_eventos():
    while True:
        print("\n  --- Eventos ---")
        print("  1 - Criar evento")
        print("  2 - Listar eventos")
        print("  0 - Voltar")
        opcao = input("  Opção: ").strip()

        match opcao:
            case "1":
                descricao = ler_nao_vazio("  Descrição: ")
                inicio    = ler_data("  Data de início (dd/mm/aaaa): ")
                fim       = ler_data("  Data de fim   (dd/mm/aaaa): ")
                print("\n  Escolha o contato associado ao evento:")
                contato = selecionar_contato()
                if not contato:
                    continue
                try:
                    e = Evento(descricao, inicio, fim, contato)
                    Agenda.adicionar_evento(e)
                    print(f"\n  Evento '{descricao}' criado com sucesso!")
                except ValueError as err:
                    print(f"  Erro: {err}")

            case "2":
                eventos = Agenda.eventos()
                if not eventos:
                    print("  Nenhum evento cadastrado.")
                else:
                    for i, e in enumerate(eventos, 1):
                        print(f"\n  [{i}]")
                        print(f"  {e.get_informacoes()}")
                        print("  " + "-" * 40)

            case "0":
                break

            case _:
                print("  Opção inválida.")

def main():
    print("=" * 45)
    print("       Bem-vindo à Agenda Telefônica")
    print("=" * 45)

    while True:
        print("\n  [1] Contatos")
        print("  [2] Contatos de Emergência")
        print("  [3] Eventos")
        print("  [0] Sair")
        opcao = input("\n  Escolha uma opção: ").strip()

        match opcao:
            case "1":
                menu_contatos()
            case "2":
                menu_emergencia()
            case "3":
                menu_eventos()
            case "0":
                total = Evento.get_total_eventos()
                print(f"\n  Total de eventos criados nesta sessão: {total}")
                print("  Até logo!")
                break
            case _:
                print("  Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()