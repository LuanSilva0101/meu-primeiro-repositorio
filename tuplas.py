# tuplas.py
# Exercício: convertendo entre lista e tupla

# Criando uma tupla com os 3 dias da semana que mais gosto
dias_favoritos = ("sábado", "domingo", "sexta")
print("Tupla inicial:", dias_favoritos)

# Convertendo a tupla em lista com list()
dias_lista = list(dias_favoritos)
print("Convertida para lista:", dias_lista)

# Adicionando um novo dia na lista
dias_lista.append("quinta")
print("Depois de adicionar um dia:", dias_lista)

# Convertendo a lista de volta para tupla com tuple
dias_favoritos = tuple(dias_lista)
print("Convertida de volta para tupla:", dias_favoritos)