import mysql.connector 
import pandas as pd

class mydbDF:
    def __init__(self) :
        self.mydb = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='batman2022',
            db='cine'
        )
        self.cursor = self.mydb.cursor()
        
    def dataframe(self):
        try:
            self.cursor = self.mydb.cursor()
            sql =''' SELECT DISTINCT m.name AS 'Movie' , m.year AS 'YEAR', d.last_name AS 'Director', m.ranking AS 'Ranking'
                FROM (cine.movies_directors AS md JOIN cine.movies AS m ON m.id = md.movies_id)
                JOIN cine.directors AS d ON d.id = director_id
                WHERE m.ranking > 8 ORDER BY m.ranking DESC '''
            self.cursor.execute(sql)
            lista = self.cursor.fetchall()
            self.mydb.commit()
            l = []
            for row in lista:
                l.append(row)
            df = pd.DataFrame(l)
            df1_im = df.set_axis(['PELICULA  ','AÑO ','DIRECTOR ','PUNTAJE '], axis=1)
            return df1_im
            
        except Exception as e:
            raise
    def mostrar_DF(self):
        m = self.dataframe()
        print(m)
    def primera_consulta(self):
        df = self.dataframe()
        print(df.loc[0:9,['PELICULA  ','PUNTAJE ']])
       
        
    def segunda_consulta(self):
        df = self.dataframe()
        print(df.iloc[20:51])
        
        
     