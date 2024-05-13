import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Carregar os dados do CSV a partir da URL
url = "https://raw.githubusercontent.com/carsonmars/plot-visualizacao-info/main/dataset/pgepe-anos.csv"
dados = pd.read_csv(url)

# Renomear as colunas para corresponderem ao esperado no código
dados.rename(columns={'ANOS': 'Ano', 'VALORES': 'Quantidade'}, inplace=True)

# Remover caracteres não numéricos e converter a coluna 'Quantidade' para float
dados['Quantidade'] = dados['Quantidade'].str.replace('[^\d,]', '', regex=True).str.replace(',', '.').astype(float)

# Definir cores para as barras
cores = plt.cm.viridis(np.linspace(0, 1, len(dados)))

# Função para formatar os ticks do eixo y
def bilhoes(x, pos):
    return f'R$ {x / 1e9:.1f} Bi'

# Plotar o gráfico em barras
plt.figure(figsize=(10, 6))
for i in range(len(dados)):
    plt.bar(dados['Ano'][i], dados['Quantidade'][i], color=cores[i])
plt.xlabel('Ano')
plt.ylabel('Valor (R$)')
plt.title('CUSTO EM R$ PGE PE POR ANO')
plt.xticks(rotation=45)

# Aplicar o formato de bilhões ao eixo y
formatter = FuncFormatter(bilhoes)
plt.gca().yaxis.set_major_formatter(formatter)

# Definir os limites do eixo y manualmente
plt.ylim(0, dados['Quantidade'].max() * 1.1)  # Ajustar o fator de 1.1 conforme necessário

plt.tight_layout()
plt.show()
