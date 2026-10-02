# listas.py
# Exercício: criação e manipulação de listas

# Criando uma lista com 5 jogos favoritos
jogos_favoritos = ["Dark Souls 3", "Monster Hunter World", "Elden Ring", "Bloodborne", "Sekiro"]
print("Lista inicial:", jogos_favoritos)

# Adicionando um item com append()
jogos_favoritos.append("Lies of P")
print("Depois do append:", jogos_favoritos)

# Removendo um item pelo nome
jogos_favoritos.remove("Elden Ring")
print("Depois do remove:", jogos_favoritos)

# Removendo um item pela posição; sem número, tira o último.
jogos_favoritos.pop()
print("Depois do pop:", jogos_favoritos)

# Ordenando a lista em ordem alfabética com sort
jogos_favoritos.sort()
print("Depois do sort:", jogos_favoritos)