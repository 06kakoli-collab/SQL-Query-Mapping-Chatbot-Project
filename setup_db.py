import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS students (student_id INT PRIMARY KEY, name VARCHAR(100), department VARCHAR(50), year INT, cgpa DECIMAL(3,2), attendance INT)")


cursor.execute("CREATE TABLE IF NOT EXISTS subjects (subject_id INT PRIMARY KEY, subject_name VARCHAR(100), department VARCHAR(50))")


cursor.execute("CREATE TABLE IF NOT EXISTS fees (fee_id INT PRIMARY KEY, student_id INT, total_fee INT, paid_fee INT, FOREIGN KEY (student_id) REFERENCES students(student_id))")


cursor.execute("CREATE TABLE IF NOT EXISTS placements (placement_id INT PRIMARY KEY, student_id INT, company_name VARCHAR(100), package_lpa DECIMAL(5,2), status VARCHAR(50), FOREIGN KEY (student_id) REFERENCES students(student_id))")


cursor.execute("INSERT OR IGNORE INTO students VALUES (1, 'Kakoli Chakrovortty', 'CSE', 3, 8.5, 80)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (2, 'Shubham Mishra', 'CSE', 2, 7.2, 65)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (3, 'Omisha Panda', 'ECE', 3, 6.8, 72)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (4, 'Aditi Priya', 'ME', 4, 9.1, 90)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (5, 'Kushal Das', 'CSE', 1, 5.5, 55)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (6, 'Sneha Mitro', 'ECE', 2, 8.0, 85)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (7, 'Sumit Singh', 'ME', 3, 7.8, 78)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (8, 'Nayan Kumar', 'CSE', 4, 9.5, 95)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (9, 'Ayush Singh', 'ECE', 1, 6.1, 60)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (10, 'Mohit Taurani', 'ME', 2, 7.0, 70)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (11, 'Harsh Patel', 'CSE', 3, 8.8, 88)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (12, 'Parijat Banerjee', 'ECE', 4, 5.9, 50)")


cursor.execute("INSERT OR IGNORE INTO fees VALUES (1, 1, 80000, 80000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (2, 2, 80000, 60000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (3, 3, 70000, 70000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (4, 4, 75000, 50000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (5, 5, 80000, 30000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (6, 6, 70000, 70000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (7, 7, 75000, 75000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (8, 8, 80000, 80000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (9, 9, 70000, 40000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (10, 10, 75000, 75000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (11, 11, 80000, 60000)")
cursor.execute("INSERT OR IGNORE INTO fees VALUES (12, 12, 70000, 35000)")


cursor.execute("INSERT OR IGNORE INTO placements VALUES (1, 1, 'TCS', 6.5, 'Placed')")
cursor.execute("INSERT OR IGNORE INTO placements VALUES (2, 2, 'Infosys', 4.5, 'Placed')")
cursor.execute("INSERT OR IGNORE INTO placements VALUES (3, 4, 'Google', 45.0, 'Placed')")
cursor.execute("INSERT OR IGNORE INTO placements VALUES (4, 6, 'JP Morgan', 5.0, 'Placed')")
cursor.execute("INSERT OR IGNORE INTO placements VALUES (5, 8, 'Microsoft', 50.0, 'Placed')")
cursor.execute("INSERT OR IGNORE INTO placements VALUES (6, 11, 'Amazon', 35.0, 'Placed')")
cursor.execute("INSERT OR IGNORE INTO placements VALUES (7, 3, 'None', 0, 'Not Placed')")
cursor.execute("INSERT OR IGNORE INTO placements VALUES (8, 5, 'None', 0, 'Not Placed')")


cursor.execute("INSERT OR IGNORE INTO subjects VALUES (1, 'Data Structures', 'CSE')")
cursor.execute("INSERT OR IGNORE INTO subjects VALUES (2, 'Operating Systems', 'CSE')")
cursor.execute("INSERT OR IGNORE INTO subjects VALUES (3, 'Basic electrical engineering', 'ECE')")
cursor.execute("INSERT OR IGNORE INTO subjects VALUES (4, 'Data Structures Algorithm', 'ME')")
cursor.execute("INSERT OR IGNORE INTO subjects VALUES (5, 'Database Management', 'CSE')")

conn.commit()
conn.close()

print("done!")