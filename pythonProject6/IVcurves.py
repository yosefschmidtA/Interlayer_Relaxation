import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from scipy.ndimage import gaussian_filter1d
import numpy as np

# Lendo o arquivo e separando os blocos de dados
with open("structure4.txt", "r") as file:
    lines = file.readlines()

# Encontrando o índice do separador "--"
separator_index = next(i for i, line in enumerate(lines) if "--" in line)

df1 = pd.read_csv(StringIO("".join(lines[:separator_index])), delim_whitespace=True, header=None)
df2 = pd.read_csv(StringIO("".join(lines[separator_index + 1:])), delim_whitespace=True, header=None)
df3 = (df2[2] + df1[2]) / 2

# Criando o gráfico
plt.figure(figsize=(8, 6), dpi=100)

# Aplicando suavização gaussiana com sigma=1 (ajuste conforme necessário)
df3_smooth = gaussian_filter1d(df3, sigma=1)
df_smooth_not_normalized = pd.DataFrame({"Energy (eV)": df1[0], "Intensity Smooth (a.u.)": df3_smooth})
df_smooth = pd.DataFrame({"Energy (eV)": df1[0], "Intensity Smooth (a.u.)": df3_smooth})

# Lendo o arquivo de corrente sem cabeçalho e convertendo corretamente os valores numéricos
arquivo_corrente = "corrente.txt"
df_corrente = pd.read_csv(arquivo_corrente, sep="\t", header=None, names=["Energia(eV)", "Io(uA)"], dtype={"Energia(eV)": float, "Io(uA)": str})

# Corrigindo vírgula decimal (caso exista) e convertendo a coluna para float
df_corrente["Io(uA)"] = df_corrente["Io(uA)"].str.replace(",", ".").astype(float)

# Criando um dicionário Energia -> Corrente absoluta
corrente_dict = dict(zip(df_corrente["Energia(eV)"], abs(df_corrente["Io(uA)"])))

# Normalizando a intensidade dividindo pelo módulo da corrente correspondente
df_smooth["Normalized Intensity"] = df_smooth.apply(
    lambda row: row["Intensity Smooth (a.u.)"] / corrente_dict[row["Energy (eV)"]]
    if row["Energy (eV)"] in corrente_dict else np.nan, axis=1
)

# Salvando o novo arquivo
df_smooth.to_csv("dados_normalizados.txt", sep="\t", index=False, float_format="%.6f")

# Plotando os dois conjuntos
plt.plot(df1[0], df_smooth["Normalized Intensity"], linestyle="-", linewidth=2, color="black", label="([4,-4]  Normalized")
#plt.plot(df1[0], df_smooth["Intensity Smooth (a.u.)"], linestyle="-", linewidth=2, color="blue", label="([3,0]+[-3,0])/2 not Normalized")
# Configurando os eixos e rótulos
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel("Energy (eV)", fontsize=22, fontweight="bold")
plt.ylabel("Intensity (a.u)", fontsize=22, fontweight="bold")

# Adicionando legenda
plt.legend(fontsize=14)

# Salvando e mostrando o gráfico
save_path = 'curva1.png'
plt.savefig(save_path, dpi=200, bbox_inches='tight')
plt.show()

# Nome do arquivo de saída
output_file = "dados_formatados.txt"

# Número de pontos
num_pontos = len(df_smooth)

# Valor fixo (1.000E-003)
valor_fixo = 1.000E-3

# Abrindo o arquivo para escrita
with open(output_file, "w") as f:
    # Escrevendo o cabeçalho
    f.write(f"{num_pontos:3d}   {valor_fixo:.3E}\n")

    # Escrevendo os valores de energia e intensidade normalizada com a formatação correta
    for energia, intensidade in zip(df_smooth["Energy (eV)"], df_smooth["Normalized Intensity"]):
        f.write(f"{energia:6.2f}{intensidade:15.5f}\n")

print(f"Arquivo '{output_file}' gerado com sucesso!")
