import sys

from time import sleep
from pathlib import Path

from loguru import logger

DIR_ROOT = str(Path(__file__).parents[1])
sys.path.append(DIR_ROOT)

try:
    from app.utils.classes.grafo_nd import TGrafoND
except ModuleNotFoundError:
    from utils.classes.grafo_nd import TGrafoND


def main(graph_object: TGrafoND):

    while True:

        print(
            """\nEscolha uma das opções abaixo:
1) Ler dados do arquivo grafo.txt
2) Gravar dados no arquivo grafo.txt
3) Inserir vértice
4) Inserir aresta
5) Remover vértice
6) Remover aresta
7) Mostrar conteúdo do arquivo
8) Mostrar grafo
9) Apresentar a conexidade
10) Apresentar o grafo reduzido
11) Sair\n"""
        )

        opcao = input("Digite a opção desejada: ").lower()

        if opcao == "1":
            graph_object.leArquivo(arquivo="app/data/grafo.txt")
        elif opcao == "2":
            graph_object.gravarGrafo(arquivo="app/data/grafo_gravado.txt")
        elif opcao == "3":
            graph_object.insereVertice()
        elif opcao == "4":
            try:
                v1 = int(input("INSIRA O VÉRTICE 1: "))
                v2 = int(input("INSIRA O VÉRTICE 2: "))
                peso = int(input("INSIRA O PESO DA ARESTA: "))
                graph_object.insereAresta(
                    vertice_destino=v1, vertice_origem=v2, peso=peso
                )
                sleep(2)
                graph_object.imprimeGrafo()
            except Exception:
                logger.info("INPUT FORNECIDO INVÁLIDO, TENTE NOVAMENTE!")
                continue
        elif opcao == "5":
            try:
                graph_object.imprimeRelacaoVertices()
                v = int(input("INSIRA O NÚMERO DO VÉRTICE A SER REMOVIDO: "))
                graph_object.removeVertice(vertice=v)
                sleep(2)
                graph_object.imprimeGrafo()
            except Exception:
                logger.info("INPUT FORNECIDO INVÁLIDO, TENTE NOVAMENTE!")
                continue
        elif opcao == "6":
            try:
                v1 = int(input("INSIRA O VÉRTICE 1: "))
                v2 = int(input("INSIRA O VÉRTICE 2: "))
                graph_object.removeAresta(vertice_destino=v1, vertice_origem=v2)
            except Exception:
                logger.info("INPUT FORNECIDO INVÁLIDO, TENTE NOVAMENTE!")
                continue
        elif opcao == "7":
            graph_object.exibirGrafoVisual()
        elif opcao == "8":
            graph_object.imprimeGrafo()
        elif opcao == "9":
            graph_object.tipo_conexidade()
        elif opcao == "10":
            graph_object.grafo_reduzido()
        elif opcao == "11":
            logger.info("Saindo...")
            break
        else:
            logger.error("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    book_graph = TGrafoND()
    main(graph_object=book_graph)
