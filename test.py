import psycopg2

conn = psycopg2.connect(dbname= "postgres", user ="postgres",password="abhi123",host="localhost",port="5432")
print("cannect succussfully")
# creating a connection between dbms and python language

#creating a table
def Table():
    conn = psycopg2.connect(dbname= "postgres", user ="postgres",password="abhi123",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute('''create  table employee(Name text,ID int,age int);''')
    print("table created")
    conn.commit()
    

#insert data into table    
def Data():
    conn = psycopg2.connect(dbname= "postgres", user ="postgres",password="abhi123",host="localhost",port="5432")

 #to take input from user
    name = input("entre the name:")
    id = input('entre id:')
    age = input('entre age:')

    query= '''insert into employee(Name,ID,age) values(%s ,%s,%s);'''
    cursor.execute(query,(name,id,age))
    print("data added successfully")
    conn.commit()
    


# fetch and display all record
cursor = conn.cursor()
cursor.execute("select * from employee ; ")
single_record = cursor.fetchone()
print("Frist record :", single_record)

# select with where candition
print("\n --- fetching records with WHERE candition (age >20)---" )
where_query = "select * from employee WHERE age>%s;"
cursor.execute(where_query , (20,))
fil_record  = cursor.fetchall()

print("mathching record:")
for row in fil_record:
    print(f"ID: {row[0]} | Name : {row[1]} | age:{row[2]}")

# trucate table

cursor = conn.cursor()
cursor.execute("truncate table employee;")

except Exception as error:
    print (" an erroroccure")

conn.commit()
conn.close()