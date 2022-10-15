from Funciones import mydbFF
from DataFrame import mydbDF


def menuPincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print(' ')
            print(' =============== MENU ==========')
            print( '''        
    1 - Listar Todos los Actores
    2 - Listar Todos los Directores
    3 - Listar Todas las Peliculas
    4 - Buscar Pelicula  
    5 - Buscar Actor
    6 - Buscar Director
                  
============ PREGUNTAS INTERESANTES =============
    7 - LISTA DE DIRECTOR POR CANTIDADES DE PELICULAS  
    8 - LISTA RANKING DE ACTORES 
    9 - DETALLES DE LAS PELICULAS 
===================================

============ PREGUNTAS DATAFRAME =============
    10 - DETALLE DE LAS PELICULAS CON DATAFRAME 
    11 - LISTA DE LAS PRIMERAS 10 PELICULAS CON PUNTAJE
    12 - LISTA DE PELICULAS DESDE LA 20 A LA 50 
    13 - *******SALIR DEL PROGRAMA****** 
==============================================
''')
            opcion = int(input(' seleccione alguna opción : '))
            
            if opcion < 1 or opcion > 13:
                print(' Opcion incorrecta, ingrese nuevamente ')
            elif opcion == 13 :
                print('Gracias por usar este sistema ')
                break
            else :
                opcionCorrecta = True 
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    DAO = mydbFF()
    DDF = mydbDF()
    
    if opcion == 1:
        DAO.actors()
    elif opcion == 2:
        DAO.directors()
    elif opcion== 3:
        DAO.movies()
    elif opcion == 4:
        DAO.buscar_movies()
    elif opcion == 5:
        DAO.buscar_actor()
    elif opcion == 6:
        DAO.buscar_director()
    elif opcion == 7:
        DAO.directores_peliculas()
    elif opcion == 8:
        DAO.actores_ranking()
    elif opcion == 9:
        DAO.peliculas_detalles()
    elif opcion== 10:
        DDF.mostrar_DF()
    elif opcion == 11:
        DDF.primera_consulta()
    elif opcion == 12:
        DDF.segunda_consulta()
    
menuPincipal()
