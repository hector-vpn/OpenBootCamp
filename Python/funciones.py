import math
def areaTriangulo(altura, base):

    area = ((base * altura)/2)
    
    return area

def areaCirculo(radio):

    area = (math.pi * (radio ** 2))

    return area

print(f"Area del triangulo [{areaTriangulo(4,2):.2f}]")
print(f"Area del circulo [{areaCirculo(4):.2f}]")