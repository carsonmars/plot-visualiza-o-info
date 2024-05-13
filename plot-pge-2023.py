import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do CSV
url = "https://raw.githubusercontent.com/carsonmars/plot-visualizacao-info/main/dataset/pge-2023.csv"
df = pd.read_csv(url)

# Renomear as colunas para correspondência com o DataFrame
df.columns = ['Meses', 'Valores']

# Converter o formato dos números
df['Valores'] = df['Valores'].str.replace(',', '').astype(float)

# Definir os nomes dos meses como rótulos de x
meses = df['Meses'].tolist()

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Valores'], marker='o', linestyle='-')
plt.title('Custo PGE 2023')
plt.xlabel('')
plt.ylabel('Valor (R$ milhões)')
plt.grid(True)
plt.xticks(df.index, meses, rotation=45)
plt.tight_layout()
plt.show()
