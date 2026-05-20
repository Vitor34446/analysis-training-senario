import pandas as pd
import numpy as np 
from carregar_dados import carregar_todos_os_dados


colun_ignora = ["ID_Cliente","ID_Cidade","ID_Produto","ID_Categoria","ID_Venda","ID_cliente"]

files = carregar_todos_os_dados()

def filtro_data (files):
    
    filtered = {}

  # making a filter to the data frame, ignoring columns that is not gonna be used 

    for nome in files:
        df = files[nome]

        mask_total = pd.Series(False, index=df.index)

        num_col = df.select_dtypes(include="number")
        var1 = num_col.drop(columns=colun_ignora, errors="ignore")

        df[var1.columns]= df[var1.columns].fillna(0)

        for col in var1:

            mask_total = mask_total | (num_col[col] !=0) 


        filtered_df= df[mask_total]

        filtered[nome] = filtered_df

    # for nome, tabela in filtered.items():
    #     print(f"{nome}")
    #     print(tabela)

    return filtered


    # basic descriptions, see what kind of data it is, getting random items on the data frame
    # see the unique df values 

def analisa_df(df, nome="Tabela"):
    tabe = df.select_dtypes(include="number").drop(columns=colun_ignora, errors="ignore")
    if tabe.empty:
        print(f"\n{nome}: sem colunas numéricas para analisar")
        return

    print(f'\nTabela descrição {nome}')
    print(round(tabe.describe(), 2))

    print(f'\nTabela info {nome}')
    print(df.info())

    print(f'\nTabela correlação {nome}')
    correlacao = tabe.corr()
    print(correlacao)

    print(f'\nTabela únicos {nome}')
    print(tabe.nunique())

    print(f'\nValores aleatórios {nome}')
    print(df.sample(5))


def informaçoes_basicas(files):
    if isinstance(files, pd.DataFrame):
        analisa_df(files, nome="Tabela única")
        return files

    filtro = filtro_data(files)
    for nome, df in filtro.items():
    
        tabe = df.select_dtypes(include="number")
        usar = tabe.drop(columns=colun_ignora, errors="ignore")

        ids =  df.select_dtypes(include="number")
        tab_clie = filtro["DimCliente"]
    
        for col in usar:

            if not tabe.empty:

                print(f'\ntabela descrição {nome}')
                print(round(tabe.describe(),2))
    
                print(f'\ntabela info {nome}')
                print(df.info())

                print(f'\ntabela unicos {nome}')
                print(tabe.nunique())

                print(f'\nvalores aleatorios {nome}')
                print(df.sample(5))
    return files 

if __name__ == "__main__":
    from carregar_dados import carregar_todos_os_dados
    
    teste = "filtro data"

    if teste == "Informaçoes basicas":
        print("Informações basicas")
        informaçoes_basicas(files)
    elif teste == "filtro data":
        print("Filtro Data")
        filtro = filtro_data(files)
        for nome, df in filtro.items():
            print(f'\nTabela {nome}')
            print(df.head(3))
