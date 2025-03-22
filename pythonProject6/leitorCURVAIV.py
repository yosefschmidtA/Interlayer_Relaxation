import matplotlib.pyplot as plt
import numpy as np

# Nome do arquivo contendo os dados
arquivo = 'dados0.txt'

# Inicializar listas para armazenar as curvas
curvas_x = []
curvas_y5 = []  # Quinta coluna (shift)
curvas_y3 = []  # Terceira coluna (valor fixo ou referência)

# Variáveis temporárias para armazenar cada curva
x_temp = []
y5_temp = []
y3_temp = []

# Abrir e ler o arquivo linha por linha
with open(arquivo, 'r') as f:
    for linha in f:
        linha = linha.strip()
        # Verificar se é separador de curva
        if linha == '--':
            # Salvar curva atual e começar nova
            if x_temp and y5_temp and y3_temp:  # Garante que não está vazio
                curvas_x.append(x_temp)
                curvas_y5.append(y5_temp)
                curvas_y3.append(y3_temp)
            x_temp = []
            y5_temp = []
            y3_temp = []
        elif linha:  # Se não for linha vazia
            partes = linha.split()
            if len(partes) >= 5:  # Garantir que há pelo menos 5 colunas
                x_temp.append(float(partes[0]))  # Primeira coluna (X)
                y3_temp.append(float(partes[4]))  # Quinta coluna (Y3)
                y5_temp.append(float(partes[3]))  # Quarta coluna (Y5)

    # Salvar última curva, caso exista
    if x_temp and y5_temp and y3_temp:
        curvas_x.append(x_temp)
        curvas_y5.append(y5_temp)
        curvas_y3.append(y3_temp)

# Plotar de forma separada (manualmente)
plt.figure(figsize=(10, 7))

# Plotar a 3ª coluna (referência EXP), assumindo que seja a mesma para todas
plt.plot(curvas_x[0], curvas_y3[0], '-', label='Experiment', linewidth=3, color='black')

# Agora, verificar quantas curvas tem e plotar cada uma separadamente
cores = ['blue', 'red', 'green', 'orange', 'purple', 'black']  # Defina cores diferentes

if len(curvas_x) > 0:
    plt.plot(curvas_x[0], curvas_y5[0], '-', label='Vinner 0 eV R-factor: 0.326', linewidth=2, color=cores[0])
if len(curvas_x) > 1:
    plt.plot(curvas_x[1], curvas_y5[1], '-', label='Vinner 10 eV R-factor: 0.360', linewidth=2, color=cores[1])
if len(curvas_x) > 2:
    plt.plot(curvas_x[2], curvas_y5[2], '-', label='Vinner 20 eV R-factor: 0.410', linewidth=2, color=cores[2])

# Cálculo da área sob cada curva com numpy.trapezoid (substituto moderno do trapz)
areas = []  # Lista para armazenar as áreas

for i in range(len(curvas_x)):
    area = np.trapz(curvas_y5[i], curvas_x[i])  # Integração de y em relação a x
    areas.append(area)
    print(f"Área sob a curva {i + 1} (Vinner): {-1*area:.4f}")

# Área da curva experimental (se desejar)
area_exp = np.trapz(curvas_y3[0], curvas_x[0])
print(f"Área sob a curva experimental (EXP): {-1*area_exp:.4f}")

# Personalização do gráfico
plt.xlabel('Φ (degree)', fontsize=40, fontweight='bold')  # Aumentar o tamanho da fonte e colocar em negrito
plt.ylabel('Anisotropy', fontsize=40, fontweight='bold')   # Aumentar o tamanho da fonte e colocar em negrito
plt.title('', fontsize=16, fontweight='bold')  # Título em negrito e maior
plt.legend(fontsize=12)  # Aumentar o tamanho da legenda e em negrito
plt.grid(True)
plt.xticks(fontsize=22)  # Aumentar os números do eixo X e colocar em negrito
plt.yticks(fontsize=22)  # Aumentar os números do eixo Y e colocar em negrito
plt.tight_layout()

# Mostrar o gráfico
plt.show()
