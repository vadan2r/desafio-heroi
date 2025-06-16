# 3️⃣ Escrevendo as classes de um Jogo
# Desafio: Criar uma classe Heroi com atributos e métodos para atacar
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        
    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "arma desconhecida"

        print(f"O {self.tipo} {self.nome} atacou usando {ataque}.")

# Exemplo de uso
heroi1 = Heroi("Aragorn", 35, "guerreiro")
heroi1.atacar()  # Saída: O guerreiro Aragorn atacou usando espada

heroi2 = Heroi("Merlin", 150, "mago")
heroi2.atacar()  # Saída: O mago Merlin atacou usando magia

heroi3 = Heroi("Bruce Lee", 40, "monge")
heroi3.atacar() # Saída: O monge Bruce Lee atacou usando artes marciais

heroi4 = Heroi("Naruto", 17, "ninja")
heroi4.atacar() # Saída: O ninja Naruto atacou usando shuriken