import requests
import pandas as pd
from loguru import logger


def get_livro(titulo):
    titulo_formatado = titulo.replace(" ", "+")

    url = f"https://openlibrary.org/search.json?title={titulo_formatado}"

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        if "docs" in dados and len(dados["docs"]) > 0:
            livro = dados["docs"][0]
            titulo = livro.get("title", "Não disponível")

            autor = ", ".join(livro.get("author_name", ["Não disponível"]))
            logger.debug(f"AUTOR: {autor}")

            ano = livro.get("first_publish_year", "Não disponível")
            logger.debug(f"ANO: {ano}")

            subject_key = ", ".join(livro.get("subject_key", ["Não disponível"]))
            logger.debug(f"SUBJECT KEY: {subject_key}")

            subject = ", ".join(livro.get("subject", ["Não disponível"]))
            logger.debug(f"SUBJECT: {subject}")

            subject_facet = ", ".join(livro.get("subject_facet", ["Não disponível"]))
            logger.debug(f"SUBJECT FACET: {subject_facet}")

            return {
                "Título": titulo,
                "Autor": autor,
                "Ano de Publicação": ano,
                "Subject": subject,
                "Subject Key": subject_key,
                "Subject Facet": subject_facet,
            }
        else:
            return {
                "Título": titulo,
                "Autor": "Não encontrado",
                "Ano de Publicação": "Não disponível",
                "Subject": "Não disponível",
                "Subject Key": "Não disponível",
                "Subject Facet": "Não disponível",
            }
    else:
        logger.error(f"Erro na requisição: {response.status_code}")
        return None


def processar_livros(arquivo_txt, arquivo_excel):
    lista_livros = []

    with open(arquivo_txt, "r") as file:
        for linha in file:
            titulo = linha.strip()
            if titulo:
                logger.info(f"Buscando livro: {titulo}...")
                dados_livro = get_livro(titulo)
                if dados_livro:
                    lista_livros.append(dados_livro)
                    logger.success(f"Livro adicionado a lista: {titulo}")

    df = pd.DataFrame(lista_livros)

    df.to_excel(arquivo_excel, index=False)
    logger.success(f"Os dados foram salvos no arquivo {arquivo_excel}.")


arquivo_txt = "app/data/livros.txt"
arquivo_excel = "app/data/result_API.xlsx"
processar_livros(arquivo_txt, arquivo_excel)
