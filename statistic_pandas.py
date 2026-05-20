import pandas as pd
import numpy as np
from limpeza_num import fillna_num_copy
from analise_sem_filtro import filtro_data
from carregar_dados import carregar_todos_os_dados
from limpeza_object import limpeza_objetos

dictionary = carregar_todos_os_dados()

colun_ignora= ["ID_Cliente",
               "ID_Cidade",
               "ID_Produto",
               "ID_Categoria",
               "ID_Venda",
               "ID_cliente",
               "Data",
               "Data_formatada"]

dfs_tratados = fillna_num_copy(dictionary)

dfs_data = filtro_data(dfs_tratados)

dfs_final = limpeza_objetos(dfs_data)

  # now the data is clean, it's possible to start the statistic part 

for name, df in dfs_final.items():
    filter = df.drop(columns=colun_ignora, errors="ignore")
    filter = filter.select_dtypes(include=np.number)

    varian = filter.var()
    desvio = filter.std()
    media = filter.mean()
    se = filter.std() / np.sqrt(filter.count())
    percentual_se = round((se / media) * 100,2)
    cv = round((desvio / media) * 100,2)
    
    metric = "cv"

    if metric == "varian":
        print(f"\n{name}")
        print("Variancia:")
        print(varian)
    elif metric =="desvio":
        print(f"\n{name}")
        print("Desvio Padrao:")
        print(desvio)
    elif metric == "media":
        print(f"\n{name}")
        print("Media:")
        print(media)
    elif metric == "se":
        print(f"\n{name}")
        print("Erro Padrão:")
        print(se)
    elif metric == "percentual_se":
        print(f"\n{name}")
        print("Erro Padrão percentual:")
        print(percentual_se)
    elif metric == "cv":
        print(f"\n{name}")
        print("coeficiente de variação:")
        print(cv)


