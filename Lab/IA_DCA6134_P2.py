import sqlite3

#step 1: connect to sqlite db (creates company.db if it doesn't exist)
connection = sqlite3.connect("company.db")

# step 2: create a cursor object to execute SQL command
cursor = connection.cursor()

# step 3: Create EMP_DATA table with fields: EMP_ID,NAME,DEPARTMENT 
cursor.execute("""
CREATE TABLE IF NOT EXISTS EMP_DATA(
    EMP_ID INTEGER PRIMARY KEY,
    NAME TEXT NOT NULL,
    DEPARTMENT TEXT NOT NULL
)
""")

# Clear the table before inserting
cursor.execute("DELETE FROM EMP_DATA")

# Step 4: Insert Data of 3 empolyees
cursor.execute("INSERT INTO EMP_DATA VALUES (101,'VASANTH','FINANCE')")
cursor.execute("INSERT INTO EMP_DATA VALUES (102,'VIGNESH','ACCOUNT')")
cursor.execute("INSERT INTO EMP_DATA VALUES (103,'AMLAN','PRODUCTION')")

# Step 5: Update Department of empolyee with ID 102 to 'STORE'
cursor.execute("UPDATE EMP_DATA SET DEPARTMENT = 'STORE' WHERE EMP_ID = 102")

# step 5: Fetch and print the updated 
cursor.execute("SELECT * FROM EMP_DATA WHERE EMP_ID = 102")
updated_row = cursor.fetchone()
print(updated_row)

# step 7: commit changes and close connection
connection.commit()
connection.close()
