animais = [1,2,3, "gato", 22]
animais[0] = "cachorro"
animais.remove(22)
animais.append("leão")
animais.extend(["Cobra", "Zebra"])

print(animais)
print(len(animais))
print("gato" in animais)
print(animais.count("gato"))



print("\n\n///////////////////\n\n")

lista=[500, 131,514,30,10,84,5]
lista.sort()
print(lista)
print(max(lista))
print(min(lista))





#Tuplas são imutaveis
tp = ("Banana", "Maçã", 10, 50)
#tp[1] = "Laranja" , este comando não irá funcionar
#pois não podemos alterar valores da tupla
print(tp[0])
print(tp.count("Maçã"))
print(tp[0:2])


print("\n\n//////////DICIONARIOS/////////\n\n")

dc = {"Maçã": 10, "Banana": 20, "Laranja":15, "Uva":5}
dc["Maçã"]=25
dc.setdefault("Limão", 13)

print(dc)
print(dc["Maçã"])
print(dc.keys())
print(dc.values())