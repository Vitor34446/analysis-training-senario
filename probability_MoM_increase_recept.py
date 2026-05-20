import pandas as pd
from filter import filtered_no_outliers
from normalization import normalizar

files = filtered_no_outliers()
dfs_table_no_outliers = files["TabelaFato"]
df = dfs_table_no_outliers.copy()

df["Data"]= pd.to_datetime(df["Data"])

receita_mensal = (
    df.groupby(pd.Grouper(key='Data', freq='M'))['Receita_Total']
    .sum()
    .reset_index()
)

receita_mensal["Variação"] = receita_mensal["Receita_Total"].pct_change()

receita_mensal["Cresceu"] = receita_mensal["Variação"] > 0

prob = receita_mensal['Cresceu'].mean()

print(f"Probabilidade de aumento: {prob:.2%}")