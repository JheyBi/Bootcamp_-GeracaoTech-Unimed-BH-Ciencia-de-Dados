#Conjutos

#Elimina elementos duplicados, mas não garente a ordem
set([1,2,3,1,3,4]) # {1,2,3,4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}

#Metodos

#Union

conjunto_a = {1,2}
conjunto_b = {3,4}

conjunto_a.union(conjunto_b) # {1,2,3,4}

#Intersection

conjunto_a = {1,2,3}
conjunto_b = {3,4,5}

conjunto_a.intersection(conjunto_b) # {3}

#Difference

conjunto_a = {1,2,3}
conjunto_b = {3,4,5}

conjunto_a.difference(conjunto_b) # {1,2}
conjunto_b.difference(conjunto_a) # {4,5}

#Symmetric_difference

conjunto_a = {1,2,3}
conjunto_b = {3,4,5}

conjunto_a.difference_symmetric(conjunto_b) # {1,2,4,5}

#issubset

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

conjunto_a.issubset(conjunto_b) #True
conjunto_b.issubset(conjunto_a) #False

#issuperset

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

conjunto_a.issuperset(conjunto_b) #False
conjunto_b.issuperset(conjunto_a) #True

