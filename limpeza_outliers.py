import pandas as pd 
import numpy as np
from carregar_dados import carregar_todos_os_dados

files= carregar_todos_os_dados()


colun_ignora = ["ID_Cliente","ID_Cidade","ID_Produto","ID_Categoria","ID_Venda","ID_cliente"]

# it is necessary to see the outliers, values that are far from the rest of the data
# they can be small values or big ones

def ver_outliers (files):
    
    outliers_dict ={}
    
    for nome in files:
      df = files[nome]
      outliers_dict[nome] = {}

      mask_total = pd.Series(False, index=df.index)

      num_col = df.select_dtypes(include="number").drop(columns=colun_ignora, errors="ignore").columns
      df[num_col]= df[num_col].fillna(0)


  # it's necessary to access the columns inside the table that are inside the dict
  # but with the variable num_col that contains the filters to the numeric values  

      for col in num_col:

        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lin_inf = max(0,Q1 - 1.5 * IQR)
        lin_sup = Q3 + 1.5 * IQR

   # now it's necessary to concatenate the filters into a single dictionary  

        mask_col = (df[col] < lin_inf) | (df[col] > lin_sup)

        outliers_regra = df[col] < 2

        mask_total = mask_total | mask_col | outliers_regra
    
      outliers_dict[nome]= df[mask_total]

      # print(outliers_dict)

    return outliers_dict
    

def excluir_outliers(files, outliers_dict):
    for nome in files:
        df = files[nome]
        outliers = outliers_dict[nome]
        df_limpo = df[~df.index.isin(outliers.index)]
        files[nome] = df_limpo


excluir_outliers(files, ver_outliers(files))


if __name__ == "__main__":
  files = carregar_todos_os_dados()
  outliers = ver_outliers(files)

  # now it's possible to access the data with the outliers and see all of them

  for nome, df in outliers.items():
      print(f"\nOutliers em {nome}:")
      print(df)


  