from tabulate import tabulate
nombre = "Pepe"
apellido = "Sanchez"
edad = 23
email = "pepito@hotmail.com"
casado = False
hijos = False
amigos = [["Juan"],["Pedro"],["Jose"]]

pelisVistas={'peli1':['Transformers'], 
            'peli2':['Skyfall'],
            'peli3':['Capitana Marvel'],
            'peli4':['Capitana Marvel']}

print("+--------------------------+")
print("|       CONTACTO           |")
print("+--------------------------+")

print(f"| NOMBRE: {nombre}\t \t   |")
print(f"| APELLIDO: {apellido}\t   |")
print(f"| EDAD: {edad}\t\t   |")
print(f"| EMAIL: {email}|")
print("+--------------------------+")
print("----------------------------")
print("\tPELICULAS VISTAS")
print(tabulate(pelisVistas))
print("+--------------------------+")
print("\tLISTA DE AMIGOS")
print("+--------------------------+")
print(tabulate(amigos))

