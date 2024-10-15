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
from collections import defaultdict
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
        self.grafo = defaultdict(list)
        self.livros = {}

    def imprimeGrafo(self):
        """
        EXIBE A MATRIZ DE ADJACÊNCIA DO GRAFO.
        """

        if self.grafo:
            logger.info("A LISTA DE ADJACÊNCIA É:")
            for vertice, vizinhos in self.grafo.items():
                vizinhos_str = " -> ".join([f"{v} (peso {p})" for v, p in vizinhos])
                print(f"{vertice}: {vizinhos_str}")
        else:
            logger.info("A LISTA DE ADJACÊNCIA AINDA NÃO FOI CRIADA!")

    def imprimeRelacaoVertices(self):
        """
        EXIBE OS VÉRTICES E OS SEUS RESPECTIVOS NOMES
        """

        logger.info("VÉRTICES E NOMES DOS LIVROS:")
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
            self.grafo[vertice_origem].append((vertice_destino, peso))
            self.grafo[vertice_destino].append((vertice_origem, peso))
            logger.info(f"ARESTA INSERIDA ENTRE {vertice_origem} E {vertice_destino} COM PESO {peso}.")
            
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
        self.grafo[vertice_origem] = [
            (v, p) for v, p in self.grafo[vertice_origem] if v != vertice_destino
        ]
        self.grafo[vertice_destino] = [
            (v, p) for v, p in self.grafo[vertice_destino] if v != vertice_origem
        ]
        logger.info(f"ARESTA REMOVIDA ENTRE {vertice_origem} E {vertice_destino}.")


    def insereVertice(self, nome_livro: str):
        """
        INSERE UM NOVO VÉRTICE NO GRAFO.
        """

        self.livros[self.vertices] = nome_livro
        logger.info(f"VÉRTICE {self.vertices} - '{nome_livro}' INSERIDO.")
        self.vertices += 1

        self.imprimeGrafo()
        logger.info(f"VÉRTICE {self.vertices-1} INSERIDO COM SUCESSO.")

    def removeVertice(self, vertice: int):
        """
        REMOVE UM VÉRTICE DE UM GRAFO NÃO-DIRECIONADO E TODAS AS ARESTAS ASSOCIADAS.

        Args:
            vertice (int): O ÍNDICE DO VÉRTICE A SER REMOVIDO (1-INDEXADO).
        """

        if vertice in self.grafo:
            del self.grafo[vertice]  # Remove o vértice da lista de adjacência
        for vizinhos in self.grafo.values():
            vizinhos[:] = [(v, p) for v, p in vizinhos if v != vertice]
        self.livros.pop(vertice, None)
        self.vertices -= 1
        logger.success(f"VÉRTICE {vertice} REMOVIDO.")

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
            for linha in linhas[2:self.vertices + 2]:
                vertice, nome_livro = linha.strip().split(' "')
                self.livros[int(vertice)] = nome_livro

            for linha in linhas[self.vertices + 3:]:
                origem, destino, peso = map(int, linha.split())
                self.insereAresta(origem, destino, peso)

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
            print(f"- Vértice {vertice}: {repr(nome_livro)}")


        print("---------------------------------------------------------------")
        print("\nArestas (conexões entre os vértices) e seus respectivos pesos:")
        arestas = set()
        for origem, vizinhos in self.grafo.items():
            for destino, peso in vizinhos:
                if (destino, origem, peso) not in arestas:  # Evitar duplicatas
                    arestas.add((origem, destino, peso))
                    print(
                        f"- {self.livros[origem]} - {self.livros[destino]} ---> Com peso: {peso}"
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
                    nome_formatado = nome_livro.translate(str.maketrans('', '', '"'))
                    f.write(f'{vertice} "{nome_formatado}"\n')


                
                arestas = set()  # Evita duplicatas
                for origem, vizinhos in self.grafo.items():
                    for destino, peso in vizinhos:
                        if (destino, origem, peso) not in arestas:
                            arestas.add((origem, destino, peso))

                f.write(f"{len(arestas)}\n") 

                for origem, destino, peso in arestas:
                    f.write(f"{origem} {destino} {peso}\n")

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
        visitados = set()

        def busca_profundidade(v: int):
            """
            REALIZA A BUSCA EM PROFUNDIDADE (DFS) A PARTIR DE UM VÉRTICE.

            Args:
                v (int): O ÍNDICE DO VÉRTICE DE PARTIDA PARA A BUSCA EM PROFUNDIDADE.
            """
            visitados.add(v)
            for vizinho, _ in self.grafo[v]:
                if vizinho not in visitados:
                    busca_profundidade(vizinho)

        # INICIA A BUSCA EM PROFUNDIDADE A PARTIR DO VÉRTICE 0
        busca_profundidade(0)

        # VERIFICA SE TODOS OS VÉRTICES FORAM VISITADOS
        if len(visitados) == self.vertices:
            logger.info("O GRAFO É CONEXO.")
            return 0
        else:
            logger.info("O GRAFO É DESCONEXO.")
            return 1

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

