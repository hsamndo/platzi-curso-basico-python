def run():
    poblacion_paises = {
        'Argentina': 44938712,
        'Brazil': 210147125,
        'Colombia': 50372424
    }
#    print(poblacion_paises['Brazil'])
#    print(poblacion_paises.keys())
#    for pais in poblacion_paises.values():
#        print(pais)
    print(poblacion_paises.items())
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()