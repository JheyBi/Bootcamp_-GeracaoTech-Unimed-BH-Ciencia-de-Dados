import pandas as pd

df1 = pd.read_excel("datasets/Aracaju.xlsx")
df2 = pd.read_excel("datasets/Fortaleza.xlsx")
df3 = pd.read_excel("datasets/Natal.xlsx")
df4 = pd.read_excel("datasets/Recife.xlsx")
df5 = pd.read_excel("datasets/Salvador.xlsx")

#print(df5.head())


#Juntando todos os arquivos
df = pd.concat([df1,df2,df3,df4,df5])


#Confirmando se juntou mesmo os arquivos
print("====================HEAD===================\n\n")
print(df.head())
print("\n\n====================TAIL===================\n\n")
print(df.tail())
print("\n\n====================SAMPLE===================\n\n")
print(df.sample(5))
print("\n")
print(df["Cidade"].unique())
print("\n\n")

#Verificando o tipo de cada coluna
print(df.dtypes)
print("\n\n")


#Alterando o tipo de dado da coluna LOJAID, 
#já que não iremos realizar nenhum calculo com ele, não há necessidade dele ser do tipo int

df["LojaID"] = df["LojaID"].astype("object")

#Verificando o tipo de cada coluna
print(df.dtypes)
print("\n\n")

#Consultando linhas com valores nulos
print(df.isnull().sum())


#Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

#Apagando as linhas com valores nulos
#df.dropna(inplace=True)




#Criando uma coluna nova
df["Receita"] = df["Vendas"].mul(df["Qtde"])
print(df.head())


#Retornando a maior receita
print(df["Receita"].max())

#Retornando a menor receita
print(df["Receita"].min())


#Retornando o top3 receitas
print(df.nlargest(3, "Receita"))

#Retornando o top3 menores receitas
print(df.nsmallest(3, "Receita"))

print("\n")

#Agrupamento por cidade
print(df.groupby("Cidade")["Receita"].sum())

#Ordenando conjuto de dados
print(df.sort_values("Receita", ascending=True).head(10))


#Transformando  a coluna data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

#Verificando os tipos
print("\n")
print(df.dtypes)

#Transformando a coluna data em tipo data
df["Data"] = pd.to_datetime(df["Data"])

#Verificando os tipos
print("\n")
print(df.dtypes)

#Agrupamento da receita por ano
print(df.groupby(df["Data"].dt.year)["Receita"].sum())


#Criando a coluna de ano
df["ano_venda"] = df["Data"].dt.year

#Extraindo o mes e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

print(df.sample(5))

#Filtrando as vendas de 2019 do mês de março
vendas_marco_2019 = df.loc[(df["ano_venda"]==2019) & (df["mes_venda"]==3)]
print(vendas_marco_2019)

#print(df["LojaID"].value_counts(ascending=False))

print(df["LojaID"].value_counts(ascending=False).plot.bar())