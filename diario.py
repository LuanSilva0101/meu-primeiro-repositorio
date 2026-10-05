with open ("diario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Estou aprendendo Python!\n")
    arquivo.write("Preciso praticar mais.\n")
    arquivo.write("Espero que amanhã seja um dia produtivo.\n")

with open("diario.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Ainda não estou confiante nas minhas habilidades.\n")
    arquivo.write("Espero melhorar com mais prática.\n")

with open("diario.txt", "r", encoding="utf-8") as arquivo:
    for i, linha in enumerate(arquivo, start=1):
        print(f"{i}: {linha.strip()}")