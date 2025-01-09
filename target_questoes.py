import json

# Questão 1 - Cálculo da soma de 1 até o valor de INDICE
def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    print(f"Soma dos números de 1 até {INDICE}: {SOMA}")

# Questão 2 - Verificação se um número pertence à sequência de Fibonacci
def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

def verificar_fibonacci():
    numero = int(input("Informe um número para verificar se ele pertence à sequência de Fibonacci: "))
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# Questão 3 - Cálculo de menor e maior faturamento diário e dias acima da média
def calcular_faturamento():
    faturamento_json = '''{
        "SP": [67836.43, 0, 0, 0, 0, 0, 0, 5000.00, 0, 10000.00],
        "RJ": [36678.66, 1000.00, 1500.00, 0, 0, 0, 2000.00, 0, 0, 0],
        "MG": [29229.88, 0, 0, 2000.00, 2500.00, 0, 0, 0, 0, 3000.00],
        "ES": [27165.48, 0, 1000.00, 0, 0, 500.00, 1000.00, 0, 0, 0],
        "Outros": [19849.53, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }'''

    faturamento = json.loads(faturamento_json)

    # Flatten list
    faturamento_diario = [valor for lista in faturamento.values() for valor in lista]

    # Calculando o menor e maior valor de faturamento
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)

    # Calculando a média de faturamento, ignorando os dias com faturamento 0
    dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
    media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

    # Calculando os dias com faturamento acima da média
    dias_acima_media = len([valor for valor in dias_com_faturamento if valor > media_faturamento])

    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias acima da média: {dias_acima_media}")

# Questão 4 - Cálculo do percentual de faturamento por estado
def calcular_percentual_faturamento():
    faturamento_estado = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    total_faturamento = sum(faturamento_estado.values())

    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estado.items()}

    for estado, percentual in percentuais.items():
        print(f"Percentual de {estado}: {percentual:.2f}%")

# Questão 5 - Inversão dos caracteres de uma string
def inverter_string(s):
    return s[::-1]

def inverter_texto():
    texto = input("Digite um texto para inverter: ")
    texto_invertido = inverter_string(texto)
    print(f"Texto invertido: {texto_invertido}")

# Menu para selecionar qual questão executar
def menu():
    while True:
        print("\nEscolha a questão que deseja executar:")
        print("1 - Cálculo da soma de 1 até o valor de INDICE")
        print("2 - Verificação se um número pertence à sequência de Fibonacci")
        print("3 - Cálculo de faturamento diário")
        print("4 - Cálculo do percentual de faturamento por estado")
        print("5 - Inversão dos caracteres de uma string")
        print("0 - Sair")

        escolha = input("Digite o número da questão: ")

        if escolha == '1':
            calcular_soma()
        elif escolha == '2':
            verificar_fibonacci()
        elif escolha == '3':
            calcular_faturamento()
        elif escolha == '4':
            calcular_percentual_faturamento()
        elif escolha == '5':
            inverter_texto()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
