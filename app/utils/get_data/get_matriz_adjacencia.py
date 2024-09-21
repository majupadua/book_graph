import pandas as pd
import numpy as np

df = pd.read_excel("app/data/base_pesos.xlsx")

livros = pd.concat([df["Livro 1"], df["Livro 2"]]).unique()

livro_idx = {livro: idx for idx, livro in enumerate(livros)}

n = len(livros)
matriz_adjacencia = np.zeros((n, n), dtype=int)

for _, row in df.iterrows():
    livro1, livro2, peso = row["Livro 1"], row["Livro 2"], int(row["Peso"])
    idx1, idx2 = livro_idx[livro1], livro_idx[livro2]
    matriz_adjacencia[idx1, idx2] = peso
    matriz_adjacencia[idx2, idx1] = peso

with open("app/data/matriz_adjacencia.txt", "w") as f:
    for linha in matriz_adjacencia:
        linha_txt = ", ".join(map(str, linha))
        f.write(linha_txt + "\n")

print("Matriz de adjacência com pesos salva em 'app/data/matriz_adjacencia.txt'.")
