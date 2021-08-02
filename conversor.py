def conversor(tipo_peso, valor_dolar):
    pesos = input('¿cuántos pesos ' +  tipo_peso + ' tienes?: ')
    pesos = float(pesos)
    valor_dolar = valor_dolar
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    conversor('colombianos', 3875)
elif opcion == '2':
    conversor('argentinos', 65)
elif opcion == '3':
    conversor('mexicanos', 19.96)
else:
    print('Ingresa una opción correcta por favor')

