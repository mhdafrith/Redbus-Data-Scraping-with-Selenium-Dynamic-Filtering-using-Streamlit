import pymysql
import pandas as pd



def creation_of_table(cursor, table_name, table_column_declaration):
    create_table_query = f'create table {table_name}{table_column_declaration};'
    print("create_table_query = ", create_table_query)
    cursor.execute(create_table_query)
    print("Table Created Successfully")



try:
    # Connection Parameters
    connection = pymysql.connect(
         host = 'localhost', user = 'root', 
         password = '24434244342', database = 'redbus_project')
    print("connection = ", connection)
    cursor = connection.cursor()
    print("cursor = ", cursor)
    table_name='bus_data'
    table_column_declaration='(id int primary key auto_increment not null,route_name varchar(255),route_link varchar(255),busname varchar(255),bustype varchar(255),departing_time time,duration varchar(255),reaching_time time,star_rating decimal(10,2))'
    creation_of_table(cursor,table_name,table_column_declaration)
except Exception as e:
    print(str(e))


df=pd.read_csv('/Users/mohamedafrith/Desktop/redbus_project/final_redbus_data_2.csv')
db_config = {
    'user': 'root',
    'password': '24434244342',
    'host': 'localhost',
    'database': 'redbus_project'
}

# Connect to the database
conn = pymysql.connect(**db_config)
cursor = conn.cursor()




insert_query = "INSERT INTO bus_data (route_name,route_link,busname,bustype,departing_time ,duration,reaching_time ,star_rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

for index, row in df.iterrows():
    cursor.execute(insert_query,(row['route_name'], row['route_link'],row ['busname'], row['bustype'],row['departing_time'],row['duration'], row['reaching_time'], row['star_rating']))


conn.commit()

# Close the connection
cursor.close()
conn.close()
   