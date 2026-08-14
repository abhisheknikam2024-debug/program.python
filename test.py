
import psycopg2
try:
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="abhi123", host="localhost",port="5432")
    cursor = conn.cursor()
    print("Successfully connected to PostgreSQL database.")


    create_table_query = """
        CREATE TABLE IF NOT EXISTS boys(id INT,name VARCHAR(50),age INT NOT NULL,course VARCHAR(50));
        """
    cursor.execute(create_table_query)
    conn.commit()
    print(" Table 'boys' created successfully.")
    # creating a table

    insert_query = """
        INSERT INTO boys (name, age, course) 
        VALUES ('Abhi', 22, 'Python Development');
        """
    cursor.execute(insert_query)
    conn.commit()
    print("Initial record inserted successfully.")

    # insert the value in table

    user_name = input("Enter Name: ")
    user_age = int(input("Enter Age: "))
    user_course = input("Enter Course: ")

    # Use %s placeholders for parameterized queries (prevents SQL injection)
    dynamic_insert = """
        INSERT INTO boys (name, age, course) 
        VALUES (%s, %s, %s);
        """
    cursor.execute(dynamic_insert, (user_name, user_age, user_course))
    conn.commit()
    
    print(" Dynamic record inserted successfully.")
    
    # user input given to create

    cursor.execute("SELECT * FROM boys;")
    single_record = cursor.fetchone()
    print("First Record:", single_record)

    # display all record

    print("\n--- Fetching Records with WHERE Condition (age > 20) ---")
    where_query = "SELECT * FROM boys WHERE age > %s;"
    cursor.execute(where_query, (20,))
    filtered_records = cursor.fetchall()
    
    print("Matching Records:")
    for row in filtered_records:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")

    # select with where candition

    cursor.execute("TRUNCATE TABLE boys ;")
    conn.cursor()
    print("truncate tsble successfully")

    conn.close()

except Exception as error :
    print("an error occure")
    