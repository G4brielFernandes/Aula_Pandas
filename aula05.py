import pandas as pd 

df = pd.read_csv('dados.limpos.csv')
df = df.rename(columns={"DATA FINAL": "ANO"})
df["ANO"] = pd.to_datetime(df["ANO"], errors="coerce").dt.year

# Qual a quantidade de Registros de cada produto em cada região
x = df.groupby(['PRODUTO','REGIÃO'])
x['NÚMERO DE POSTOS PESQUISADOS'].count()

# Como os preços da Gasolina Comum variaram em 2018 
filtro = (df['PRODUTO'] == 'GASOLINA COMUM') & (df['ANO'] == 2018)
df_filtrado = df.loc[filtro]
df_filtrado
desvio = df_filtrado['PREÇO MÉDIO REVENDA'].describe().to_frame()
desvio
df['PRODUTO'].value_counts()
# Como os preços da Gasolina Comum e Etanol no São Paulo variaram em 2017 
x = df.query('PRODUTO in ["GASOLINA COMUM" , "ETANOL HIDRATADO"] and ESTADO == "CEARA" and ANO == 2018')
x['PREÇO MÉDIO REVENDA'].describe().to_frame()
x.groupby('PRODUTO')['PREÇO MÉDIO REVENDA'].describe()