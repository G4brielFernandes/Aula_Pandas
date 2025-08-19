import pandas as pd

# Carrega os dados e faz um backup
df = pd.read_csv('copia_dados.csv') 
df_backup = df.copy()

# Converte colunas de data
df['DATA INICIAL'] = pd.to_datetime(df['DATA INICIAL'])
df['DATA FINAL'] = pd.to_datetime(df['DATA FINAL'])
df.info()

# Lista de colunas numéricas
lin = [
 'MARGEM MÉDIA REVENDA', 
 'PREÇO MÉDIO DISTRIBUIÇÃO', 
 'DESVIO PADRÃO DISTRIBUIÇÃO',
 'PREÇO MÍNIMO DISTRIBUIÇÃO',
 'PREÇO MÁXIMO DISTRIBUIÇÃO',
]

# Converte colunas para numérico, forçando erro como NaN
for i in lin:
    df[i] = pd.to_numeric(df[i], errors="coerce")
df.info()

# Verifica nulos
df['MARGEM MÉDIA REVENDA'].isnull().sum()

# Preenche valores específicos
df_prefiltro = df.fillna(value={ 
    'PREÇO MÉDIO DISTRIBUIÇÃO': 10, 
    'DESVIO PADRÃO DISTRIBUIÇÃO': 20,
    'PREÇO MÍNIMO DISTRIBUIÇÃO': 30,
    'PREÇO MÁXIMO DISTRIBUIÇÃO': 'vazio',
})
df_prefiltro.isnull().sum()

# Remove linhas com NaN no DataFrame original
df.dropna(inplace=True)
df.info()

# Salva em CSV limpo
df.to_csv('dados.limpos.csv', index=False)
