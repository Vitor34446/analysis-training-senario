import pandas as pd
import numpy as np
from carregar_dados import carregar_todos_os_dados

files = carregar_todos_os_dados()

     # cleaning a ficional database, there is no missing lines but in this project 
     # the complete path of data cleaning will be made, even it is not necessary,
     # but the other project gonna be more complete to recriate a real cenario whit 
     # missing object and numeric information

    # cleaning the numeric ones

colun_ignora= ["ID_Cliente","ID_Cidade","ID_Produto","ID_Categoria","ID_Venda","ID_cliente"]


def ver_nulos_tipos(files):
    for nome, df in files.items():
        print(f"\n{nome}")
        print(df.isnull().sum())

    for nome, df in files.items():
        print(nome, type(df))

    return files

       # if database have some missing lines, could use that to see if
       # its better to use fillna.mean() or fillna().median or simply 
       # drop()
def ver_numericos(files):

    for nome, df in files.items():

        numericos = df.select_dtypes(include="number").drop(columns=colun_ignora, errors="ignore")
    
        varian = numericos.var()
        desvio = numericos.std()
        media = numericos.mean()
        cv = round(desvio/media * 100,2)
        # print(f"\n{nome}")
        # print("Variancia:")
        # print(varian)
        print(f"\n{nome}")
        print("Desvio Padrao:")
        print(desvio)
        print(f"\n{nome}")
        print("Media:")
        print(media)
        print(f"\n{nome}")
        print("Coeficiente Variação:")
        print(cv)
    return files 

    # the CV(coeficient of variation) in all colunms are high, 44.5 in quant_vendas table Quant_Vendas,
    # quantidade 55.1 percent in QuantidadeCat, preco_unitario is 55.7, Quantidade
    # is 55.8, Receita_Total is 84.5 of table TabelaFato  
def fillna_num_copy(files):

    files2_filled = {}

    for nome, df in files.items():
        df_copy = df.copy()
    
        numericos = df_copy.select_dtypes(include="number")
        colunas_analise = numericos.drop(columns=colun_ignora, errors="ignore")
    
        for col in colunas_analise.columns:
            media = numericos[col].mean()
            desvio = numericos[col].std()
            cv = desvio / media if media != 0 else 0
        
            if cv > 0.4:
                df_copy[col] = df_copy[col].fillna(numericos[col].median())
            else:
                df_copy[col] = df_copy[col].fillna(media)
    
        files2_filled[nome] = df_copy
    return files2_filled

def mostrar_copia(files):
    fill = fillna_num_copy(files)

    for nome, df in  fill.items():
        print(f"tabela {nome}")
        print(df.head(3))
    return files

   # the same structure, but not using a copy 
def fillna_num(files):

    for nome, df in files.items():
    
        numericos = df.select_dtypes(include="number").drop(columns=colun_ignora, errors="ignore")
        df[numericos.columns]= df[numericos.columns].fillna(0)
    
        for col in numericos.columns:
            media = numericos[col].mean()
            desvio = numericos[col].std()
            cv = desvio / media if media != 0 else 0
        
            if cv > 0.4:
                df[col] = df[col].fillna(numericos[col].median())
            else:
                df[col] = df[col].fillna(media)

    return files
    

if __name__ == "__main__":
    from carregar_dados import carregar_todos_os_dados

    print("Testando Ver_Numericos")
    ver_numericos(files)


    #print("\nTestando Ver_Nulos_Tipos")
    #ver_nulos_tipos(files)


    #print("\nTestando Fillna_num")
    #fillna_num(files)


    #print("\nTestando Mostrar_Copia")
    #mostrar_copia(files)
