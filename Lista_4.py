import math

def questao1():
    print("\n--- Questão 1: Dicionário palavra → nº de caracteres ---")
    palavras = ["amor", "roma", "mora", "carro", "orça", "orca", "arco"]

    resultado = {palavra: len(palavra) for palavra in palavras}

    print("Entrada:", palavras)
    print("Saída:", resultado)

def questao2():
    print("\n--- Questão 2: Agrupamento de anagramas ---")
    palavras = ["amor", "roma", "mora", "carro", "orça", "orca", "arco"]

    anagramas = {}
    for palavra in palavras:
        chave = tuple(sorted(palavra))
        if chave not in anagramas:
            anagramas[chave] = []
        anagramas[chave].append(palavra)

    print("Entrada:", palavras)
    print("Saída:")
    for chave, grupo in anagramas.items():
        print(f"  {chave}: {grupo}")

def questao3():
    print("\n--- Questão 3: Multiplicação de polinômios ---")
    p1 = {2: 3, 1: 2, 0: 1} 
    p2 = {1: 1, 0: 1}        

    def multiplicar_polinomios(p1, p2):
        resultado = {}
        for exp1, coef1 in p1.items():
            for exp2, coef2 in p2.items():
                exp = exp1 + exp2
                resultado[exp] = resultado.get(exp, 0) + coef1 * coef2
        return resultado

    resultado = multiplicar_polinomios(p1, p2)

    print("p1:", p1, " → 3x² + 2x + 1")
    print("p2:", p2, " → x + 1")
    print("p1 × p2:", resultado)

def questao4():
    print("\n--- Questão 4: aplicar_operacao ---")

    def soma(a, b):          return a + b
    def subtracao(a, b):     return a - b
    def multiplicacao(a, b): return a * b
    def divisao(a, b):       return a / b
    def resto(a, b):         return a % b
    def potencia(a, b):      return a ** b
    def raiz(a):             return math.sqrt(a)
    def fatorial(a):         return math.factorial(int(a))
    def logaritmo(a, b):     return math.log(a, b)
    def cosseno(a):          return math.cos(math.radians(a))
    def seno(a):             return math.sin(math.radians(a))
    def tangente(a):         return math.tan(math.radians(a))

    def aplicar_operacao(operacao, a=None, b=None):
        if a is not None and b is not None:
            return operacao(a, b)
        elif a is not None:
            return operacao(a)
        else:
            raise ValueError("Ao menos um número deve ser fornecido.")

    print(f"soma(3, 5)           = {aplicar_operacao(soma, 3, 5)}")
    print(f"subtracao(10, 4)     = {aplicar_operacao(subtracao, 10, 4)}")
    print(f"multiplicacao(3, 7)  = {aplicar_operacao(multiplicacao, 3, 7)}")
    print(f"divisao(15, 4)       = {aplicar_operacao(divisao, 15, 4)}")
    print(f"resto(10, 3)         = {aplicar_operacao(resto, 10, 3)}")
    print(f"potencia(2, 8)       = {aplicar_operacao(potencia, 2, 8)}")
    print(f"raiz(144)            = {aplicar_operacao(raiz, 144)}")
    print(f"fatorial(6)          = {aplicar_operacao(fatorial, 6)}")
    print(f"logaritmo(100, 10)   = {aplicar_operacao(logaritmo, 100, 10)}")
    print(f"cosseno(60)          = {aplicar_operacao(cosseno, 60):.4f}")
    print(f"seno(30)             = {aplicar_operacao(seno, 30):.4f}")
    print(f"tangente(45)         = {aplicar_operacao(tangente, 45):.4f}")


def questao5():
    print("\n--- Questão 5: Sequência recursiva com memoização ---")
    memo = {}

    def T(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        memo[n] = T(n - 1) + 2 * T(n - 2)
        return memo[n]

    T_lambda = lambda n: T(n)

    print("T(n) = T(n-1) + 2*T(n-2), T(0)=0, T(1)=1")
    for i in range(11):
        print(f"  T({i}) = {T_lambda(i)}")


questao1()
questao2()
questao3()
questao4()
questao5()