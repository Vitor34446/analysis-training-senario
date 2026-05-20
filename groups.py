import pandas as pd
import numpy as np
import matplotlib.pyplot as plp
from limpeza_num import fillna_num_copy
from analise_sem_filtro import filtro_data
from carregar_dados import carregar_todos_os_dados
from limpeza_object import limpeza_objetos

dictionary = carregar_todos_os_dados()

dfs_tratados = fillna_num_copy(dictionary)

dfs_data = filtro_data(dfs_tratados)

dfs_final = limpeza_objetos(dfs_data)

df_table = dfs_final["TabelaFato"]

def metrics(df_table):
    return {
        "city_recept": df_table.groupby("ID_Cidade")["Receita_Total"].mean(),
        "city_quant": df_table.groupby("ID_Cidade")["Quantidade"].mean(),
        "product_recept": df_table.groupby("ID_Produto")["Receita_Total"].mean(),
        "product_quant": df_table.groupby("ID_Produto")["Quantidade"].mean()
    
    }


def recept_mouth(df_table):
    return df_table.groupby(df_table["Data"].dt.to_period('M'))["Receita_Total"].sum()

def recept_year(df_table):
    return df_table.groupby(df_table["Data"].dt.to_period('Y'))["Receita_Total"].sum()

def mean_per_product(df_table):
    return round(df_table.groupby("ID_Produto")["Receita_Total"].mean(), 3)

if __name__== "__main__":
    teste1 = recept_year(df_table)
    teste2 = recept_mouth(df_table)
    teste3 = mean_per_product(df_table)
    teste4 = metrics(df_table)

    print(teste2)