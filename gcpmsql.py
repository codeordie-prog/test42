import pymysql



#create connection
def connection(HOST,USER,PASSWORD,DATABASE):

    connection = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    return connection


    


