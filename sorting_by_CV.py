import pandas as pd
from filter import filtered_no_outliers
from normalization import normalizar

colun_ignora= ["ID_Cliente",
               "ID_Categoria",
               "ID_Venda",
               "ID_cliente",
               "Data",
               "Data_formatada"]

files = filtered_no_outliers()
dfs_table= files["TabelaFato"]
df_copy = dfs_table.copy()
df = dfs_table.drop(columns=colun_ignora, errors="ignore")

df_score_produto = (
    df.groupby("ID_Produto")[["Receita_Total","Preco_Unitario","Quantidade"]]
    .apply(lambda x: x.std()/ x.mean())
)

df_score_cidade = (
    df.groupby("ID_Cidade")[["Receita_Total","Preco_Unitario","Quantidade"]]
    .apply(lambda x: x.std()/ x.mean())
)

df_score_produto.columns= [
    'CV_Receitap',
    'CV_Preco_Unitariop',
    'CV_Quantidadep'
]

df_score_cidade.columns= [
    'CV_Receitac',
    'CV_Preco_Unitarioc',
    'CV_Quantidadec'
]

df_score_norm_pro = df_score_produto.copy()

df_score_norm_pro['CV_Receitap'] = 1-normalizar(df_score_produto['CV_Receitap'])
df_score_norm_pro['CV_Preco_Unitariop'] = 1-normalizar(df_score_produto['CV_Preco_Unitariop'])
df_score_norm_pro['CV_Quantidadep'] = 1-normalizar(df_score_produto['CV_Quantidadep'])

df_score_norm_pro['score'] = (
    0.40 * df_score_norm_pro['CV_Receitap'] +
    0.30 * df_score_norm_pro['CV_Preco_Unitariop'] +
    0.30 * df_score_norm_pro['CV_Quantidadep']
)

df_score_norm_cid = df_score_cidade.copy()

df_score_norm_cid['CV_Receitac'] = 1-normalizar(df_score_cidade['CV_Receitac'])
df_score_norm_cid['CV_Preco_Unitarioc'] = 1-normalizar(df_score_cidade['CV_Preco_Unitarioc'])
df_score_norm_cid['CV_Quantidadec'] = 1-normalizar(df_score_cidade['CV_Quantidadec'])

df_score_norm_cid['score'] = (
    0.40 * df_score_norm_cid['CV_Receitac'] +
    0.30 * df_score_norm_cid['CV_Preco_Unitarioc'] +
    0.30 * df_score_norm_cid['CV_Quantidadec']
)

ranking_pro = df_score_norm_pro.sort_values(by='score', ascending=False)
ranking_cid = df_score_norm_cid.sort_values(by='score', ascending=False)

print(ranking_pro)
print(ranking_cid)

ranking_table_cid = ranking_cid.head(3)

print(ranking_table_cid.to_markdown())