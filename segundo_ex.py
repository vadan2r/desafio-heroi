# Função que compara vitória e derrotas de um jogador
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
# Exemplo de uso da função

nivel, saldo_rankeadas = comparar_vitorias_derrotas(50, 20) # Retorna saldo de 30 e nível Prata
print(f"O heroi tem saldo de {saldo_rankeadas} e está no nível {nivel}.")