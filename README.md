# 🛡️ Classificador de Nível de Herói

Este projeto tem como objetivo a implementação de funcionalidades relacionadas à classificação e comportamento de heróis em um contexto de jogos ou desafios gamificados. As funções foram desenvolvidas em Python e seguem três eixos principais:

![Heróis](https://github.com/user-attachments/assets/5176cf1b-a6cb-4088-bc0b-e9db0cd29b72)


## 📌 Funcionalidades

### 1. Classificação de Nível com Base na Experiência (XP)

A função `heroi()` classifica o nível de um herói de acordo com sua experiência (XP):

```python
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
    return f"Herói: {nome}, Nível: {nivel}"

![Nível com Base na Experiência](https://github.com/user-attachments/assets/d0091a05-8a81-4b01-8692-3449ecd64517)


2. Comparação entre Vitórias e Derrotas
A função comparar_vitorias_derrotas() calcula o saldo de partidas ranqueadas (vitórias - derrotas) e classifica o jogador conforme o número de vitórias:

def comparar_vitorias_derrotas(vitorias, derrotas):
    saldo_rankeadas = (vitorias - derrotas)
    nivel = ""    
    if vitorias <= 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"        
    return nivel, saldo_rankeadas

![Vitórias e Derrotas](https://github.com/user-attachments/assets/6455df2f-42c3-4c5f-96f9-de483c6bb87d)


3. Classe Heroi com Método de Ataque
A classe Heroi representa personagens com atributos e comportamento específico de ataque, dependendo do tipo de herói:

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

🚀 Como Executar
Certifique-se de ter o Python instalado.

Salve o código em um arquivo .py.

Execute com o comando:

python nome_do_arquivo.py

📄 Licença
Este projeto é um desafio proposto para fins educacionais e de prática em lógica de programação com Python.
