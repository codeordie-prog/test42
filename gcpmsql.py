import pymysql

HOST = '34.28.140.195'
USER='kelvin'
DATABASE ='expense_tracker'
PASSWORD = 'Kelvinjoe692'


#create connection
def connection(HOST,USER,PASSWORD,DATABASE):

    connection = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    return connection

def result():

    conn = connection(HOST=HOST,USER=USER,PASSWORD=PASSWORD,DATABASE=DATABASE)

    crsr = conn.cursor()

    query = 'SELECT * FROM expenses;'

    crsr.execute(query)

    results = crsr.fetchall()

    return results



    


