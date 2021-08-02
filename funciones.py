def imprimir_mensaje():
    print('Mensaje especial: ')
    print('Estoy aprendiendo a usar funciones')

imprimir_mensaje()
imprimir_mensaje()
imprimir_mensaje()

def conversacion(mensaje):
    print('Hola')
    print('Como estás')
    print(mensaje)
    print('Adios')

opcion = input('Elige una opción (1, 2, 3): ')
if opcion == '1':
  conversacion('Elegiste la opción 1')
if opcion == '2':
    conversacion('Elegiste la opción 2')
if opcion == '3':
   conversacion('Elegiste la opción 3')