from connection import Connection


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
    