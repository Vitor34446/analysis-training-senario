from carregar_dados import carregar_todos_os_dados
from limpeza_num import ver_numericos
from limpeza_outliers import ver_outliers
from limpeza_outliers import excluir_outliers
from limpeza_num import fillna_num
from limpeza_num import fillna_num_copy
from analise_sem_filtro import filtro_data
from limpeza_num import ver_nulos_tipos
from limpeza_num import mostrar_copia
from analise_sem_filtro import informaçoes_basicas
from limpeza_object import limpeza_objetos
from limpeza_object import objetos_vazios
from groups import recept_mouth
from groups import recept_year
from groups import mean_per_product
from filter import filtered_no_outliers

def main():
    files = carregar_todos_os_dados()
   
    dfs_tratados = fillna_num_copy(files)

    dfs_data = filtro_data(dfs_tratados)

    dfs_final = limpeza_objetos(dfs_data)

    df_table = dfs_final["TabelaFato"]

    #ver_numericos(files)
    #ver_outliers(files)
    #excluir_outliers(files)
    #recept_mouth(df_table)
    #recept_year(df_table)
    #mean_per_product(df_table)
    #fillna_num(files)
    #fillna_num_copy(files)
    #filtro_data(files)
    #ver_nulos_tipos(files)
    #mostrar_copia(files)
    #informaçoes_basicas(files)
    #limpeza_objetos(files)
    #objetos_vazios(files)
    filtered_no_outliers()
    
    print("Deu boa")

if __name__== "__main__":
    main()