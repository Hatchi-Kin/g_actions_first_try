import mysql.connector as mysql

class Connection:
    __USER = 'root'
    __PWD = 'example'
    __HOST = 'localhost'
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


def create_test_table():
    cursor = Connection.connect()
    query = "CREATE TABLE test_table (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255))"
    cursor.execute(query)
    Connection.disconnect()
    return True


def test_table_exists():
    cursor = Connection.connect()
    cursor.execute("SHOW TABLES LIKE 'test_table'")
    result = cursor.fetchone()
    Connection.disconnect()
    assert result != None

def test_write_data():
    cursor = Connection.connect()
    name = "test"
    last_name = "test"
    email = "test"
    query = f"INSERT INTO test_table(name, last_name, email) VALUES('{name}', '{last_name}', '{email}')"
    cursor.execute(query)
    Connection.disconnect()
    
    cursor = Connection.connect()
    cursor.execute("SELECT COUNT(*) FROM test_table")
    result = cursor.fetchone()[0]
    Connection.disconnect()
    assert result == 1


def test_read_data():
    cursor = Connection.connect()
    cursor.execute("SELECT * FROM test_table")
    result = cursor.fetchone()
    Connection.disconnect()
    assert result != None
    assert result[1] == "test"
    assert result[2] == "test"
    assert result[3] == "test"


def test_flush_data():
    cursor = Connection.connect()
    cursor.execute("DELETE FROM test_table")
    Connection.disconnect()
    cursor = Connection.connect()
    cursor.execute("SELECT COUNT(*) FROM test_table")
    result = cursor.fetchone()[0]
    Connection.disconnect()
    assert result == 0
    