from analise_sem_filtro import informaçoes_basicas
import matplotlib.pyplot as plt
from carregar_dados import carregar_todos_os_dados
from limpeza_object import limpeza_objetos
from limpeza_num import fillna_num_copy
from analise_sem_filtro import filtro_data
import seaborn as sns

colun_ignora = ["ID_Cliente","ID_Cidade","ID_Produto","ID_Categoria","ID_Venda","ID_cliente"]

dictionary = carregar_todos_os_dados()

dfs_tratados = fillna_num_copy(dictionary)

dfs_data = filtro_data(dfs_tratados)

dfs_final = limpeza_objetos(dfs_data)

df_table = dfs_final["TabelaFato"]

informaçoes_basicas(df_table)


tabe = df_table.select_dtypes(include="number").drop(columns=colun_ignora, errors="ignore")
if not tabe.empty:
    correlacao = tabe.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Matriz de Correlação - TabelaFato')
    plt.show()


