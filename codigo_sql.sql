SELECT * from read_csv_auto('Excel/QuantVendas.csv');

SELECT * from read_csv_auto('Excel/CatPrefer.csv');

SELECT * from read_csv_auto('Excel/DimCidade.csv', delim=>';',
encoding='latin-1');

SELECT * from read_csv_auto('Excel/DimProduto.csv');

SELECT * from read_csv_auto('Excel/DimCliente.csv');

SELECT * from read_csv_auto('Excel/DimCategoria.csv');

SELECT * from read_csv_auto('Excel/TabelaFato.csv');

SELECT * from read_csv_auto('Excel/QuantidadeCat.csv');

SELECT * from read_csv_auto('Excel/ranking.csv');


SELECT * from read_csv_auto('Excel/top3.csv');


select ID_Cidade, COUNT(*) as quantidade 
from read_csv_auto('Excel/TabelaFato.csv')
GROUP BY ID_Cidade
ORDER BY Quantidade DESC;

SELECT MAX(Preco_Unitario) max FROM
read_csv_auto('Excel/TabelaFato.csv');

SELECT MIN(Preco_Unitario) max FROM
read_csv_auto('Excel/TabelaFato.csv');


