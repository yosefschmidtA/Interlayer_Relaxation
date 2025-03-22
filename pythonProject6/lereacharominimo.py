# Nome do arquivo de entrada
arquivo = "resultados.txt"

# Inicializa variáveis para armazenar o menor valor e sua combinação
menor_valor = float("inf")
melhor_comb = None

# Leitura dos dados
with open(arquivo, "r") as f:
    for linha in f:
        partes = linha.strip().split()
        if len(partes) == 3:  # Garante que a linha tenha 3 valores
            x, _, valor = float(partes[0]), int(partes[1]), float(partes[2])
            if valor < menor_valor:
                menor_valor = valor
                melhor_comb = x

# Exibe o resultado
if melhor_comb is not None:
    print(f"O menor valor é {menor_valor:.10f} na posição {melhor_comb}")
else:
    print("Nenhum valor válido encontrado.")
