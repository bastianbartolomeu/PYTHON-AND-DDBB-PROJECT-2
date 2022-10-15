import mysql.connector 
import pandas as pd

class mydbFF:
    def __init__(self) :
        self.mydb = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='batman2022',
            db='cine'
        )
        self.cursor = self.mydb.cursor()
    
    def actors(self):
        try:
            sql ='SELECT * FROM cine.actors'
            self.cursor.execute(sql)
            listados = self.cursor.fetchall()
            print(listados)
        except Exception as e:
            raise
        
    def directors(self):
        try:
            sql ='SELECT * FROM cine.directors'
            self.cursor.execute(sql)
            listados = self.cursor.fetchall()
            print(listados)
        except Exception as e:
            raise
    
    def movies_DF(self):
        try:
            sql ='SELECT * FROM cine.movies'
            self.cursor.execute(sql)
            listados = self.cursor.fetchall()
            return listados
        except Exception as e:
            raise
        
    def movies(self):
        m = self.movies_DF()
        print(m)
        
    def movies_b(self):
        m = self.movies_DF()
        l= []
        for row in m:
            l.append(row)
        df =pd.DataFrame(l)
        return df
        
    def prueba(self):
        m = self.movies_b()
        l = m[0]
        k = int(input('Ingresa un valor : '))
        if k in l:
            print('correcto')
        else:
            print('malo')
    
        
    def buscar_movies(self):
        try:
            self.cursor = self.mydb.cursor()
            sql ='SELECT * FROM cine.movies Where id = %s'
            f = int(input('Ingrese el ID de la Pelicula : '))    
            sel = (f,)
            self.cursor.execute(sql,sel)
            lista = self.cursor.fetchall()
            print(' LA DESCRIPCIÓN DE LA PELICULA ES LA SIGUENTE : \n')                    
            print(' ID de la Pelicula : ', lista[0][0], '\n','Nombre : ', lista[0][1],'\n','AÑO DE LA PELICULA : ',lista[0][2],'\n','RANKING DE LA PELICULA : ',lista[0][3])
            self.mydb.commit()
    
    
        except Exception as e:
            raise
    
    def buscar_actor(self):
        try:
            self.cursor = self.mydb.cursor()
            sql ='SELECT * FROM cine.actors Where id = %s'
            f = int(input('Ingrese el ID del Actor : '))
            sel = (f,)
            self.cursor.execute(sql,sel)
            lista = self.cursor.fetchall()
            print(' LA DESCRIPCIÓN DE LA PELICULA ES LA SIGUENTE : \n')
            print(' ID del Actor : ', lista[0][0], '\n','Nombre del actor : ', lista[0][1],'\n','Apellido Actor : ',lista[0][2])
            self.mydb.commit()
        except Exception as e:
            raise
    
    def buscar_director(self):
        try:
            self.cursor = self.mydb.cursor()
            sql ='SELECT * FROM cine.directors Where id = %s'
            f = int(input('Ingrese el ID del director: '))
            sel = (f,)
            self.cursor.execute(sql,sel)
            lista = self.cursor.fetchall()
            print(' LA DESCRIPCIÓN DE LA PELICULA ES LA SIGUENTE : \n')
            print(' ID del Actor : ', lista[0][0], '\n','Nombre del actor : ', lista[0][1],'\n','Apellido Actor : ',lista[0][2])
            self.mydb.commit()
        except Exception as e:
            raise
        
    def directores_peliculas(self):
        try:
            self.cursor = self.mydb.cursor()
            sql='''SELECT DISTINCT d.last_name AS APELLIDO, d.first_name AS NOMBRE, COUNT(movies_id) AS 'CANTIDAD DE PELICULAS' 
                FROM cine.movies_directors AS md JOIN cine.directors AS d ON d.id = md.director_id
                GROUP BY  APELLIDO , NOMBRE HAVING COUNT(movies_id) > %s
                ORDER BY COUNT(movies_id) DESC'''
            f =int(input(' DIRECTORES CON CUANTAS PELICULAS DESEA BUSCAR : '))
            sel =(f,)
            self.cursor.execute(sql,sel)
            lista = self.cursor.fetchall()
            print(lista)
            self.mydb.commit()
        except Exception as e: 
            raise
    
    def actores_ranking(self):
        try:
            self.cursor = self.mydb.cursor()
            sql='''SELECT DISTINCT a.last_name, a.first_name, COUNT(movies_id)
                    FROM cine.actors AS a JOIN cine.movies_actores AS ma ON ma.actor_id = a.id
                    GROUP BY a.last_name, a.first_name 
                    ORDER BY a.last_name, a.first_name'''
            self.cursor.execute(sql)
            lista = self.cursor.fetchall()
            print(lista)
            self.mydb.commit()
        except Exception as e: 
            raise
    
    def peliculas_detalles(self):
        try:
            self.cursor = self.mydb.cursor()
            sql =''' SELECT DISTINCT m.name AS 'Movie' , m.year AS 'YEAR', d.last_name AS 'Director', m.ranking AS 'Ranking'
                FROM (cine.movies_directors AS md JOIN cine.movies AS m ON m.id = md.movies_id)
                JOIN cine.directors AS d ON d.id = director_id
                WHERE m.ranking > %s ORDER BY m.ranking DESC '''
            f= int(input('INGRESE EL RANKING DE LAS PELICULAS QUE QUIERE BUSCAR '))
            sel =(f,)
            self.cursor.execute(sql,sel)
            lista = self.cursor.fetchall()
            print(lista)
            self.mydb.commit()
        except Exception as e:
            raise
            
    