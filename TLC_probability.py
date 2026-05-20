import numpy as np
from groups import recept_year
from groups import recept_mouth
from carregar_dados import carregar_todos_os_dados
from limpeza_object import limpeza_objetos
from limpeza_num import fillna_num_copy
from analise_sem_filtro import filtro_data

dictionary = carregar_todos_os_dados()
dfs_tratados = fillna_num_copy(dictionary)
dfs_data = filtro_data(dfs_tratados)
dfs_final = limpeza_objetos(dfs_data)
df_table = dfs_final["TabelaFato"]
teste = recept_year(df_table)

def tlc_probability(coluna, tamanho_amostra=30, num_amostras=1000):
    if coluna not in df_table.columns:
        print(f"Error: Column '{coluna}' not found in the DataFrame.")
        return
    
    populacao = df_table[coluna].dropna()
    if populacao.empty:
        print(f"Error: Column '{coluna}' don't have valid numeric data.")
        return
    
    medias_amostrais = []
    for _ in range(num_amostras):
        amostra = np.random.choice(populacao, size=tamanho_amostra, replace=True)
        medias_amostrais.append(np.mean(amostra))
    
    media_populacao = np.mean(populacao)
    probabilidade = np.mean(np.array(medias_amostrais) > media_populacao)
    
    print(f"Probability of the sample mean of '{coluna}' being greater than the population mean: {probabilidade:.4f}")

tlc_probability("Receita_Total")

