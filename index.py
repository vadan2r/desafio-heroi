#Desafio Classificador de nível de Herói
def heroi(nome, XP, nivel):
    if XP < 1000:
        nivel = "Ferro"
    elif XP < 2000:
        nivel = "Bronze"
    elif XP < 5000:
        nivel = "Prata"
    elif XP < 7000:
        nivel = "Ouro"
    elif XP < 8000:
        nivel = "Platina Diamante"
    elif XP < 9000:
        nivel = "Ascendente"
    elif XP < 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"
    return f"Heroi: {nome}, Nivel: {nivel}"

# Testando a função com diferentes heróis
heroi1 = heroi("Garen", 1500, "")
heroi2 = heroi("Lux", 3000, "")
heroi3 = heroi("Zed", 8000, "")

print(heroi1)
print(heroi2)
print(heroi3)