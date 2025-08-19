# def muita(x):
#     r = x ** 2
#     final = r / 10
#     return final

# lista = list(range(10))
# lista_quarado = list(map(lambda x: x ** 2, lista))
# lista_muita_coisa = list(map(muita, lista))
# lista_quarado
# lista_muita_coisa
import pandas as pd 

# Lê o arquivo dado.tsv usando separador de tabulação (\t)
df = pd.read_csv('dado.tsv', sep='\t')
df.head(10)  
df.info()    

# Cria DataFrame manual com nomes, idades e booleano
df_nomes = pd.DataFrame({
    'nome': ['Carlos', 'Ricardo', 'Gablriela', 'Rachador'],
    'idade': [12, 23, 43, None],
    'menino': [True, True, False, True],
})
df_nomes.shape      # retorna quantidade de linhas e colunas
df_nomes.columns    # retorna os nomes das colunas

# Troca os nomes das colunas (linha rename não altera sem atribuição, 
# já esta força a troca)
df_nomes.columns = ['Jaja', 'RIRI', 'ZWEZ']
df_nomes

# Cria uma Series (1 dimensão) com índices personalizados
pd.Series([24,23,12], index=['prova1', 'prova2', 'prova3'])

# Cria lista de novos produtos baseada no número de linhas do df
nlinha, ncolunas = df.shape
novos_produtos = [f'Produto{i}' for i in range(nlinha)]
df['PRODUTO'] = novos_produtos   # adiciona coluna no df
df.head()

# Cria DataFrame "consoles" com notas de avaliação
consoles = pd.DataFrame({
    'Bom': [10, 20 , 15],
    'Ruim': [4, 13, 9],
    'Pessimo': [7, 5, 3],
}, index=['PlayStaion', 'Xbox', 'Nitendo'])
consoles.index   # mostra índice

# Exemplos de seleção de dados com iloc/loc
df.iloc[0:20:5, 0:3]      # fatia linhas/colunas por posição
df.iloc[0,3]              # seleciona célula específica
consoles.iloc[2]          # linha pelo índice numérico
consoles.loc['Xbox']      # linha pelo rótulo
consoles.loc[['Xbox', 'Nitendo'], ['Ruim']]  # fatia linhas e colunas
consoles.iloc[0:, [0, 2]] # todas as linhas, colunas 0 e 2
consoles[['Bom', 'Pessimo']]                  # seleciona colunas pelo nome
df[['REGIÃO','PRODUTO','ESTADO']]             # seleciona colunas do df

# Faz cópia do df, remove coluna e exporta para CSV
copia_df = df.copy()
del copia_df['PRODUTO']
df.to_csv('copia_dados.csv', index=False, sep=';')