import pandas as pd

# Load the uploaded Excel file to examine its structure and contents
file_path = "app/aux_data/base_pesos.xlsx"
xls = pd.ExcelFile(file_path)

# Load the data from 'Sheet1'
df = pd.read_excel(file_path, sheet_name="Sheet1")

# Creating the graph file content based on the user's request
grafo_tipo = (
    2  # Based on the description, assuming it's an undirected graph with edge weights
)
vertices = list(set(df["Livro 1"].tolist() + df["Livro 2"].tolist()))  # Unique vertices
vertices_dict = {v: idx for idx, v in enumerate(vertices)}  # Mapping vertex to an index

# Number of vertices (n) and number of edges (m)
n = len(vertices)
m = df.shape[0]

# Prepare the lines for the graph file content
grafo_lines = [f"{grafo_tipo}\n", f"{n}\n"]
for vertex, idx in vertices_dict.items():
    # As per the description, there's no mention of vertex weights, so weight is set as 0.
    grafo_lines.append(f'{idx} "{vertex}"\n')

grafo_lines.append(f"{m}\n")
for _, row in df.iterrows():
    # Fetching vertex indices and edge weight
    v1_idx = vertices_dict[row["Livro 1"]]
    v2_idx = vertices_dict[row["Livro 2"]]
    peso = row["Peso"]
    grafo_lines.append(f"{v1_idx} {v2_idx} {peso}\n")

# Saving the graph data to "grafo.txt"
grafo_file_path = "app/aux_data/grafo_txt_from_excel.txt"
with open(grafo_file_path, "w") as file:
    file.writelines(grafo_lines)
