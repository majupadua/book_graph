import pandas as pd
import numpy as np
import os

# Cria a pasta 'data' se não existir
os.makedirs("app/aux_data", exist_ok=True)

# Lê os dados do Excel
df = pd.read_excel("app/aux_data/base_pesos.xlsx")

# Cria uma lista única de livros
livros = pd.concat([df["Livro 1"], df["Livro 2"]]).unique()
livro_idx = {livro: idx for idx, livro in enumerate(livros)}

# Número de livros
n = len(livros)

# Inicializa a lista de adjacência
lista_adjacencia = {livro: [] for livro in livros}

# Preenche a lista de adjacência com os pesos
for _, row in df.iterrows():
    livro1, livro2, peso = row["Livro 1"], row["Livro 2"], int(row["Peso"])
    lista_adjacencia[livro1].append((livro2, peso))
    lista_adjacencia[livro2].append((livro1, peso))

# Grava a lista de adjacência no arquivo
with open("app/aux_data/lista_adjacencia.txt", "w") as f:
    for livro, conexoes in lista_adjacencia.items():
        conexoes_txt = ", ".join(f"{conexao[0]} (peso: {conexao[1]})" for conexao in conexoes)
        f.write(f"{livro}: [{conexoes_txt}]\n")

print("Lista de adjacência com pesos salva em 'app/aux_data/lista_adjacencia.txt'.")
