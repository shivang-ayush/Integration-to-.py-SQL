# import mysql.connector

# # Connect to the database (or create it if it doesn't exist)
# connection = mysql.connector.connect('minedb.db')

# # Create a cursor object to interact with the database
# cursor = connection.cursor()

# # Example: Create a table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS school (
#     Admission_no INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     class INTEGER NOT NULL,
#     section TEXT NOT NULL,
#     roll INTEGER NOT NULL,
#     D_O_B INTEGER NOT NULL,
#     Students_adhar_card_no INTEGER NOT NULL,
#     Whatsapp_no INTEGER NOT NULL,
#     PEN_no INTEGER NOT NULL,
#     Appahar_no INTEGER NOT NULL,
#     School_house_group TEXT NOT NULL,
#     Category TEXT NOT NULL,
#     Religion TEXT NOT NULL,
#     email TEXT NOT NULL,
#     father_name TEXT NOT NULL,
#     father_adhar_card_no INTEGER NOT NULL,
#     father_phone_no INTEGER NOT NULL,
#     father_occupation TEXT NOT NULL,
#     mother_name TEXT NOT NULL,
#     mother_occupation TEXT NOT NULL,
#     mother_adhar_card_no INTEGER NOT NULL,
#     mother_phone_no INTEGER NOT NULL,
#     Full_Address TEXT NOT NULL,
#     Height INTEGER NOT NULL,
#     Weight INTEGER NOT NULL,
#     Blood_group TEXT NOT NULL                                            
# )
# ''')

# # Example: Insert data into the table
# cursor.execute('''
# INSERT INTO school () VALUES (Admission_no, name, class, section, roll, D_O_B, Students_adhar_card_no, Whatsapp_no, PEN_no, Appahar_no, 
#     School_house_group, Category, Religion, email, father_name, father_adhar_card_no, father_phone_no, 
#     father_occupation, mother_name, mother_occupation, mother_adhar_card_no, mother_phone_no, Full_Address, 
#     Height, Weight, Blood_group)
# ''', (11111, 'KnownUserOne', 13, 'Biology', 14, 192091, 123456789012, 854546489494, 9287987, 92864984289,
#       'Silver', 'Gen', 'Hindu', 'knownuser@gmail.com', 'KnownUserOneFatherName', 123456789012, 1234567890,
#       'KnownUserOneFatherOccupation', 'KnownUserOneMotherName', 'KnownUserOneMotherOccupation', 123456789012, 1234567890, 'Pune, Maharashtra',
#       170, 60, 'O+'))

# # Commit the changes and close the connection
# connection.commit()
# connection.close()

# print("Database setup complete!")

# # Just checking the stuff !!!




import mysql.connector

# Connect to the database (or create it if it doesn't exist)
connection = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL host
    user="your_username",  # Replace with your MySQL username
    password="your_password",  # Replace with your MySQL password
    database="minedb"  # Replace with your database name
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Example: Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS school (
    Admission_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    class INTEGER NOT NULL,
    section TEXT NOT NULL,
    roll INTEGER NOT NULL,
    D_O_B DATE NOT NULL,
    Students_adhar_card_no BIGINT NOT NULL,
    Whatsapp_no BIGINT NOT NULL,
    PEN_no BIGINT NOT NULL,
    Appahar_no BIGINT NOT NULL,
    School_house_group TEXT NOT NULL,
    Category TEXT NOT NULL,
    Religion TEXT NOT NULL,
    email TEXT NOT NULL,
    father_name TEXT NOT NULL,
    father_adhar_card_no BIGINT NOT NULL,
    father_phone_no BIGINT NOT NULL,
    father_occupation TEXT NOT NULL,
    mother_name TEXT NOT NULL,
    mother_occupation TEXT NOT NULL,
    mother_adhar_card_no BIGINT NOT NULL,
    mother_phone_no BIGINT NOT NULL,
    Full_Address TEXT NOT NULL,
    Height INTEGER NOT NULL,
    Weight INTEGER NOT NULL,
    Blood_group TEXT NOT NULL                                            
)
''')

# Example: Insert data into the table
cursor.execute('''
INSERT INTO school (
    Admission_no, name, class, section, roll, D_O_B, Students_adhar_card_no, Whatsapp_no, PEN_no, Appahar_no, 
    School_house_group, Category, Religion, email, father_name, father_adhar_card_no, father_phone_no, 
    father_occupation, mother_name, mother_occupation, mother_adhar_card_no, mother_phone_no, Full_Address, 
    Height, Weight, Blood_group
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
''', (
    11111, 'KnownUserOne', 13, 'Biology', 14, '2005-09-12', 123456789012, 8545464894, 9287987, 92864984289,
    'Silver', 'Gen', 'Hindu', 'knownuser@gmail.com', 'KnownUserOneFatherName', 123456789012, 1234567890,
    'KnownUserOneFatherOccupation', 'KnownUserOneMotherName', 'KnownUserOneMotherOccupation', 123456789012, 1234567890, 
    'Pune, Maharashtra', 170, 60, 'O+'
))

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Database setup complete!")