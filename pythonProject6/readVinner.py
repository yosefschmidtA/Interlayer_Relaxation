import matplotlib.pyplot as plt
arquivo = 'VinnerGa.txt'


x = []
y = []

with open(arquivo, 'r') as f:
    for linha in f:
        partes = linha.split()
        if len(partes) >= 3:  # Garantir que a linha tenha pelo menos 3 colunas
            x.append(float(partes[0]))  # Primeira coluna (X)
            y.append(float(partes[2]))  # Terceira coluna (Y)


plt.figure(figsize=(10, 7))
plt.plot(x, y, label='Dados', linewidth=2, color='blue')


plt.xlabel('Vinner (eV)', fontsize=36, fontweight='bold')  # Eixo X
plt.ylabel('R-factor', fontsize=36, fontweight='bold')  # Eixo Y
plt.title('', fontsize=16, fontweight='bold')
plt.xticks(fontsize=22)  # Aumentar os números do eixo X e colocar em negrito
plt.yticks(fontsize=22)  # Aumentar os números do eixo Y e colocar em negrito
plt.legend(fontsize=0)
plt.grid(True)


plt.tight_layout()
plt.show()
