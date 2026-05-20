import pandas as pd
from filter import filtered_no_outliers
from normalization import normalizar

files = filtered_no_outliers()
dfs_table_no_outliers = files["TabelaFato"]
df = dfs_table_no_outliers.copy()

receita_cidade_mes = (
    df.groupby(['ID_Cidade', pd.Grouper(key='Data', freq='ME')])['Receita_Total']
    .sum()
    .reset_index()
)

top3_receita_produto_cidade = (
    df.groupby(["ID_Cidade","ID_Produto"])['Receita_Total'].sum()
    .reset_index()
)

top3_receita_produto_cidade = (
    top3_receita_produto_cidade.groupby("ID_Cidade")
    .apply(lambda x: x.nlargest(3,"Receita_Total"))
)

receita_cidade_mes["variação"] = (
    receita_cidade_mes
    .groupby('ID_Cidade')['Receita_Total']
    .pct_change()
)

receita_cidade_mes['cresceu'] = receita_cidade_mes['variação'] > 0 

prob_cidade = (
    receita_cidade_mes
    .groupby('ID_Cidade')['cresceu']
    .mean()
    .sort_values (ascending=False)
)

impacto_cidade = (
    receita_cidade_mes
    .groupby('ID_Cidade')['Receita_Total']
    .sum()
)

receita_cidade_mes['variação'] = receita_cidade_mes['variação'].clip(-1, 1)
receita_produto_mes = receita_cidade_mes.dropna(subset=['variação'])

media_variacao = receita_produto_mes.groupby('ID_Cidade')['variação'].mean()
volatilidade = receita_produto_mes.groupby('ID_Cidade')['variação'].std()

df_score = pd.concat([
    prob_cidade,
    impacto_cidade,
    media_variacao,
    volatilidade
], axis= 1)

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

print(top3_receita_produto_cidade)

ranking_table = ranking.head(3)

print(ranking_table.to_markdown())

#top3_receita_produto_cidade.to_csv("top3.csv", index= True)
