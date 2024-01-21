def quadrado_magico(matriz):
    if(
        sum(matriz[0]) == sum(matriz[1]) == sum(matriz[2]) and
        matriz[0][0] + matriz[0][1] + matriz[0][2] == sum(matriz[0]) and
        # Soma diagonal
        matriz[0][0] + matriz[1][1] + matriz[2][2] == sum(matriz[0]) and
        matriz[0][2] + matriz[1][1] + matriz[2][0] == sum(matriz[0]) and
        matriz[1][0] + matriz[1][1] + matriz[1][2] == sum(matriz[0]) and
        matriz[2][0] + matriz[2][1] + matriz[2][2] == sum(matriz[0])
    ):
            return "Quadrado Mágico!"
    else:
            return "Não é Mágico"

matriz = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

resultado = quadrado_magico(matriz)
print(resultado)