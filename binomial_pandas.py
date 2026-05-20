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

df_qtd = dictionary["CatPrefer"]


pro_col1 = round(((df_qtd["ID_Categoria"] == 1).mean()), 2)
pro_col2 = round(((df_qtd["ID_Categoria"] == 2).mean()), 2)
    # discrete expected value 
pro_col = ((df_qtd["ID_Categoria"]).mean())

    # the value of pro_col is 1.39, which represents the empirical expected 
    # value of the categorical variable. the category 1 is more frequent than 
    # category 2 in the long run.

print(pro_col1)
print(pro_col2)
print(pro_col)


    # it's possible to calculate the probability that k out of n random sales are
    # from category 1. 

n = 10
k = 10

prob1 = comb(n,k) * (pro_col1**k) * ((1 - pro_col1)**(n - k))
print(prob1)

    # The binomial model uses two complementary probabilities (p and 1-p).
    # Symmetry only holds when swapping both p and k (k ↔ n-k), not p alone.

# var1 = df_qtd[df_qtd["ID_Categoria"] == 1]
# var2 = var1[var1["quantidade"] == 10]
# print(var2)
