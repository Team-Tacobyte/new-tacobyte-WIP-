import mysql.connector
conn = mysql.connector.connect(user='user', password='password',
                               host='server_address', buffered=True)
cursor = conn.cursor()
databases = ("show databases")
cursor.execute(databases)
for (databases) in cursor:
    print(databases[0])
