# Perguntar três números para o usuario, e descobrir qual o tipo de triângulo(equilátero, isósceles, escaleno)

# Triângulo Equilátero: três lados iguais 
# Triângulo Isósceles: dois lados iguais
# Triângulo Escaleno: três lados diferentes

ladoa: float
ladob: float
ladoc: float

ladoa = float(input('Digite o lado a: '))
ladob = float(input('Digite o lado b: '))
ladoc = float(input('Digite o lado c: '))

if (ladoa == ladob) and (ladoa == ladoc):
  print('O triângulo é equilátero.')
elif (ladoa == ladob) or (ladoa == ladoc) or (ladob == ladoc):
  print('O triângulo é isósceles.')
else:
  print('O triângulo é escaleno.')