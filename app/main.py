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

        # EXIBE O MENU DE OPÇÕES PARA O USUÁRIO
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

        # RECEBE A OPÇÃO ESCOLHIDA PELO USUÁRIO
        opcao = input("Digite a opção desejada: ").lower()

        # LER DADOS DO ARQUIVO
        if opcao == "1":
            graph_object.leArquivo(arquivo="app/data/grafo.txt")

        # GRAVAR DADOS NO ARQUIVO
        elif opcao == "2":
            graph_object.gravarGrafo(arquivo="app/data/grafo_gravado.txt")

        # INSERIR UM VÉRTICE
        elif opcao == "3":
            graph_object.insereVertice()

        # INSERIR UMA ARESTA
        elif opcao == "4":
            try:
                # SOLICITA AO USUÁRIO AS INFORMAÇÕES NECESSÁRIAS PARA A INSERÇÃO DA ARESTA
                v1 = int(input("INSIRA O VÉRTICE 1: "))
                v2 = int(input("INSIRA O VÉRTICE 2: "))
                peso = int(input("INSIRA O PESO DA ARESTA: "))

                # CHAMA A FUNÇÃO PARA INSERIR A ARESTA COM OS PARÂMETROS RECEBIDOS
                graph_object.insereAresta(
                    vertice_destino=v1, vertice_origem=v2, peso=peso
                )
                sleep(2)
                graph_object.imprimeGrafo()  # IMPRIME O GRAFO ATUALIZADO
            except Exception:
                logger.info(
                    "INPUT FORNECIDO INVÁLIDO, TENTE NOVAMENTE!"
                )  # MENSAGEM DE ERRO CASO OS DADOS ESTEJAM INCORRETOS
                continue  # VOLTA AO MENU PRINCIPAL

        # REMOVER UM VÉRTICE
        elif opcao == "5":
            try:
                graph_object.imprimeRelacaoVertices()  # EXIBE A RELAÇÃO DE VÉRTICES EXISTENTES
                v = int(input("INSIRA O NÚMERO DO VÉRTICE A SER REMOVIDO: "))

                # REMOVE O VÉRTICE SELECIONADO
                graph_object.removeVertice(vertice=v)
                sleep(2)
                graph_object.imprimeGrafo()  # IMPRIME O GRAFO ATUALIZADO
            except Exception:
                logger.info("INPUT FORNECIDO INVÁLIDO, TENTE NOVAMENTE!")
                continue  # VOLTA AO MENU PRINCIPAL

        # REMOVER UMA ARESTA
        elif opcao == "6":
            try:
                # SOLICITA AO USUÁRIO AS INFORMAÇÕES DOS VÉRTICES DA ARESTA A SER REMOVIDA
                v1 = int(input("INSIRA O VÉRTICE 1: "))
                v2 = int(input("INSIRA O VÉRTICE 2: "))
                # CHAMA A FUNÇÃO PARA REMOVER A ARESTA
                graph_object.removeAresta(vertice_destino=v1, vertice_origem=v2)
            except Exception:
                logger.info("INPUT FORNECIDO INVÁLIDO, TENTE NOVAMENTE!")
                continue  # VOLTA AO MENU PRINCIPAL

        # MOSTRAR CONTEÚDO DO ARQUIVO GRAFO.TXT
        elif opcao == "7":
            graph_object.exibirGrafoVisual()

        # MOSTRAR O GRAFO ATUAL
        elif opcao == "8":
            graph_object.imprimeGrafo()

        # APRESENTAR A CONEXIDADE DO GRAFO
        elif opcao == "9":
            graph_object.tipo_conexidade()

        # APRESENTAR O GRAFO REDUZIDO
        elif opcao == "10":
            graph_object.grafo_reduzido()

        # SAIR DO PROGRAMA
        elif opcao == "11":
            logger.info("Saindo...")
            break

        # CASO A OPÇÃO SEJA INVÁLIDA
        else:
            logger.error("Opção inválida. Tente novamente.")


if __name__ == "__main__":

    # CRIA UM OBJETO DA CLASSE TGrafoND
    book_graph = TGrafoND()

    # INICIA O MENU PRINCIPAL PASSANDO O OBJETO GRAFO COMO PARÂMETRO
    main(graph_object=book_graph)
