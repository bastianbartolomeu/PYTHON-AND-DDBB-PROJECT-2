import mysql.connector 
import csv

class mydbPT2:
    def __init__(self) :
        self.mydb = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='batman2022',
            db='cine'
        )
        self.cursor = self.mydb.cursor()
        
        print('----------------------------------------------- ')
        print('                CONEXION EXITOSA' )
        print(self.mydb)
        print('----------------------------------------------- ')
        
         
         
    def moviesCSV_to_BBDD(self):
        with open ('C:\Users\Dell\Desktop\DIPLOMADO\PYTHON Y BASE DE DATOS\PROYECTOS\Miniproyecto2\movies.csv' ) as CSVFILE:
            readCSV = csv.reader(CSVFILE, delimiter=';')
            filas = []
            first = next(readCSV)
            print('----------------------------------------------- ')
            print('         LISTAS DE PELICULA  ')
            print('----------------------------------------------- ')
            for row in readCSV:
                #print(row)
                filas.append(tuple([row[0],row[1],row[2],row[3]]))
            print(filas)
        try:
            self.cursor = self.mydb.cursor()
            sql='INSERT INTO movies (id,name,year,ranking) VALUES (%s,%s,%s,%s)'
            self.cursor.executemany(sql,filas)
            print('--------------------------------------------------------- ')
            print('        MOVIES REGISTRADAS CORRECTAMENTE       ')
            print('--------------------------------------------------------- ')
            self.mydb.commit()
        except Exception as e:
            raise
    
        
    def actorsCSV_to_BBDD(self):
        with open ('C:/Users/basti/OneDrive/Escritorio/DIPLOMADO/PYTHON Y BASE DE DATOS/PROYECTOS/Miniproyecto2/actors.csv',encoding='utf-8') as CSVFILE:
            readCSV = csv.reader(CSVFILE, delimiter=';')
            filas = []
            first = next(readCSV)
            print('--------------------------------------------------------- ')
            print('         LISTA DE ACTORES    ')
            print('--------------------------------------------------------- ')
            for row in readCSV:
                 #print(row)
                 filas.append(tuple([row[0],row[1],row[2]]))
            print(filas)
        try:
            self.cursor = self.mydb.cursor()
            sql='INSERT INTO actors (id,first_name,last_name) VALUES (%s,%s,%s)'
            self.cursor.executemany(sql,filas)
            print('--------------------------------------------------------- ')
            print('        ACTORES REGISTRADOS CORRECTAMENTE       ')
            print('--------------------------------------------------------- ')
            self.mydb.commit()
        except Exception as e:
            raise
        
    
    def directorsCSV_to_BBDD(self):
        with open ('C:/Users/basti/OneDrive/Escritorio/DIPLOMADO/PYTHON Y BASE DE DATOS/PROYECTOS/Miniproyecto2/directors.csv',encoding='utf-8') as CSVFILE:
            readCSV = csv.reader(CSVFILE, delimiter=';')
            filas = []
            first = next(readCSV)
            print('--------------------------------------------------------- ')
            print('         LISTA DE DIRECTORES   ')
            print('--------------------------------------------------------- ')
            for row in readCSV:
                 #print(row)
                 filas.append(tuple([row[0],row[1],row[2]]))
            print(filas)
        try:
            self.cursor = self.mydb.cursor()
            sql='INSERT INTO directors (id,first_name,last_name) VALUES (%s,%s,%s)'
            self.cursor.executemany(sql,filas)
            print('--------------------------------------------------------- ')
            print('        DIRECTORES REGISTRADOS CORRECTAMENTE       ')
            print('--------------------------------------------------------- ')
            self.mydb.commit()
        except Exception as e:
            raise
        
    def movies_actorsCSV_to_BBDD(self):
        with open ('C:/Users/basti/OneDrive/Escritorio/DIPLOMADO/PYTHON Y BASE DE DATOS/PROYECTOS/Miniproyecto2/movies_actors.csv',encoding='utf-8') as CSVFILE:
            readCSV = csv.reader(CSVFILE, delimiter=';')
            filas = []
            first = next(readCSV)
            print('--------------------------------------------------------- ')
            print('                LISTA DE MOVIES & ACTORES           ')
            print('--------------------------------------------------------- ')
            for row in readCSV:
                 #print(row)
                 filas.append(tuple([row[0],row[1],row[2]]))
            print(filas)
        try:
            self.cursor = self.mydb.cursor()
            sql='INSERT INTO movies_actores (actor_id,movies_id,role) VALUES (%s,%s,%s)'
            self.cursor.executemany(sql,filas)
            print('--------------------------------------------------------- ')
            print('       DATOS MOVIES & ACTORES AGREGADAS CORRECTAMENTE       ')
            print('--------------------------------------------------------- ')
            self.mydb.commit()
        except Exception as e:
            raise
    
    def movies_directorsCSV_to_BBDD(self):
        with open ('C:/Users/basti/OneDrive/Escritorio/DIPLOMADO/PYTHON Y BASE DE DATOS/PROYECTOS/Miniproyecto2/movies_directors.csv',encoding='utf-8') as CSVFILE:
            readCSV = csv.reader(CSVFILE, delimiter=';')
            filas = []
            first = next(readCSV)
            print('--------------------------------------------------------- ')
            print('                LISTA DE MOVIES & DIRECTORES              ')
            print('--------------------------------------------------------- ')
            for row in readCSV:
                 #print(row)
                 filas.append(tuple([row[0],row[1]]))
            print(filas)
        try:
            self.cursor = self.mydb.cursor()
            sql='INSERT INTO movies_directors (director_id,movies_id) VALUES (%s,%s)'
            self.cursor.executemany(sql,filas)
            print('--------------------------------------------------------- ')
            print('   DATOS MOVIES & DIRECTORES AGREGADAS CORRECTAMENTE       ')
            print('--------------------------------------------------------- ')
            self.mydb.commit()
        except Exception as e:
            raise
        
    

        
#MP2 = mydbPT2()
#MP2.directorsCSV_to_BBDD()
#MP2.actorsCSV_to_BBDD()
#MP2.moviesCSV_to_BBDD()        
#MP2.movies_actorsCSV_to_BBDD()
#MP2.movies_directorsCSV_to_BBDD()
