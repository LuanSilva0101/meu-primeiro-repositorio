agenda = {
    "Ana": "(49) 99999-1111",
    "Bruno": "(49) 99999-2222",
    "Carla": "(49) 99999-3333",
    "Diego": "(49) 99999-4444",
    "Elisa": "(49) 99999-5555",
}

def buscar_contato(nome):
    for contato, telefone in agenda.items():
        if contato.lower() == nome.lower():
            return telefone
    return None

nome = input("Buscar contato: ")
telefone = buscar_contato(nome)

if telefone:
    print(f"{nome}: {telefone}")
else:
    print("Contato não encontrado.")