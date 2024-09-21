from loguru import logger
from collections import deque

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
        9)	Fazer um método que permita remover um vértice do Grafo (não dirigido e dirigido).
        Não se esqueça de remover as arestas associadas

        ---

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
            f"VÉRTICE {vertice + 1} E TODAS AS ARESTAS ASSOCIADAS FORAM REMOVIDAS (NÃO DIRECIONADO)."
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

            # Lê o número de vértices
            self.vertices = int(linhas[1].strip())
            self.grafo = [[0] * self.vertices for _ in range(self.vertices)]

            # Lê as arestas e os livros
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

            logger.info("GRAFO CARREGADO COM SUCESSO A PARTIR DO ARQUIVO.")

            self.imprimeGrafo()

        except FileNotFoundError:
            logger.error(f"O arquivo {arquivo} não foi encontrado.")
        except Exception as e:
            logger.error(f"Ocorreu um erro ao carregar o grafo: {e}")

    def exibirGrafoVisual(self):
        """
        EXIBE O CONTEÚDO ATUAL DO GRAFO DE FORMA VISUALMENTE COMPREENSÍVEL E ATRAENTE.
        """
        print("---------------------------------------------------------------")
        print(f"Tipo do Grafo: Não Direcionado")
        print(f"Número de Vértices: {self.vertices}")
        print("---------------------------------------------------------------")

        print("Vértices e seus respectivos nomes:")
        for vertice, nome_livro in self.livros.items():
            print(f"- Vértice {vertice}: {nome_livro.replace('"', "")}")

        print("---------------------------------------------------------------")
        print("\nArestas (conexões entre os vértices) e seus respectivos pesos:")
        arestas = []
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):  # Para não repetir arestas
                if self.grafo[i][j] != 0:
                    arestas.append((i + 1, j + 1, self.grafo[i][j]))
                    print(
                        f"- {self.livros[i + 1].replace('"', "")} - {self.livros[self.grafo[i][j]].replace('"', "")} ---> Com peso: {j + 1}"
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
                # Escreve o número estático 2 e o número de vértices
                f.write(f"2\n")
                f.write(f"{self.vertices}\n")

                # Escreve os vértices e seus respectivos nomes
                for vertice, nome_livro in self.livros.items():
                    f.write(f'{vertice} "{nome_livro}"\n')

                # Conta o número de arestas e grava cada uma
                num_arestas = 0
                arestas = []
                for i in range(self.vertices):
                    for j in range(i + 1, self.vertices):
                        if self.grafo[i][j] != 0:
                            num_arestas += 1
                            arestas.append(f"{i} {j} {self.grafo[i][j]}\n")

                # Escreve o número de arestas
                f.write(f"{num_arestas}\n")

                # Escreve cada aresta
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
            visitados[v] = True
            # PERCORRE OS VÉRTICES VIZINHOS DO VÉRTICE ATUAL
            for i in range(self.vertices):
                # SE HÁ UMA ARESTA E O VÉRTICE AINDA NÃO FOI VISITADO, CONTINUA A BUSCA
                if self.grafo[v][i] == 1 and not visitados[i]:
                    busca_profundidade(i)

        # INICIA A BUSCA EM PROFUNDIDADE A PARTIR DO VÉRTICE 0
        busca_profundidade(0)

        # VERIFICA SE TODOS OS VÉRTICES FORAM VISITADOS
        if all(visitados):
            logger.info("GRAFO É CONEXO")
            return 0  # O GRAFO É CONEXO
        else:
            logger.info("GRAFO É DESCONEXO")
            return 1  # O GRAFO É DESCONEXO
    
    def bfs(self, vertice_inicial: int, visitado: list) -> set:
        """
        Realiza uma busca em largura (BFS) a partir de um vértice inicial.
        Retorna o conjunto de vértices que pertencem à mesma componente conectada.
        """
        fila = deque([vertice_inicial])
        visitado[vertice_inicial] = True
        componente = {vertice_inicial}

        while fila:
            v = fila.popleft()

            for i in range(self.vertices):
                if self.grafo[v][i] != 0 and not visitado[i]:
                    fila.append(i)
                    visitado[i] = True
                    componente.add(i)

        return componente

    def componentesConectadas(self) -> list:
        """
        Encontra todas as componentes conectadas do grafo.
        Retorna uma lista de conjuntos, onde cada conjunto representa uma componente conectada.
        """
        visitado = [False] * self.vertices
        componentes = []

        for v in range(self.vertices):
            if not visitado[v]:
                componente = self.bfs(v, visitado)
                componentes.append(componente)

        return componentes

    def grafo_reduzido(self):
        """
        Gera o grafo reduzido com base nas componentes conectadas do grafo original.
        O grafo reduzido contém um vértice para cada componente conectada, e uma aresta
        entre duas componentes se houver pelo menos uma aresta conectando dois vértices de componentes distintas no grafo original.
        """
        
        # Encontra todas as componentes conectadas
        componentes = self.componentesConectadas()
        num_componentes = len(componentes)

        # Cria a matriz de adjacência do grafo reduzido
        grafo_reduzido = [[0] * num_componentes for _ in range(num_componentes)]

        # Mapeamento dos vértices para seus componentes conectados
        vertice_para_componente = {}
        for idx, componente in enumerate(componentes):
            for vertice in componente:
                vertice_para_componente[vertice] = idx

        # Conecta as componentes no grafo reduzido
        for v1 in range(self.vertices):
            for v2 in range(v1 + 1, self.vertices):
                if self.grafo[v1][v2] != 0:
                    comp_v1 = vertice_para_componente[v1]
                    comp_v2 = vertice_para_componente[v2]
                    if comp_v1 != comp_v2:
                        # Aresta entre componentes diferentes no grafo original -> Aresta no grafo reduzido
                        grafo_reduzido[comp_v1][comp_v2] = 1
                        grafo_reduzido[comp_v2][comp_v1] = 1

        # Exibe o grafo reduzido
        logger.info("Grafo reduzido (matriz de adjacência):")
        for linha in grafo_reduzido:
            print(linha)

        return grafo_reduzido
