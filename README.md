# Análise de Dados de Combustíveis – CEARÁ

Este repositório contém análises sobre preços de combustíveis no Ceará, com foco em Gasolina Comum e Etanol Hidratado.

---

## Pré-processamento

- Carregar dados tratados (`dados.limpos.csv`).
- Renomear coluna `DATA FINAL` para `ANO`.
- Converter datas para datetime e extrair o ano.
- Tratar valores nulos e converter colunas numéricas (`MARGEM MÉDIA REVENDA`, `PREÇO MÉDIO DISTRIBUIÇÃO`, etc.) com `pd.to_numeric`.
- Remover registros que ainda contêm valores nulos.

---

## Análises realizadas

### 1. Quantidade de registros por produto e região
```python
df.groupby(['PRODUTO','REGIÃO'])['NÚMERO DE POSTOS PESQUISADOS'].count()
2. Gasolina Comum em 2018
Filtrar produto e ano.

Estatísticas do preço médio de revenda:

python
Copiar
Editar
filtro = (df['PRODUTO'] == 'GASOLINA COMUM') & (df['ANO'] == 2018)
df_filtrado = df.loc[filtro]
df_filtrado['PREÇO MÉDIO REVENDA'].describe()
3. Distribuição de produtos
python
Copiar
Editar
df['PRODUTO'].value_counts()
4. Gasolina Comum e Etanol no Ceará em 2018
Filtrar produtos + estado + ano.

Estatísticas descritivas gerais e por produto:

python
Copiar
Editar
x = df.query('PRODUTO in ["GASOLINA COMUM", "ETANOL HIDRATADO"] and ESTADO == "CEARA" and ANO == 2018')
x.groupby('PRODUTO')['PREÇO MÉDIO REVENDA'].describe()
Observações
Estatísticas básicas (min, max, mean, median) foram utilizadas para análise rápida.

Agrupamentos por REGIÃO e PRODUTO permitem comparar preços médios e variações.

Dados foram totalmente limpos para evitar problemas com valores nulos ou inconsistentes.

Funções apply, map, applymap e groupby foram usadas para cálculos e agregações.

nginx
Copiar
Editar

Se você quiser, posso também **adicionar uma seção visual com gráficos de preços e distribuições** pron
