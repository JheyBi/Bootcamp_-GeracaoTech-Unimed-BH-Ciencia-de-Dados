import pandas as pd

df = pd.read_csv("D:/Machine Learning/datasets/Gapminder.csv", error_bad_lines=False,sep=";")

df = df.rename(columns={"country":"Pais", "continent":"Continente", "year":"Ano","lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap":"PIB"})

print(df.head(10))

#Total de linhas e colunas
print(df.shape)

#Colunas
print(df.columns)

#Tipos de dados armazenados em cada coluna
print(df.dtypes)


#Ultimas linhas do conjunto de dados
print(df.tail(10))

#Retorna informações estatisticas
print(df.describe())

#Como fazer um filtro
print(df["Continente"].unique())
Oceania = df.loc[df["Continente"]=="Oceania"]
print(Oceania.head())
print(Oceania["Continente"].unique())


#Agrupar por continente o pais
print(df.groupby("Continente")["Pais"].nunique())


#Agrupar por ano a media da expectativa de vida
print(df.groupby("Ano")["Expectativa de vida"].mean())