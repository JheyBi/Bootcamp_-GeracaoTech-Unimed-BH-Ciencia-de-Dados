numeros = [1,30,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0]
#[Variavel que deseja armazenar; Codigo]


#Metodos

#Append

lista=[]

lista.append(1)
lista.append("Python")
lista.append([40,1,2])

# print(lista) # [1, python, [40,1,2]]


#Clear

#lista = [1, python, [40,1,2]]

lista.clear()

# print(lista) # []

#Copy

#lista = [1, python, [40,1,2]]

l2 = lista.copy()

# print(l2) # [1, python, [40,1,2]]
#Listas iguais mas com id's diferentes
#Assim podemos alterar sem afetar minha lista original


#Count
cores = ["vermelho", "azul", "verde"]

cores.count("vermelho") #1
cores.count("azul") #2
cores.count("verde")#3

#Extend

linguagens = ["python", "js", "c"]

#print(linguagens) # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

#print(linguagens) # ["python", "js", "c", "java", "csharp"]



#Index(Mostra a posição da primeira ocorrencia)

#linguagens = ["python", "java", "c", "java", "csharp"]

linguagens.index("java") #1
linguagens.index("c") #2


#pop

#linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop() #csharp
linguagens.pop() #java
linguagens.pop() #c
linguagens.pop(0) #python

#Remove

#linguagens = ["python", "js", "c", "java", "c"]

linguagens.remove("c")

print(linguagens) #["python", "js", "java", "c"]


#Reverse

#linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reserve()

print(linguagens) #["csharp", "java", "c", "js", "python"]


#Sort(Ordenação de lista)

#Por ordem alfabetica
#linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() #["c","csharp", "java", "js", "python"]

#Reverse do ordem alfabetica
#linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) #["python", "js", "java","csharp","c"]

#Por tamanho da palavra
#linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) #["c", "js", "java", "python",  "csharp"]

#Reverse do tamanho da palavra
#linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) #["python", "csharp", "java", "js", "c"]




#Len(Tamanho)


#Sorted(Ordenação)


#linguagens = ["python", "js", "c", "java", "csharp"]
sorted(linguagens, key=lambda x: len(x)) #["c", "js", "java", "python",  "csharp"]



