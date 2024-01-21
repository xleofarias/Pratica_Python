def soma_pares(n):
    soma = 0
    numero = 2  # Começamos com o primeiro número par
    for x in range(n):
        soma += numero
        numero += 2  # Avançamos para o próximo número par
    return soma

# Exemplo de uso:
n = 10
resultado = soma_pares(n)
print(f"A soma dos primeiros {n} números pares é: {resultado}")