import psycopg2

# PRE-REQUISITOS:
# Bajar e instalar Postgre desde https://www.postgresql.org/download/windows/
# Luego crear un esquema, un usuario, darle todos los privilegios mediante:
'''   
    #Show databases
    \l
    #Create database
    create database staff;
    #Connect to a database
    \c staff;
    #Create a new user with a password
    #create user mihai with encrypted password 'python';
    #Show users
    \du
    #Grant privileges on a database to a user
    grant all privileges on database staff to mihai;
    #Create a new schema
    create schema mystaff authorization john;
    #Show schemas
    \dn
    #Deleting a schema / database / user
    drop schema mystaff;
    \c postgres
    drop database staff;
    drop user mihai;
'''
# crear el password de ususario, y crear la DB 'staff'
# Se puede replicar mismo ambiente en MS Access, dado que ya está insatalado en la Laptop de HP.

try:
    connection = psycopg2.connect(database="staff", user = "mihai", password = "python", host = "127.0.0.1", port = "5432")
    
except psycopg2.Error as err:
    print("An error was generated!")
    
else:
    print("Connection to database was successful!")
    
# Crear la conexión a la BD
cursor = connection.cursor()

# Ejecutar script de creación de una tabla
cursor.execute('''create table mystaff.employees
      (id int primary key not null,
       first_name varchar(25) not null,
       last_name varchar(25) not null,
       department varchar(25) not null,
       phone varchar(25),
       address varchar(50),
       salary int);''')
       
# Ejecutar script para insertar registros a la tabla
cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) \
 values (1, 'John', 'Smith', 'Sales', '0123456789', '1st Street, Miami', 50000), \
        (2, 'Jack', 'Doe', 'IT', '0213456742', '2nd Street, NY', 55000), \
        (3, 'Emily', 'Davids', 'Sales', '0123456999', '3rd Street, LA', 59000), \
        (4, 'Karen', 'Willson', 'Logistics', '0823556785', '4th Street, Las Vegas', 41000), \
        (5, 'Emma', 'Richard', 'Marketing', '0423453580', '5th Street, Denver', 40000);")
       
connection.commit()

# Detener ejecución para poder revisar en la BD la correcta ejecución de los scripts.
# En Postgre command prompt ejecutar "select * from mystaff.employees;"
i = input("Pulse cualquier tecla para continuar")

# Ejecutar script que actualiza el departamento al que pertenece Jack Doe
cursor.execute("update mystaff.employees set department = 'Logistics' where last_name = 'Doe';")
connection.commit()

# Detener ejecución para poder revisar en la BD la correcta ejecución de los scripts.
# En Postgre command prompt ejecutar "select * from mystaff.employees;"
i = input("Pulse cualquier tecla para continuar")

# Consultas a la BD y despliege de los resultados en pantalla
cursor.execute("select * from mystaff.employees where salary > 50000;")
records = cursor.fetchall()

print("Empleados cuyo salario es mayor a 50K:")
for record in records:
    print("\t", record)
print()

cursor.execute("select * from mystaff.employees where last_name like '%Richard%';")
records = cursor.fetchall()

print("Empleados cuyo apellido contiene 'Richard':")
for record in records:
    print("\t", record)
print()

cursor.execute("select * from mystaff.employees where salary between 40000 and 45000;")
records = cursor.fetchall()

print("Empleados cuyo salario sea de 40K a 45K:")
for record in records:
    print("\t", record)
print()

cursor.execute("select * from mystaff.employees where department in ('Sales', 'IT');")
records = cursor.fetchall()

print("Empleados cuyo departamento sea Ventas o IT:")
for record in records:
    print("\t", record)
print()

cursor.execute("select * from mystaff.employees where salary between 40000 and 45000;")
records = cursor.fetchone()

print("Registro primero de la consulta:")
for record in records:
    print("\t", record)
print()

records = cursor.fetchmany(size = 2)

print("Siguiente par de registros de la consulta:")
for record in records:
    print("\t", record)
print()

# Detener ejecución para poder revisar en la BD la correcta ejecución de los scripts.
# En Postgre command prompt ejecutar "select * from mystaff.employees;"
i = input("Pulse cualquier tecla para continuar")

# Ejecutar script que borra aquellos empleados cuyo salario sea mayor a 50K
cursor.execute("delete from mystaff.employees where salary > 50000;")
connection.commit()

# Detener ejecución para poder revisar en la BD la correcta ejecución de los scripts.
# En Postgre command prompt ejecutar "select * from mystaff.employees;"
i = input("Pulse cualquier tecla para continuar")

connection.close()