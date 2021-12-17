import psycopg2


class doinsertbase:
 

 
   

  
    def abrir_base():
        
          connection = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='mysecretpassword',
                database = 'postgres')    
            
      
   

    def cierro_base():
        print("cierro")