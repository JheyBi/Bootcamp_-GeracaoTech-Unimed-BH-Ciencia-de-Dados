import pandas as pd

df = pd.read_excel("datasets/AdventureWorks.xlsx")
print(df.head())
print(df.shape)
print(df.dtypes)

#Como fazer a receita total?
receita_total = df["Valor Venda"].sum()
print(f"\nReceita: {receita_total}")


#Como fazer o custo total?
#Criando a coluna custo
df["custo"] = df["Custo Unitário"]*df["Quantidade"]

#Calculando o custo total
custo_total = round(df["custo"].sum(), 2)
print(f"\nCusto: {custo_total}")

#Criando a coluna lucro
df["lucro"] = df["Valor Venda"]-df["custo"]

#Total de lucro
lucro_total = round(df["lucro"].sum(), 2)
print(f"\nlucro: {lucro_total}")

#Criando uma coluna com total de dias para enviar o produto
df["tempo_envio"] = (df["Data Envio"]-df["Data Venda"]).dt.days
print(df.head())

print(df.groupby("Marca")["tempo_envio"].mean())

#Verificando dados nulos
#print(df.isnull().sum())

#Formatação dos numeros
pd.options.display.float_format = "{:20,.2f}".format

#Lucro por marca por ano
print(df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum())

#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
print(lucro_ano)


#Total de produtos vendidos ordenados 
print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).reset_index())

#Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year==2009]
print(df_2009.head())



