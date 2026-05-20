import pandas as pd
import numpy as np
from limpeza_num import fillna_num_copy
from analise_sem_filtro import filtro_data
from carregar_dados import carregar_todos_os_dados
from limpeza_object import limpeza_objetos
from math import comb

dictionary = carregar_todos_os_dados()

dfs_tratados = fillna_num_copy(dictionary)

dfs_data = filtro_data(dfs_tratados)

dfs_final = limpeza_objetos(dfs_data)


     # see the teoric and empiric variance on TabelaFato and QuantidadeCat

df_qtd1 = dfs_final["TabelaFato"]
df_qtd2 = dfs_final["QuantidadeCat"]

def var_empi_teori():
    regras = {
        "receita_alta": df_qtd1["Receita_Total"] > df_qtd1["Receita_Total"].mean(),
        "quantidade_alta": df_qtd1["Quantidade"] > df_qtd1["Quantidade"].mean(),
        "preco_alto": df_qtd1["Preco_Unitario"] > df_qtd1["Preco_Unitario"].mean(),
        "cidade8": df_qtd1["ID_Cidade"] == 8,
        "quantidade3": df_qtd2["quantidade"] == 3
    }

    nomes = []
    var_empi_list = []
    var_teori_list = []

    for name, cond in regras.items():
        col_bin = cond.astype(int)
        p = round(col_bin.mean(), 3)
        var_empi = round(col_bin.var(), 3)
        var_teori = round(p * (1-p), 3)

        nomes.append(name)
        var_empi_list.append(var_empi)
        var_teori_list.append(var_teori)

        print(f"\n{name} %{p} empirico {var_empi} teorico {var_teori}")

    return nomes, var_empi_list, var_teori_list
    

var_empi_teori()


# var_empirica = round(((df_qtd["ID_Categoria"] == 1).var()), 2)
# var_teorica = p * (1-p)
# print (f"empirico {var_empirica} e teorico {var_teorica}")
