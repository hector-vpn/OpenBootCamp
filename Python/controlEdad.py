
edad = int(input(">> Ingrese su edad: "))

if(edad < 18 and edad > 0):
    print(">> Todavia no alcanzo la mayoria de edad")
elif(edad > 112 or edad < 0):
    print("Edad encorrecta")
else:
    print("Es mayor de edad")
