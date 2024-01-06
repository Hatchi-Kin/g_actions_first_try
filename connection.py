# mysql-connector-python==8.1.0
import mysql.connector as mysql

class Connection:
    __USER = 'root'
    __PWD = 'example'
    __HOST = 'mysql'
    __PORT = '3306'
    __DB = 'testdb'
    __cursor = None
    __bdd = None


    @classmethod
    def connect(cls):
        if cls.__cursor == None : 
            cls.__bdd = mysql.connect(user = cls.__USER, password = cls.__PWD, host = cls.__HOST, port = cls.__PORT, database = cls.__DB)
            cls.__cursor = cls.__bdd.cursor() 
        
        return cls.__cursor
    

    @classmethod
    def disconnect(cls):
        # indispensable pour closer, il faut que tout le cursor soit lu
        if cls.__bdd.in_transaction:
            cls.__bdd.commit()
        cls.__cursor.fetchall()
        cls.__cursor.close()
        cls.__bdd.close()
        cls.__cursor = None