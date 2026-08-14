

import psycopg2

# ==========================================
# 1. CONNECT TO POSTGRESQL DATABASE
# ==========================================
try:
    conn = psycopg2.connect(
        dbname="postgres",     # Default PostgreSQL database
        user="postgres",       # Your database username
        password="abhi123",    # Your database password
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    print("✓ Successfully connected to PostgreSQL database.")

    # ==========================================
    # 2. CREATE A TABLE
    # ==========================================
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        age INT NOT NULL,
        course VARCHAR(50) NOT NULL
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("✓ Table 'students' created successfully.")

    # ==========================================
    # 3. INSERT HARDCODED DATA
    # ==========================================
    insert_query = """
    INSERT INTO students (name, age, course) 
    VALUES ('Abhi', 22, 'Python Development');
    """
    cursor.execute(insert_query)
    conn.commit()
    print("✓ Initial record inserted successfully.")

    # ==========================================
    # 4. INSERT DYNAMIC DATA (Parameterized Query)
    # ==========================================
    print("\n--- Enter New Student Details ---")
    user_name = input("Enter Name: ")
    user_age = int(input("Enter Age: "))
    user_course = input("Enter Course: ")

    # Use %s placeholders for parameterized queries (prevents SQL injection)
    dynamic_insert = """
    INSERT INTO students (name, age, course) 
    VALUES (%s, %s, %s);
    """
    cursor.execute(dynamic_insert, (user_name, user_age, user_course))
    conn.commit()
    print("✓ Dynamic record inserted successfully.")

    # ==========================================
    # 5. FETCH & DISPLAY ALL RECORDS (fetchone)
    # ==========================================
    print("\n--- Fetching First Record using fetchone() ---")
    cursor.execute("SELECT * FROM students;")
    single_record = cursor.fetchone()
    print("First Record:", single_record)

    # ==========================================
    # 6. SELECT WITH WHERE CONDITION
    # ==========================================
    print("\n--- Fetching Records with WHERE Condition (age > 20) ---")
    where_query = "SELECT * FROM students WHERE age > %s;"
    cursor.execute(where_query, (20,))
    filtered_records = cursor.fetchall()
    
    print("Matching Records:")
    for row in filtered_records:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]}")

    # ==========================================
    # 7. TRUNCATE TABLE (Clean up table data)
    # ==========================================
    print("\n--- Performing TRUNCATE Operation ---")
    cursor.execute("TRUNCATE TABLE students;")
    conn.commit()
    print("✓ Table 'students' truncated successfully.")

except Exception as error:
    print("An error occurred during database operations:", error)

