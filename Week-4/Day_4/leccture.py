import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'laeticiaoceane'
PASSWORD = '12345678'
DATABASE = 'public'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

cursor = connection.cursor()
query = "SELECT * FROM movies LIMIT 2;"
cursor.execute(query)
results = cursor.fetchall()
print("\n",results,"\n")
#connection.close()