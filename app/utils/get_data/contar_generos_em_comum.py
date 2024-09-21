import pandas as pd

df = pd.read_excel("app/data/result_API.xlsx")

lista_generos_aux = [generos.split(", ") for generos in df["Subject"].tolist()]

lista_generos = []
for i in lista_generos_aux:
    lista_generos.append([genero.title() for genero in i])


df_final = []


def contar_generos_em_comum(lista_generos, df):
    tamanho = len(lista_generos)
    resultados = []

    for i in range(tamanho):
        titulo1 = df["Título"].iloc[i]
        for j in range(0, tamanho):
            if i == j:
                continue
            titulo2 = df["Título"].iloc[j]
            generos_em_comum = set(lista_generos[i]) & set(lista_generos[j])
            if not generos_em_comum:
                generos_em_comum = ["-"]
                peso = 0
            else:
                peso = len(generos_em_comum)
            resultados.append((f"Lista {i} e Lista {j}", peso, generos_em_comum))
            df_final.append(
                {
                    "Livro 1": titulo1,
                    "Livro 2": titulo2,
                    "Peso": peso,
                    "Gêneros": ", ".join(generos_em_comum),
                }
            )
    df = pd.DataFrame(df_final)
    df.to_excel("app/data/base_pesos.xlsx", index=False)
    return resultados


resultados_comparacao = contar_generos_em_comum(lista_generos, df)

for comparacao, quantidade, generos in resultados_comparacao:
    print(f"{comparacao}: {quantidade} gêneros em comum --> {generos}")
