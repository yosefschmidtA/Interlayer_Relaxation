import numpy as np
import pandas as pd
import random


# Carregar os dados do arquivo corretamente
def load_rfactor_data(filename):
    data = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            interlayer1_value = round(float(lines[i].split('=')[1].strip()), 3)
            interlayer2_value = round(float(lines[i + 1].split('=')[1].split()[0].strip()), 3)
            rfactor_value = round(float(lines[i + 1].split('=')[2].strip()), 3)
            data[(interlayer1_value, interlayer2_value)] = rfactor_value
    return data


# Simulação de busca iterativa sem QAOA para testes
def simulated_search(data, max_iterations=100):
    interlayer_values = np.arange(0.13, 0.41, 0.01)  # Valores permitidos

    # Escolha inicial aleatória de interlayers dentro do intervalo
    inter1 = round(random.choice(interlayer_values),3)
    inter2 = round(random.choice(interlayer_values),3)
    best_rfactor = data.get((inter1, inter2), float('inf'))
    best_params = (inter1, inter2)

    print(f"Iniciando busca com Interlayer1 = {inter1}, Interlayer2 = {inter2}, R-factor = {best_rfactor}")

    for _ in range(max_iterations):
        inter1 = round(random.choice(interlayer_values), 3)
        inter2 = round(random.choice(interlayer_values), 3)
        new_rfactor = data.get((inter1, inter2), float('inf'))

        if new_rfactor < best_rfactor:
            best_rfactor = new_rfactor
            best_params = (inter1, inter2)

        print(f"Nova tentativa: Interlayer1 = {inter1}, Interlayer2 = {inter2}, R-factor = {new_rfactor}")

    print("Melhor resultado encontrado:")
    print(f"Interlayer1 = {best_params[0]}, Interlayer2 = {best_params[1]}, R-factor = {best_rfactor}")
    return best_params, best_rfactor


# Simulação
filename = "dadosd123bcc.txt"  # Arquivo de entrada
rfactor_data = load_rfactor_data(filename)
simulated_search(rfactor_data)
