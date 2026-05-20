from limpeza_object import limpeza_objetos
from analise_sem_filtro import filtro_data
from limpeza_num import fillna_num
from carregar_dados import carregar_todos_os_dados
from limpeza_outliers import excluir_outliers
from limpeza_outliers import ver_outliers

def filtered_no_outliers():
    files = carregar_todos_os_dados()
   
    dfs_tratados = fillna_num(files)

    dfs_data = filtro_data(dfs_tratados)

    dfs_final = limpeza_objetos(dfs_data)

    #dfs_ver_outliers = ver_outliers(dfs_final)

    #excluir_outliers(dfs_final, dfs_ver_outliers)

    return dfs_final

# testes = filtered_no_outliers()
# print(testes)
