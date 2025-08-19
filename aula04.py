import pandas as pd

df = pd.read_csv('dados.limpos.csv')  
# Lê os dados de um arquivo CSV e cria o DataFrame principal.

stat = df.describe()  
# Gera estatísticas descritivas (contagem, média, min, max, etc.) de todas as colunas numéricas.

stat[['PREÇO MÉDIO REVENDA', 'DESVIO PADRÃO REVENDA']]  
# Exibe apenas as estatísticas dessas duas colunas.

stat.loc[['min', 'max', 'mean']]  
# Seleciona apenas as linhas de estatísticas mínimas, máximas e médias.

stat.loc[['min', 'max', 'mean'], ['DESVIO PADRÃO REVENDA', 'NÚMERO DE POSTOS PESQUISADOS']]  
# Filtra linhas (min, max, mean) e colunas específicas.

df['PREÇO MÉDIO REVENDA'].min()  
# Retorna o menor valor da coluna.

df['PREÇO MÉDIO REVENDA'].median()  
# Calcula a mediana dessa coluna.

sorted(df['ESTADO'].unique())  
# Lista os estados únicos em ordem alfabética.

df['ESTADO'].value_counts().sort_values(ascending=False)  
# Conta registros por estado e ordena do maior para o menor.

df['ESTADO'].value_counts().sort_values()  
# Conta registros por estado e ordena do menor para o maior.

df['ESTADO'].value_counts().sort_values().to_frame()  
# Converte a contagem de estados para um DataFrame.

def soma(linha):
    return linha.sum()
# Define uma função que soma os valores de uma linha ou coluna.

meu_df = pd.DataFrame({
    'A': [1,2,3,4],
    'B': [10,20,30,40],
    'C': [100,200,300,400],
}, index=['LINHA1' , 'LINHA2' , 'LINHA3', 'LINHA4'])  
# Cria um DataFrame de exemplo.

meu_df['SOMA'] = meu_df.apply(soma,axis=1)  
# Cria coluna "SOMA" com a soma das colunas em cada linha.

meu_df.loc['LINHA5'] = meu_df.apply(soma,axis=0)  
# Adiciona nova linha "LINHA5" com a soma de cada coluna.

meu_df['media ABC'] = meu_df[['A','B','C']].apply(lambda sires: sires.mean(), axis=1)  
# Cria coluna com a média de A, B e C.

meu_df['C/2'] = meu_df['C'].apply(lambda x: x / 2)  
# Cria coluna "C/2" dividindo os valores da coluna C por 2.

meu_df.applymap(lambda x: x * 2)  
# Multiplica todos os valores do DataFrame por 2 (não altera o original).

sires = pd.Series(['JOÃO', 'CARLOS', 'JOSE', 'MARIA'])  
# Cria uma Series de nomes.

sires.map(lambda x: x.lower())  
# Converte todos os nomes para minúsculo usando map.

sires.str.lower()  
# Converte todos os nomes para minúsculo usando método de string (mais eficiente).

df_reigao = df.groupby('REGIÃO')  
# Agrupa o DataFrame original pela coluna "REGIÃO".

df_reigao.indices  
# Mostra os índices de cada grupo.

df_reigao.get_group('NORDESTE')  
# Retorna os registros do grupo "NORDESTE".

df_reigao.describe()  
# Retorna estatísticas descritivas para cada grupo.

dd = df.groupby(['REGIÃO', 'PRODUTO'])  
# Agrupa o DataFrame por duas colunas: "REGIÃO" e "PRODUTO".

dd.describe()  
# Estatísticas descritivas por região e produto.

df.info()  
# Mostra informações gerais do DataFrame.

dd['PREÇO MÉDIO REVENDA'].mean()  
# Calcula a média da coluna "PREÇO MÉDIO REVENDA" dentro de cada grupo.

tt = pd.DataFrame([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [None,None,None]                  
], columns=['A','B','C'], index=['L1','L2','L3','L4'])  
# Cria um DataFrame com valores e uma linha com valores nulos.

tt.agg([sum,min])  
# Aplica as funções soma e mínimo em cada coluna.

dd = df.groupby('REGIÃO')  
# Agrupa novamente apenas por "REGIÃO".

dd['PREÇO MÉDIO REVENDA'].agg([max,min])  
# Calcula o valor máximo e mínimo da coluna dentro de cada região.

notas = pd.DataFrame({
    'Nome': ['João', 'Ana', 'Gael', 'Carlos'],
    'Idade': [11,12,11,10],
    'Nota': [4.3,7.5,10,7.5]
})  
# Cria um DataFrame com notas de alunos.

notas.sort_values(by=['Nota', 'Nome'], ascending=[False,True], inplace=True)  
# Ordena o DataFrame por Nota (decrescente) e, em caso de empate, por Nome (crescente).

notas = notas.reset_index(drop=True)  
# Reseta o índice para ficar sequencial após a ordenação.

notas  
# Exibe o DataFrame final.
