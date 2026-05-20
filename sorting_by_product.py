import pandas as pd
from filter import filtered_no_outliers
from normalization import normalizar

files = filtered_no_outliers()
dfs_table_no_outliers = files["TabelaFato"]
df = dfs_table_no_outliers.copy()

receita_produto_mes = (
    df.groupby(['ID_Produto', pd.Grouper(key='Data', freq='ME')])['Receita_Total']
    .sum()
    .reset_index()
)

receita_produto_mes['Variação'] = (
    receita_produto_mes
    .groupby('ID_Produto')['Receita_Total']
    .pct_change()
)

receita_produto_mes['cresceu'] = receita_produto_mes['Variação'] > 0

prob_produto = (
    receita_produto_mes
    .groupby('ID_Produto')['cresceu']
    .mean()
    .sort_values(ascending=False)
)

impacto_produto = (
    receita_produto_mes
    .groupby('ID_Produto')['Receita_Total']
    .sum()
)

receita_produto_mes['Variação'] = receita_produto_mes['Variação'].clip(-1, 1)
receita_produto_mes = receita_produto_mes.dropna(subset=['Variação'])

media_variacao = receita_produto_mes.groupby('ID_Produto')['Variação'].mean()
volatilidade = receita_produto_mes.groupby('ID_Produto')['Variação'].std()

resultado = pd.concat([prob_produto, impacto_produto], axis=1)
resultado.columns = ['prob_crescimento', 'receita_total']

resultado = resultado.sort_values(by='prob_crescimento', ascending=False)

# print(resultado)

df_score = pd.concat([
    prob_produto,
    impacto_produto,
    media_variacao,
    volatilidade
], axis=1)

df_score.columns = [
    'prob_crescimento',
    'receita_total',
    'media_variacao',
    'volatilidade'
]
df_score_norm = df_score.copy()

df_score_norm['prob_crescimento'] = normalizar(df_score['prob_crescimento'])
df_score_norm['receita_total'] = normalizar(df_score['receita_total'])
df_score_norm['media_variacao'] = normalizar(df_score['media_variacao'])
df_score_norm['volatilidade'] = 1-normalizar(df_score['volatilidade'])

df_score_norm['score'] = (
    0.40 * df_score_norm['prob_crescimento'] +
    0.30 * df_score_norm['receita_total'] +
    0.20 * df_score_norm['media_variacao'] +
    0.10 * df_score_norm['volatilidade']
)

ranking = df_score_norm.sort_values(by='score', ascending=False)

print(ranking)

ranking_table = ranking.head(3)

print(ranking_table.to_markdown())