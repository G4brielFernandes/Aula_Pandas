import pandas as pd

# Lê o CSV que foi salvo antes
df = pd.read_csv('copia_dados.csv')

# Mostra os estados únicos da coluna ESTADO
df['ESTADO'].unique()

# Cria um filtro simples (estado == CEARA)
x = df['ESTADO'] == 'CEARA'
df[x]

# Filtra por CEARA usando query e reseta o índice
estado_ce = df.query('ESTADO == "CEARA"').reset_index(drop=True)
estado_ce

# Filtro composto: estado CEARA e preço > 2.0
filto1 = df['ESTADO'] == 'CEARA'
df_filtado = df[filto1]
filtro2 = df_filtado['PREÇO MÉDIO REVENDA'] > 2.0
df_filtado = df_filtado[filtro2]
df_filtado

# Retorna uma série booleana (se cada linha tem preço > 2.0)
df['PREÇO MÉDIO REVENDA'] > 2.0

# Filtro múltiplo: CEARA ou (PARA e preço > 2.0)
filtro = (df['ESTADO'] == 'CEARA') | (df['ESTADO'] == 'PARA') & (df['PREÇO MÉDIO REVENDA'] > 2.0)
df[filtro]

# Mesmo filtro com query (mais legível)
df.query('ESTADO == "CEARA" or ESTADO == "PARA"')

# Filtro ainda mais específico: 
# (estado CEARA ou PARA) E preço > 2 E produto == GASOLINA COMUM
selc1 = (df['ESTADO'] == 'CEARA') | (df['ESTADO'] == 'PARA')
selc2 = (df['PREÇO MÉDIO REVENDA'] > 2)
selc3 = (df['PRODUTO'] == 'GASOLINA COMUM')
filtro = selc1 & selc2 & selc3
x = df[filtro]
x['ESTADO'].unique() 

df.head()

# Filtra usando lista de produtos (isin)
lista_produtos = ['GASOLINA COMUM','ETANOL HIDRATADO']
x = df['PRODUTO'].isin(lista_produtos)
df_x = df[x]   
df_x['PRODUTO'].unique()

df.head()

# Itera sobre as 5 primeiras linhas, acessa o valor de PREÇO MÉDIO REVENDA
# multiplica por 10 e imprime com o índice
for i, c in df.head(5).iterrows():
    x = c['PREÇO MÉDIO REVENDA'] * 10
    print(f"esse é o index - {i} essa é a coluna {x}")


