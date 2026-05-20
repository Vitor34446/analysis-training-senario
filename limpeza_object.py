import pandas as pd 
import numpy as np
from carregar_dados import carregar_todos_os_dados


files = carregar_todos_os_dados()
  
  # cleaning the object just putting "sem valor" that means "no value" in 
  # every column in every table inside the dict


def limpeza_objetos (files):
    for nome, df in files.items():
      df_copy = df.copy()

      name = df_copy.select_dtypes(include="object").columns
        # print(nome)
        # print(df_copy[name].isnull().sum())

      df_copy[name]= df_copy[name].fillna("sem valor")

      files[nome] = df_copy

      #print(df_copy.head(3))

    return files

def objetos_vazios (files):
    for nome in files:
      obj_col = files[nome].select_dtypes(include="object").columns
      files[nome][obj_col]= files[nome][obj_col].fillna("sem valor")

    return files

#for nome, df in files.items():
    #print(f'\ntabela {nome}')
    #print(df.describe())


if __name__ == "__main__":
   
   from carregar_dados import carregar_todos_os_dados

   teste = "Limpeza objetos"

   if teste == "Limpeza objetos":
      
      print("\n Teste Limpeza_objetos")
      limpeza_objetos(files)

   elif teste == "Objetos_Vazios":
      print("\nTeste Objetos_Vazios")
      objetos_vazios(files)

