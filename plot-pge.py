import pandas as pd
import matplotlib.pyplot as plt
import squarify

# URL do arquivo CSV no GitHub
url = 'https://raw.githubusercontent.com/carsonmars/plot-visualizacao-info/main/dataset/remuneracao_13052024.csv'

# Carregar os dados do CSV
df = pd.read_csv(url)

# Contagem das categorias de servidores
categoria_counts = df['Categoria'].value_counts()

# Cores para as categorias de servidores
cores = plt.cm.tab20.colors[:len(categoria_counts)]

# Criar o treemap
plt.figure(figsize=(10, 8))
squarify.plot(sizes=categoria_counts.values, label=categoria_counts.index, color=cores, alpha=0.7)

# Adicionar título
plt.title('TIPO DE SERVIDORES DA PROCURADORIA GERAL DO ESTADO DE PERNAMBUCO')

# Remover eixos
plt.axis('off')

# Exibir o treemap
plt.show()
