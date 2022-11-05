#Dicionarios

pessoa = {"nome": "Guilherme", "idade": 28}

pessoa["nome"] #Guilherme

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "idade": 28},
    "leonardo@gmail.com": {"nome": "Leonardo", "idade": 28},
    "giovana@gmail.com": {"nome": "Giovana", "idade": 22},
}

#Metodos

#Clear

#contatos.clear() # Limpa o dicionario

#Copy

#contatos.copy() #  Copia o dicionario

#Fromkeys

dict.fromkeys(["nome", "telefone"]) # {"nome": None, "telefone": None}

#Get

print(contatos.get("guilherme@gmail.com", {})) # {"guilherme@gmail.com": {"nome": "Guilherme", "idade": 28}

#Items

#print(contatos.items()) # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'idade': 28}), ('leonardo@gmail.com', {'nome': 'Leonardo', 'idade': 28}), ('giovana@gmail.com', {'nome': 'Giovana', 'idade': 22})])

#Keys

#print(contatos.keys()) #dict_keys(['guilherme@gmail.com', 'leonardo@gmail.com', 'giovana@gmail.com'])

#Pop

contatos.pop("guilherme@gmail.com")

#Popitem

contatos.popitem() # Vai remover o "guilherme@gmail.com"

#SetDefault(Adiciona um valor no dicionario que ainda não existe)

contatos.setdefault("joao@gmail.com", {"nome": "joao", "idade":28})
print(contatos)

#Update


#Values

print(contatos.values()) # dict_values([{'nome': 'Leonardo', 'idade': 28}, {'nome': 'joao', 'idade': 28}])