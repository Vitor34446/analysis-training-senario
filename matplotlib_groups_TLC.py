import matplotlib.pyplot as plp 
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

def show_tlc(coluna, tamanho_amostra=30, num_amostras=1000):
    if coluna not in df_table.columns:
        print(f"Erro: Coluna '{coluna}' não encontrada no DataFrame.")
        return
    
    populacao = df_table[coluna].dropna()
    if populacao.empty:
        print(f"Erro: Coluna '{coluna}' não tem dados numéricos válidos.")
        return
    
    medias_amostrais = []
    for _ in range(num_amostras):
        amostra = np.random.choice(populacao, size=tamanho_amostra, replace=True)
        medias_amostrais.append(np.mean(amostra))
    

    plp.figure(figsize=(10, 6))
    plp.hist(medias_amostrais, bins=30, edgecolor='black', alpha=0.7)
    plp.title(f'Distribuição das Médias Amostrais - TLC ({coluna})')
    plp.xlabel(f'Média Amostral de {coluna}')
    plp.ylabel('Frequência')
    plp.grid(True, alpha=0.3)
    plp.show()

show_tlc("Receita_Total")






