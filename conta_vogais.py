def conta_vogais():
    palavra = input("Digite a palavra para contarmos as vogais: ")
    palavra = palavra.lower() # para que a comparação não seja sensível a maiuscula/minuscula
    resultado = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in palavra:
            resultado[i] = palavra.count(i)
    return resultado

print(conta_vogais())