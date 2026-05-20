import pandas as pd 
import numpy as np 

  # it's necessary to create a def with all the tables, because the changes can be 
  # saved on this def 


def carregar_todos_os_dados():
    files={
        "TabelaFato":pd.read_csv('Excel/TabelaFato.csv', sep=';'),
        "CatPrefer":pd.read_csv('Excel/CatPrefer.csv', sep=';'),
        "DimCliente":pd.read_csv('Excel/DimCliente.csv', sep=';'),
        "QuantidadeCat":pd.read_csv('Excel/QuantidadeCat.csv', sep=';'),
        "QuantVendas":pd.read_csv('Excel/QuantVendas.csv', sep=';')
    }
     

    for nome, df in files.items():
        # clean spaces on columns names
        df.columns = df.columns.str.strip()
        
        # Convert "Data" column to datetime and print "Data_formatada"
        if "Data" in df.columns:
            df["Data"] = pd.to_datetime(df["Data"], dayfirst=True ) # convert to datetime
            df["Data_formatada"] = df["Data"].dt.strftime("%d/%m/%Y") 

   
    return files 
   