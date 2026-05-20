                ## Data Analisis Training

    A project dedicated to recriate a real sales cenario, with some simplifications.

                ## Structure of the project

    CSV Files
        ↓
    Data Cleaning
        ↓
    Missing Values Handling
        ↓
    Outlier Removal (IQR)
        ↓
    CV Calculation
        ↓
    Normalization
        ↓
    Score Modeling
        ↓
    Product & City Ranking
        ↓
    Business Insights

                ## Project Limitations

    ° Synthetic values.
    ° No promotions or holiday included.
    ° No cost columns.
    ° No missing values.

                ## Business questions

    ° Identify the most sold product. 
    ° Identify the city with the highest sales frequency.
    ° Create a score to determinate the best product or city for investiment.
    ° Analize the MoM probability of growth.

                ## Dataset 

    ° It contains a total of 10 csv tables.
    ° Products. 
    ° Category.
    ° Clients.
    ° Sales and dates.
    ° City.
    ° Other tables (ranking and top3) were created by intersecting tables using 
    Pandas dictionaries.

                ## Technologies used 

    ° Python.
    ° SQL.
    ° Pandas.
    ° Matplotlib.
    ° Numpy.
    ° Seaborn.
    ° Excel.

                ## Data Cleaning 

        The following preprocessing steps were applied:
    
    ° Missing values handling.

    ° Outlier removal.

    ° Data type conversion.

    ° Standardization of categorical variables.

    ° I also used coeficient of variation (CV) to use the function fillna().Depending 
    of the percentage of CV, I filled with median or mean.

    ° IQR was used for outlier filtering. 

                ## Analisys performed 

    ° Detection of top investment opportunities.
    ° Product performance ranking.
    ° City performance ranking. 
    ° Cross-analysis between cities and products.
    ° Trend analysis over time. 

                ## Methodology

    ° Data cleaning.
    ° Outlier treatment.
    ° Feature engineering.
    ° Score creation.
    ° Normalization.
    ° Ranking logic.

                ## Scoring Sistem 

    ° Conservative: Based on the coefficient of variation (CV), prioritizing products or cities with lower volatility.

    ° Agressive: Based on growth metrics, prioritizing products or cities with higher growth potential.

    ° In the aggressive score, growth probability has the highest weight, followed by total revenue.

                 ## Key insights 

        |ID City |growth probability |total revenue |variation mean |volatility |score |
    |-------------:|----------------:|-------------:|--------------:|------------:|-----:|
    |   1(Fortaleza) |  1     |        0.857188 |         0.81 |     0.408  | 0.86 |
    |   2 |  0.625 |  0.317  |         1        |     0.007 | 0.546 |
    |   9 |  0.875 |  0.143 |         0.237299 |     0.887   | 0.529 |

    ° Agressive city score: city 7 (Fortaleza) achieved a score of 86, being the best to invest in an agressive campaign. 

        |ID City |growth probability |total revenue |variation mean |volatility |score |
    |-------------:|---------------:|----------------:|------------:|---------------:|-------:|
    |      13(window) |  1        |  1        |         1        |       0.537 | 0.953 |
    |      6 |  0.857 |  0.495 |         0.825 |       0.642 | 0.72 |
    |      12 |  0.714 |  0.682 |         0.673 |       0.478 | 0.673 |

    ° Agressive product score: product 13 (window) achieved a score of 95, showing a strong growth potencial. 

    ° The Categorie 1 represents 61% of the frequency, and the Category 2 represents 39%, indicating slightly better performance for Category 1.

        |ID Product |CV Recept |CV Unitary Price |CV quant |score |
    |-------------:|--------------:|---------------------:|-----------------:|---------:|
    |  7(ball) |  1        |  1        |         0.967 | 0.99 |
    | 13 |  0.906 |  0.935 |         0.811 | 0.886 |
    | 16 |  0.639 |  0.425 |         1        | 0.683 |

    ° Conservative product score: product 7 and product 13 performed very well. Product 13 is stable and popular. 

        |ID_Cidade |CV_Receitac |CV_Preco_Unitarioc |CV_Quantidadec |score |
    |------------:|--------------:|---------------------:|-----------------:|---------:|
    |  8(Brasilia) |      1        |             0.924 |         0.444 | 0.810 |
    |  4 |      0.608 |             0.905 |         0.702 | 0.725 |
    |  1 |      0.556 |             1        |         0.495 | 0.671 |

    ° Conservative city score: city 8 (Brasilia) was the most stable.

    ° The top 3 products performed better than the top 3 cities across all scoring systems, suggesting that investing in products is safer and potentially more profitable.