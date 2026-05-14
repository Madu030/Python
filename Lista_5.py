import os
import re
import sys
import zipfile
from datetime import datetime


# Lista 5 - Bibliotecas Internas
# 1. Escreva um script que:
# recebe um caminho ( input )
# lista arquivos e pastas do caminho
# para cada arquivo, imprime: nome, tamanho, data de modificação (timestamp ou formatada)
# no fim, imprime:
# total de arquivos
# total de pastas
# tamanho total dos arquivos

def questao1():
    caminho = input("Digite o caminho do diretorio: ")
    conteudo = os.listdir(caminho)
    totalDeArquivos = 0
    totalDePastas = 0
    tamanhoTotalDosArquivos = 0

    print(f"{'Nome':<15} {'Tamanho':>14} {'Data de Modificação':<20}")
    print('-' * 50)

    for i in conteudo:
        caminhoCompleto = os.path.join(caminho, i)

        tamanho = os.path.getsize(caminhoCompleto)

        timestamp = os.path.getmtime(caminhoCompleto)
        dataDeModificacao = datetime.fromtimestamp(timestamp)

        print(f"{i:<15} {tamanho:>14} {dataDeModificacao:%Y-%m-%d %H:%M:%S}")

        if (os.path.isdir(caminhoCompleto)):
            totalDePastas += 1
        elif (os.path.isfile(caminhoCompleto)):
            totalDeArquivos += 1

        tamanhoTotalDosArquivos += tamanho

    print("-" * 50)
    print(f"Arquivos: {totalDeArquivos}")
    print(f"Pastas: {totalDePastas}")
    print(f"Tamanho total: {tamanhoTotalDosArquivos}mb")


# 2. Crie um pacote chamado estatistica com dois módulos:
# leitor.py: Contendo uma função ler_csv(caminho) que leia um arquivo CSV e retorne uma lista de
# dicionários, convertendo automaticamente valores numéricos.
# analise.py: Contendo uma função estatisticas(dados, campo) que receba os dados lidos (lista de
# dicionários) e o nome de um campo numérico, e retorne um dicionário com estatísticas básicas
# (média, mínimo, máximo e total).
def questao2():
    estatistica = 'estatistica'

    if not os.path.exists(estatistica):
        os.mkdir(estatistica)
        print("Diretório 'estatistica' criado com sucesso!")
    else:
        print("Diretório 'estatística' já existe!")

    diretorioAtual = os.getcwd()
    caminhoParaEstatistica = diretorioAtual + r'\estatistica'

    with open(caminhoParaEstatistica + r'\listar.py', 'w') as f:
        f.write('''import csv

def ler_csv(caminho):
    dados = []
    with open(caminho, newline='') as f:
        leitor = csv.DictReader(f)

        for  linha in leitor:

            for chave, valor in linha.items():
                try:
                    linha[chave] = int(float(valor))
                except ValueError:
                    pass

            dados.append(linha)
    return dados
    ''')

    with open(caminhoParaEstatistica + r'\analise.py', 'w') as f:
        f.write('''def estatisticas(dados, campo):
    valores = [item[campo] for item in dados]

    return {
        'media': sum(valores) / len(valores),
        'minimo': min(valores),
        'maximo': max(valores),
        'total': sum(valores)
    }
        ''')

    from estatistica.listar import ler_csv
    from estatistica.analise import estatisticas

    caminhoDoCsv = input('Digite o caminho do arquivo .csv: ')
    dadosDoCsv = ler_csv(caminhoDoCsv)

    print(dadosDoCsv)
    chave = input('Digite qual campo você deseja ver a análise estatística: ')
    print(estatisticas(dadosDoCsv, chave))


# 3. Implemente um interpretador que avalie expressões aritméticas simples compostas pelas
# operações +, -, *, / e parênteses. Utilize funções recursivas para realizar o parsing e a avaliação da
# expressão. Além disso, defina as operações básicas usando expressões lambda em um dicionário
# de operadores.

# Requisitos:
# Crie um módulo chamado interprete.py contendo:
# Um dicionário que mapeia os operadores para funções lambda (por exemplo, {'+' : lambda
# a, b: a + b, ...} ).
# Uma função recursiva avaliar(expressao) que recebe uma string com a expressão e retorna
# o resultado numérico.
# O interpretador deve lidar com a precedência dos operadores e com parênteses.
def questao3():
    operacoes = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }


    def avaliar(expressao):

        expressao = expressao.replace(" ", "")
        indice = 0

        def parse_expressao():
            nonlocal indice

            resultado = parse_termo()

            while indice < len(expressao) and expressao[indice] in "+-":
                operador = expressao[indice]
                indice += 1

                proximo = parse_termo()

                resultado = operacoes[operador](resultado, proximo)

            return resultado

        def parse_termo():
            nonlocal indice

            resultado = parse_fator()

            while indice < len(expressao) and expressao[indice] in "*/":
                operador = expressao[indice]
                indice += 1

                proximo = parse_fator()

                resultado = operacoes[operador](resultado, proximo)

            return resultado

        def parse_fator():
            nonlocal indice

            # Parênteses
            if expressao[indice] == '(':
                indice += 1

                resultado = parse_expressao()

                indice += 1  # pula ')'

                return resultado

            numero = ""

            while indice < len(expressao) and expressao[indice].isdigit():
                numero += expressao[indice]
                indice += 1

            return int(numero)

        return parse_expressao()

    print(avaliar("(1+2)*3"))

# 4. Desenvolva um simulador de jogo de dados onde, ao lançar os dados, diferentes eventos são
# disparados com base no resultado. Organize o código em um pacote chamado jogo com os
# módulos:
# dados.py: Função para simular o lançamento de um dado (usando random.randint ).
# eventos.py: Implementação de um sistema de eventos que permite registrar chamadas para
# determinados resultados (por exemplo, se o dado mostrar 6, disparar o evento "sorte").

def questao4():
    pacote = 'simulador'

    if not os.path.exists(pacote):
        os.mkdir(pacote)
        print("Diretório 'jogo' criado com sucesso!")
    else:
        print("Diretório 'jogo' já existe!")

    diretorioAtual = os.getcwd()
    caminhoParaJogo = os.path.join(diretorioAtual, pacote)

    with open(os.path.join(caminhoParaJogo, '__init__.py'), 'w') as f:
        f.write('')

    with open(os.path.join(caminhoParaJogo, 'dados.py'), 'w') as f:
        f.write('''import random

def lancar_dado():
    return random.randint(1, 6)
    ''')

    with open(os.path.join(caminhoParaJogo, 'eventos.py'), 'w') as f:
        f.write('''_registro = {}

def registrar(resultado, callback):
    _registro.setdefault(resultado, []).append(callback)

def disparar(resultado):
    callbacks = _registro.get(resultado, [])
    if callbacks:
        for cb in callbacks:
            cb(resultado)
    else:
        print(f"  Resultado {resultado}: nenhum evento especial.")
    ''')

    from simulador.dados import lancar_dado
    from simulador.eventos import registrar, disparar

    registrar(1, lambda r: print(f"  Resultado {r}: Azar! Você perdeu a vez."))
    registrar(6, lambda r: print(f"  Resultado {r}: SORTE! Jogue novamente!"))
    registrar(3, lambda r: print(f"  Resultado {r}: Metade do caminho!"))

    print("\n=== Simulador de Jogo de Dados ===")
    rodadas = int(input("Quantas rodadas deseja jogar? "))

    for rodada in range(1, rodadas + 1):
        input(f"\nRodada {rodada} — pressione Enter para lançar o dado...")
        resultado = lancar_dado()
        print(f"  Dado: {resultado}")
        disparar(resultado)


# 5. Crie um script que:
# encontra todos os arquivos .txt em um diretório (pode ser o atual)
# Lista 5 - Bibliotecas Internas 1
# cria um backup.zip
# grava esses arquivos no zip
# ao final imprime: para cada arquivo, tamanho original e comprimido
def questao5():
    diretorio = os.path.dirname(os.path.abspath(__file__))

    arquivos = {
        "compras.txt": """leite
    pão
    ovos
    manteiga
    arroz
    feijão
    macarrão
    azeite
    sal
    açúcar
    """,
        "agenda.txt": """09:00 - Reunião com equipe
    10:30 - Revisão do projeto
    12:00 - Almoço
    14:00 - Apresentação para o cliente
    16:00 - Atualizar documentação
    17:30 - Daily de encerramento
    """,
        "notas.txt": """Estudar Python todos os dias.
    Praticar exercícios das listas.
    Revisar orientação a objetos.
    Ler sobre bibliotecas padrão.
    Fazer projetos pequenos para fixar o conteúdo.
    """,
        "contatos.txt": """Nome: Ana Silva | (11)98765-4321 | ana.silva@email.com
    Nome: Bruno Costa | (21)91234-5678 | bruno.costa@gmail.com
    Nome: Carla Souza | (31)3456-7890 | carla.souza@outlook.com
    Nome: Diego Lima | (41)99876-5432 | diego.lima@yahoo.com
    """,
        "log.txt": """[2025-05-01 08:00:01] INFO  - Sistema iniciado.
    [2025-05-01 08:05:32] INFO  - Usuário admin fez login.
    [2025-05-01 08:47:10] WARN  - Tentativa de acesso negada.
    [2025-05-01 09:12:55] ERROR - Falha ao conectar ao banco de dados.
    [2025-05-01 09:13:01] INFO  - Reconexão bem-sucedida.
    [2025-05-01 10:00:00] INFO  - Backup automático concluído.
    """,
    }

    print(f"Criando arquivos .txt em: {diretorio}\n")
    print(f"{'Arquivo':<20} {'Tamanho (B)':>12}")
    print("-" * 34)

    for nome, conteudo in arquivos.items():
        caminho = os.path.join(diretorio, nome)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)
        tamanho = os.path.getsize(caminho)
        print(f"{nome:<20} {tamanho:>12}")

    print("-" * 34)
    print(f"{len(arquivos)} arquivos criados com sucesso!")

    diretorio = input("Digite o diretório a ser varrido (Enter = atual): ").strip() or "."
    arquivos_txt = [
        os.path.join(diretorio, f)
        for f in os.listdir(diretorio)
        if f.endswith(".txt") and os.path.isfile(os.path.join(diretorio, f))
    ]

    if not arquivos_txt:
        print("Nenhum arquivo .txt encontrado no diretório.")
        return

    caminho_zip = os.path.join(diretorio, "backup.zip")

    with zipfile.ZipFile(caminho_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for caminho in arquivos_txt:
            zf.write(caminho, arcname=os.path.basename(caminho))

    print(f"\n{'Arquivo':<30} {'Original (B)':>14} {'Comprimido (B)':>16}")
    print("-" * 62)

    with zipfile.ZipFile(caminho_zip, "r") as zf:
        for info in zf.infolist():
            print(f"{info.filename:<30} {info.file_size:>14} {info.compress_size:>16}")

    print("-" * 62)
    print(f"Backup salvo em: {caminho_zip}")


# 6. Leia duas datas no formato DD/MM/AAAA e calcule:
# diferença em dias
# diferença em semanas e dias (ex.: 9 semanas e 3 dias)
# qual data é maior
def questao6():
    def ler_data(label):
        while True:
            texto = input(f"Digite a {label} (DD/MM/AAAA): ")
            try:
                return datetime.strptime(texto, "%d/%m/%Y").date()
            except ValueError:
                print("  Formato inválido. Use DD/MM/AAAA.")

    data1 = ler_data("1ª data")
    data2 = ler_data("2ª data")

    delta = abs((data2 - data1).days)
    semanas, dias_restantes = divmod(delta, 7)

    print(f"\nDiferença em dias: {delta} dia(s)")
    print(f"Diferença em semanas: {semanas} semana(s) e {dias_restantes} dia(s)")

    if data1 > data2:
        print(f"A data maior é: {data1.strftime('%d/%m/%Y')}")
    elif data2 > data1:
        print(f"A data maior é: {data2.strftime('%d/%m/%Y')}")
    else:
        print("As duas datas são iguais.")

# 7. Dado um texto ( input ), extraia e imprima:
# todos os e-mails encontrados
# todos os números de telefone no padrão simples (XX)XXXXX-XXXX ou (XX)XXXX-XXXX
# substitua múltiplos espaços por um único espaço e imprima o texto “limpo”
def questao7():
    print('Digite o texto')
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)
    texto = " ".join(linhas)

    # E-mails
    emails = re.findall(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", texto)

    # Telefones: (XX)XXXXX-XXXX ou (XX)XXXX-XXXX
    telefones = re.findall(r"\(\d{2}\) ?\d{4,5}-\d{4}", texto)

    # Texto limpo (múltiplos espaços → um único)
    texto_limpo = re.sub(r" {2,}", " ", texto)

    print(f"\nE-mails encontrados ({len(emails)}):")
    for email in emails:
        print(f"  {email}")

    print(f"\nTelefones encontrados ({len(telefones)}):")
    for tel in telefones:
        print(f"  {tel}")

    print(f"\nTexto limpo:\n  {texto_limpo}")

# E-mails encontrados (3):
#   suporte@empresa.com
#   comercial@empresa.com.br
#   financeiro@empresa.com
#
# Telefones encontrados (3):
#   (11)98765-4321
#   (21)3456-7890
#   (31)99876-5432
#
# Texto limpo:
#   Olá! Entre em contato com a nossa equipe pelo e-mail suporte@empresa.com ...


questao1()
print('\n')
questao2()
print('\n')
questao3()
print('\n')
questao4()
print('\n')
questao5()
print('\n')
questao6()
print('\n')
questao7()