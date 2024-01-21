# celsiu_congelamento = 0 # 0 é o ponto de congelamento da agua e 100 é o ponto de ebulição
# fahrenheit_congelamento = 32 # 32 é o ponto de congelamento da agua e 212 é o ponto de ebulição
# divida = 1.8 # é o ponto que precisamos usar para dividir e concluir a conversão

def conversao_fah_para_celsius():
    fahrenheit = float(input("Temperatura em Fahrenheit para realizamos a conversão: ")) # realizar a subtração do numero desejado pelo 32
    celsius = (fahrenheit - 32) / 1.8
    return (f'{round(celsius, 2)}ºC')

converta = conversao_fah_para_celsius()
print(converta)

def conversao_cel_para_fah():
    celsius = float(input("Temperatura deseja em Celsius para realizamos a conversão: "))
    fahrenheit = ((celsius * 1.8) + 32)
    return (f'{round(fahrenheit, 2)}ºF')

converta = conversao_cel_para_fah()
print(converta)