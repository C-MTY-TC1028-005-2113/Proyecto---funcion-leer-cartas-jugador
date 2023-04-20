# Nombre -
# Matricula -
# Carrera -
figura = "?"
def leer_cartas_jugador(nombre, tablero):
    # desplegar el nombre del jugador recibido en el parámetro nombre
    # leer la carta1 r1, c1  " r1":, "c1:"
    # validar que la carta este en el rango 0..5 y que esa carta no  este visible
    # leer la carta2 r2, c2  " r2":, "c2:"
    # validar que la carta este en el rango 0..5 y que esa carta no  este visible
    # y que sea diferente de la carta1
    pass

def  despliega_tablero(opcion, matriz, r1 = None, c1 = None, r2 = None, c2 = None):
    pass



def main() :
    # 1º Leer los datos de entrada
    caso = int(input())
    
    if caso == 4:
        escondidas = [['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q'], ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q']]
        tablero = [['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        r1,c1,r2,c2 = leer_cartas_jugador("Jugador1", tablero);
        print(r1,c1,r2,c2)
    elif caso == 5:
        escondidas = [['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q'], ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q']]
        tablero = [['a', 'b', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        r1,c1,r2,c2 = leer_cartas_jugador("Jugador2", tablero);
        print(r1,c1,r2,c2)
    elif caso == 6:
        escondidas = [['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q'], ['a', 'b', 'c', 'd', 'e', 'f'], ['g', 'h', 'i', 'j', 'k', 'l'], ['m', 'n', 'ñ', 'o', 'p', 'q']]
        tablero = [['a', 'b', '?', '?', '?', 'f'], ['g', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?'], ['a', 'b', '?', '?', '?', 'f'], ['g', 'h', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', '?']]
        r1,c1,r2,c2 = leer_cartas_jugador("Jugador23", tablero);
        print(r1,c1,r2,c2)


if __name__=='__main__':
    main()
