print("Registro de usuarios")
name = input("Introduce tu nombre: ")
surname = input("Introduce tu apellido: ")
country = input("Tu pais de origen: ")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE PyBase")

mycursor.execute("USE PyBase")

sqlreg = "CREATE TABLE users (name VARCHAR(255), surname VARCHAR(255), country VARCHAR(255))"

mycursor.execute(sqlreg)

sql = "INSERT INTO users (name, surname, country) VALUES (%s, %s, %s)"
val = (name, surname, country)
mycursor.execute(sql, val)


print("Todos los datos fueron registrados correctamente xd")
