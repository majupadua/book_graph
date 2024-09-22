"""
Biblioteca Conectada: Explorando Relações entre Livros

Membros do Grupo:
1. Gabriella Silveira Braz - 10402554
2. Giovana Liao - 10402264
3. Maria Julia de Pádua - 10400630

Síntese do Conteúdo:
A classe `TGrafoND` implementa um grafo não dirigido utilizando uma matriz 
de adjacência, onde os vértices representam livros e as arestas representam 
relações entre eles, com pesos que podem indicar similaridade ou conexão. 
A classe inclui métodos para manipulação do grafo, como a inserção e remoção 
de vértices e arestas, leitura de dados de um arquivo, e exibição da matriz de 
adjacência. Também possui funcionalidades para verificar a conectividade do grafo, 
utilizando busca em profundidade e em largura, e para identificar e exibir as 
componentes conectadas. Por fim, é capaz de gerar um grafo reduzido que representa 
as componentes conectadas do grafo original, mostrando como as diferentes partes 
do grafo estão interligadas.
"""

from collections import deque

from loguru import logger

class TGrafoND:
    def __init__(self):
        """
        INICIALIZA O GRAFO COM UMA MATRIZ DE ADJACÊNCIA
        DE TAMANHO `VERTICES` x `VERTICES`.

        Args:
            vertices (int): NÚMERO DE VÉRTICES DO GRAFO.
        """

        # INICIALIZA O NÚMERO DE VÉRTICES
        self.vertices = 0
        # CRIA A MATRIZ DE ADJACÊNCIA COM TODOS OS VALORES INICIALIZADOS EM 0
        self.grafo = []
        self.livros = {}

    def imprimeGrafo(self):
        """
        EXIBE A MATRIZ DE ADJACÊNCIA DO GRAFO.
        """

        if self.grafo:
            logger.info("A MATRIZ DE ADJACÊNCIA É: ")
            print(f"\n{'     ':^2}" + f" ".join([f"{i:^2}" for i in range(self.vertices)]))
            print(f"{'     ':^2}" + f" ".join([f"{'-':^2}" for _ in range(self.vertices)]))
            for i in range(self.vertices):
                aux = []
                for peso in self.grafo[i]:
                    aux.append(f"{str(peso):^2}")
                print(f"{i:^2} | {' '.join(aux)}")
        else:
            logger.info("A MATRIZ DE ADJACÊNCIA AINDA NÃO FOI CRIADA! LEIA UM ARQUIVO OU ADICIONE VÉRTICES E ARESTAS!")



    def imprimeRelacaoVertices(self):
        """
        EXIBE A MATRIZ DE ADJACÊNCIA DO GRAFO.
        """

        logger.info("A MATRIZ DE ADJACÊNCIA É: ")
        for num, nome in self.livros.items():
            print(f"{num} --> {nome}")

    def insereAresta(self, vertice_origem: int, vertice_destino: int, peso: int = 1):
        """
        INSERE UMA ARESTA ENTRE OS VÉRTICES U E V EM UM GRAFO NÃO-DIRIGIDO.

        Args:
            vertice_origem (int): O ÍNDICE DO VÉRTICE DE ORIGEM (1-INDEXADO).
            vertice_destino (int): O ÍNDICE DO VÉRTICE DE DESTINO (1-INDEXADO).
            peso (int): O PESO DA ARESTA.
        """

        try:
            # ADICIONA UMA ARESTA ENTRE U E V (NÃO DIRIGIDO)
            self.grafo[vertice_origem][vertice_destino] = peso
            self.grafo[vertice_destino][vertice_origem] = peso
            
            # INFORMA A INSERÇÃO E MOSTRA A MATRIZ DE ADJACÊNCIA ATUALIZADA
            logger.info(
                f"ARESTA INSERIDA ENTRE OS VÉRTICES {vertice_origem} E {vertice_destino} COM PESO {peso}."
            )
        except Exception:
            logger.error(
                f"ERRO AO INSERIR ARESTA ENTRE OS VÉRTICES {vertice_origem} E {vertice_destino}."
            )


    def removeAresta(self, vertice_origem: int, vertice_destino: int):
        """
        REMOVE A ARESTA ENTRE OS VÉRTICES U E V EM UM GRAFO NÃO-DIRIGIDO E EXIBE A MATRIZ RESULTANTE.

        Args:
            vertice_origem (int): O ÍNDICE DO VÉRTICE DE ORIGEM (1-INDEXADO).
            vertice_destino (int): O ÍNDICE DO VÉRTICE DE DESTINO (1-INDEXADO).
        """

        # REMOVE A ARESTA ENTRE U E V (NÃO DIRIGIDO)
        self.grafo[vertice_origem][vertice_destino] = 0
        self.grafo[vertice_destino][vertice_origem] = 0

        # INFORMA A REMOÇÃO E MOSTRA A MATRIZ DE ADJACÊNCIA ATUALIZADA
        logger.info(
            f"ARESTA REMOVIDA ENTRE OS VÉRTICES {vertice_origem} E {vertice_destino}."
        )

    def insereVertice(self):
        """
        INSERE UM NOVO VÉRTICE NO GRAFO.
        """

        # ADICIONA UMA NOVA LINHA E COLUNA COM 0 PARA A NOVA MATRIZ DE ADJACÊNCIA
        for i in range(self.vertices):
            self.grafo[i].append(0)
        self.grafo.append([0] * self.vertices)

        self.vertices += 1

        self.imprimeGrafo()
        logger.info(f"VÉRTICE {self.vertices-1} INSERIDO COM SUCESSO.")

    def removeVertice(self, vertice: int):
        """
        REMOVE UM VÉRTICE DE UM GRAFO NÃO-DIRECIONADO E TODAS AS ARESTAS ASSOCIADAS.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE A SER REMOVIDO (1-INDEXADO).
        """

        # REMOVE A LINHA DO VÉRTICE
        self.grafo.pop(vertice)

        # REMOVE A COLUNA DO VÉRTICE EM CADA LINHA RESTANTE
        for i in range(len(self.grafo)):
            self.grafo[i].pop(vertice)

        # ATUALIZAR O NÚMERO DE VÉRTICES
        self.vertices -= 1

        # INFORMA A REMOÇÃO E MOSTRA A MATRIZ DE ADJACÊNCIA ATUALIZADA
        logger.success(
            f"VÉRTICE {vertice + 1} E TODAS AS ARESTAS ASSOCIADAS FORAM REMOVIDAS."
        )

    def leArquivo(self, arquivo: str):
        """
        CARREGA O GRAFO A PARTIR DE UM ARQUIVO TXT E SALVA OS NOMES DOS LIVROS.

        Args:
            arquivo (str): O CAMINHO DO ARQUIVO TXT QUE CONTÉM OS DADOS DO GRAFO.
        """
        try:
            with open(arquivo, "r") as f:
                linhas = f.readlines()

            self.vertices = int(linhas[1].strip())
            self.grafo = [[0] * self.vertices for _ in range(self.vertices)]

            for linha in linhas[2 : self.vertices + 2]:
                dados = linha.strip().split(' "')
                if len(dados) >= 2:
                    vertice = int(dados[0])
                    nome_livro = dados[1]
                    self.livros[vertice] = nome_livro

            for linha in linhas[self.vertices + 3 :]:
                dados = linha.strip().split(" ")
                vertice_origem, vertice_destino, peso = (
                    int(dados[0]),
                    int(dados[1]),
                    int(dados[2]),
                )
                self.insereAresta(vertice_origem, vertice_destino, peso)

            logger.success("GRAFO CARREGADO COM SUCESSO A PARTIR DO ARQUIVO.")

            self.imprimeGrafo()

        except FileNotFoundError:
            logger.error(f"O arquivo {arquivo} não foi encontrado.")
        except Exception as e:
            logger.error(f"Ocorreu um erro ao carregar o grafo: {e}")

    def exibirGrafoVisual(self):
        """
        EXIBE O CONTEÚDO ATUAL DO GRAFO DE FORMA VISUALMENTE COMPREENSÍVEL E ATRAENTE.
        """

        print("===============================================================")
        print(f"Tipo do Grafo: Não Orientado com peso nas arestas")
        print(f"Número de Vértices: {self.vertices}")
        print("---------------------------------------------------------------")

        print("Vértices e seus respectivos nomes:")
        for vertice, nome_livro in self.livros.items():
            print(f"- Vértice {vertice}: {nome_livro.replace('"', "")}")

        print("---------------------------------------------------------------")
        print("\nArestas (conexões entre os vértices) e seus respectivos pesos:")
        arestas = []
        for i in range(self.vertices-1):
            for j in range(i + 1, self.vertices-1):  # Para não repetir arestas
                if self.grafo[i][j] != 0:
                    arestas.append((i + 1, j + 1, self.grafo[i][j]))
                    print(
                        f"- {self.livros[i + 1]} - {self.livros[j]} ---> Com peso: {j + 1}"
                    )

        if not arestas:
            print("Não há arestas neste grafo.")

        print("===============================================================")

    def gravarGrafo(self, arquivo: str):
        """
        GRAVA O GRAFO EM UM ARQUIVO TXT NO FORMATO ESPECIFICADO.

        Args:
            arquivo (str): O CAMINHO DO ARQUIVO TXT A SER GRAVADO.
        """
        try:
            with open(arquivo, 'w') as f:
                f.write(f"2\n")
                f.write(f"{self.vertices}\n")

                for vertice, nome_livro in self.livros.items():
                    f.write(f'{vertice} "{nome_livro.replace('"', "")}"\n')

                num_arestas = 0
                arestas = []
                for i in range(self.vertices):
                    for j in range(i + 1, self.vertices):
                        if self.grafo[i][j] != 0:
                            num_arestas += 1
                            arestas.append(f"{i} {j} {self.grafo[i][j]}\n")

                f.write(f"{num_arestas}\n")

                for aresta in arestas:
                    f.write(aresta)

            logger.info(f"GRAFO GRAVADO COM SUCESSO NO ARQUIVO {arquivo}.")
        except Exception as e:
            logger.error(f"Ocorreu um erro ao gravar o grafo: {e}")

    def tipo_conexidade(self) -> int:
        """

        VERIFICA O TIPO DE CONEXIDADE DE UM GRAFO NÃO DIRECIONADO.

        Returns:
            int: RETORNA 0 SE O GRAFO É CONEXO E 1 SE O GRAFO É DESCONEXO.
        """

        # LISTA PARA MARCAR OS VÉRTICES VISITADOS
        visitados = [False] * self.vertices

        def busca_profundidade(v: int):
            """
            REALIZA A BUSCA EM PROFUNDIDADE (DFS) A PARTIR DE UM VÉRTICE.

            Args:
                v (int): O ÍNDICE DO VÉRTICE DE PARTIDA PARA A BUSCA EM PROFUNDIDADE.
            """
            visitados[v] = True  # MARCA O VÉRTICE ATUAL COMO VISITADO
            # PERCORRE OS VÉRTICES VIZINHOS DO VÉRTICE ATUAL
            for i in range(self.vertices):
                # SE HÁ UMA ARESTA E O VÉRTICE AINDA NÃO FOI VISITADO, CONTINUA A BUSCA
                if self.grafo[v][i] == 1 and not visitados[i]:
                    busca_profundidade(i)  # CHAMA A FUNÇÃO RECURSIVAMENTE PARA O VIZINHO

        # INICIA A BUSCA EM PROFUNDIDADE A PARTIR DO VÉRTICE 0
        busca_profundidade(0)

        # VERIFICA SE TODOS OS VÉRTICES FORAM VISITADOS
        if all(visitados):
            logger.info("GRAFO É CONEXO")  # MENSAGEM DE QUE O GRAFO É CONEXO
            return 0  # O GRAFO É CONEXO
        else:
            logger.info("GRAFO É DESCONEXO")  # MENSAGEM DE QUE O GRAFO É DESCONEXO
            return 1  # O GRAFO É DESCONEXO

    def bfs(self, vertice_inicial: int, visitado: list) -> set:
        """
        REALIZA UMA BUSCA EM LARGURA (BFS) A PARTIR DE UM VÉRTICE INICIAL.
        RETORNA O CONJUNTO DE VÉRTICES QUE PERTENCEM À MESMA COMPONENTE CONECTADA.

        Args:
            vertice_inicial (int): O VÉRTICE DE PARTIDA PARA A BUSCA EM LARGURA.
            visitado (list): LISTA QUE CONTROLA OS VÉRTICES VISITADOS.

        Returns:
            set: CONJUNTO DE VÉRTICES DA COMPONENTE CONECTADA.
        """
        fila = deque([vertice_inicial])  # INICIA A FILA COM O VÉRTICE INICIAL
        visitado[vertice_inicial] = True  # MARCA O VÉRTICE INICIAL COMO VISITADO
        componente = {vertice_inicial}  # INICIALIZA O CONJUNTO DA COMPONENTE

        while fila:  # ENQUANTO HOUVER VÉRTICES NA FILA
            v = fila.popleft()  # REMOVE O VÉRTICE DO INÍCIO DA FILA

            for i in range(self.vertices):
                if self.grafo[v][i] != 0 and not visitado[i]:  # SE HÁ UMA ARESTA E O VIZINHO NÃO FOI VISITADO
                    fila.append(i)  # ADICIONA O VIZINHO À FILA
                    visitado[i] = True  # MARCA O VIZINHO COMO VISITADO
                    componente.add(i)  # ADICIONA O VIZINHO À COMPONENTE

        return componente  # RETORNA O CONJUNTO DE VÉRTICES DA COMPONENTE

    def componentesConectadas(self) -> list:
        """
        ENCONTRA TODAS AS COMPONENTES CONECTADAS DO GRAFO.
        RETORNA UMA LISTA DE CONJUNTOS, ONDE CADA CONJUNTO REPRESENTA UMA COMPONENTE CONECTADA.

        Returns:
            list: LISTA DE COMPONENTES CONECTADAS.
        """
        visitado = [False] * self.vertices  # INICIALIZA A LISTA DE VISITADOS
        componentes = []  # LISTA PARA ARMAZENAR AS COMPONENTES ENCONTRADAS

        for v in range(self.vertices):
            if not visitado[v]:  # SE O VÉRTICE AINDA NÃO FOI VISITADO
                componente = self.bfs(v, visitado)  # REALIZA A BUSCA EM LARGURA
                componentes.append(componente)  # ADICIONA A COMPONENTE À LISTA

        return componentes  # RETORNA A LISTA DE COMPONENTES CONECTADAS


    def grafo_reduzido(self):
        """
        GERA O GRAFO REDUZIDO COM BASE NAS COMPONENTES CONECTADAS DO GRAFO ORIGINAL.
        O GRAFO REDUZIDO CONTÉM UM VÉRTICE PARA CADA COMPONENTE CONECTADA, E UMA ARESTA
        ENTRE DUAS COMPONENTES SE HOUVER PELO MENOS UMA ARESTA CONECTANDO DOIS VÉRTICES DE COMPONENTES DISTINTAS NO GRAFO ORIGINAL.
        """
        
        # ENCONTRA TODAS AS COMPONENTES CONECTADAS
        componentes = self.componentesConectadas()
        num_componentes = len(componentes)

        # CRIA A MATRIZ DE ADJACÊNCIA DO GRAFO REDUZIDO
        grafo_reduzido = [[0] * num_componentes for _ in range(num_componentes)]

        # MAPEAMENTO DOS VÉRTICES PARA SEUS COMPONENTES CONECTADOS
        vertice_para_componente = {}
        for idx, componente in enumerate(componentes):
            for vertice in componente:
                vertice_para_componente[vertice] = idx

        # CONECTA AS COMPONENTES NO GRAFO REDUZIDO
        for v1 in range(self.vertices):
            for v2 in range(v1 + 1, self.vertices):
                if self.grafo[v1][v2] != 0:  # VERIFICA SE EXISTE UMA ARESTA ENTRE v1 E v2
                    comp_v1 = vertice_para_componente[v1]  # OBTÉM A COMPONENTE DE v1
                    comp_v2 = vertice_para_componente[v2]  # OBTÉM A COMPONENTE DE v2
                    if comp_v1 != comp_v2:  # SE AS COMPONENTES FOREM DIFERENTES
                        # ARESTA ENTRE COMPONENTES DIFERENTES NO GRAFO ORIGINAL -> ARESTA NO GRAFO REDUZIDO
                        grafo_reduzido[comp_v1][comp_v2] = 1
                        grafo_reduzido[comp_v2][comp_v1] = 1

        # EXIBE O GRAFO REDUZIDO
        logger.info("GRAFO REDUZIDO:")
        for linha in grafo_reduzido:
            print(linha)

        return grafo_reduzido  # RETORNA A MATRIZ DE ADJACÊNCIA DO GRAFO REDUZIDO

