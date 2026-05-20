import pandas as pd
import mysql.connector
import os

# Configuração MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="JKL3U90%#Ggj*",
    database="projeto_dados_fic"
)
cursor = conn.cursor()

# Pasta com CSVs
pasta = r"C:\Projeto_Dados_ficticios\Excel"

for arquivo in os.listdir(pasta):
    if arquivo.endswith(".csv"):
        caminho = os.path.join(pasta, arquivo)
        df = pd.read_csv(caminho, encoding="latin1", sep=";")
        df = df.astype(object).where(pd.notnull(df), None)
        
        tabela = os.path.splitext(arquivo)[0]  # nome da tabela = nome do arquivo

        # Criar tabela automaticamente (todas as colunas como TEXT, opcional: ajustar tipos)
        colunas = ", ".join([f"`{col}` TEXT" for col in df.columns])
        cursor.execute(f"DROP TABLE IF EXISTS `{tabela}`;")
        cursor.execute(f"CREATE TABLE `{tabela}` ({colunas});")

        # Inserir dados
        for _, row in df.iterrows():
            valores = tuple(None if pd.isna(x) else x for x in row)
            placeholders = ", ".join(["%s"] * len(row))
            cursor.execute(f"INSERT INTO `{tabela}` VALUES ({placeholders})", valores)

        print(f"{arquivo} importado para a tabela `{tabela}`")

conn.commit()
cursor.close()
conn.close()
print("Importação completa!")