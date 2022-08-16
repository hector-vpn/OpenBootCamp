from tokenize import PseudoExtras


print("+---------------------------------------+")
print("|   \tCalculadora IMC                 |")
print("+---------------------------------------+")
peso = float(input("| >> Introduzca su peso [Kg]="))
print("+---------------------------------------+")
alt = float(input("| >>Introduza su altura [m]="))
imc = peso / alt**2

print("+---------------------------------------+")
print(f"Su IMC = [{imc:.2f}]")
print("+---------------------------------------+")
