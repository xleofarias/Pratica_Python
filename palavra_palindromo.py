# Função para confirmar se a palavra digitada é palíndromo.
def confirma_palindromo():
    palavra_input = input("DIGITE A PALAVRA: ").lower()
    print(palavra_input.strip())
    palavra_contrario = palavra_input [::-1]
    if palavra_contrario.lower() == palavra_input.lower():
        print(f"{palavra_input} é palíndromo")
    else: print(f"{palavra_input} não é palíndromo")

confirma_palindromo()