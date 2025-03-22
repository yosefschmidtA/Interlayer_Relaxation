import shutil
import sys
# Nome do arquivo original e da cópia
arquivo_original = "exp.txt"
arquivo_copia = "exp_modificado.txt"

# Criar uma cópia do arquivo original
shutil.copy(arquivo_original, arquivo_copia)

novo_valor = float(sys.argv[1])

# Modificar apenas as linhas necessárias diretamente na cópia
with open(arquivo_copia, "r+") as f:
    linhas = f.readlines()  # Lê todas as linhas do arquivo
    f.seek(0)  # Volta para o início do arquivo para sobrescrever somente as linhas modificadas

    for i, linha in enumerate(linhas):
        if i < 17:  # Mantém as primeiras 17 linhas inalteradas
            f.write(linha)
            continue

        partes = linha.rstrip("\n")  # Remove apenas a quebra de linha
        colunas = partes.split()

        if len(colunas) == 6:  # Verifica se há exatamente 6 colunas
            # Calcula o deslocamento da terceira coluna e mantém a formatação
            inicio_terceira_coluna = linha.index(colunas[2])  # Encontra a posição original
            linha_modificada = linha[:inicio_terceira_coluna] + f"{novo_valor:.4f}" + linha[
                                                                                      inicio_terceira_coluna + len(
                                                                                          colunas[2]):]
            f.write(linha_modificada)
        else:
            f.write(linha)  # Mantém a linha original

    f.truncate()  # Garante que o arquivo não fique com sobra de conteúdo antigo
