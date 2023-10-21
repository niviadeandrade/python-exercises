#Calculadora IMC#

def testePeso():
  while True:
    try:
       peso1 = float(input("Digite seu peso para calcular o IMC (em kg - ex: 65):"))
       return peso1
    except ValueError:
        print("Entrada inválida")

def testeAltura():
   while True:
      try:
         altura1 = float(input("Digite sua altura para calcular o IMC (em m - ex: 1.67):"))
         if altura1 <=3.00:
            return altura1
         else:
             print("Entrada inválida")
      except ValueError:
           print("Entrada inválida")


peso = testePeso()
altura = testeAltura()
imc = peso / (altura * altura)
if imc < 18.5:
  print("De acordo com a classificação de IMC, seu IMC é Baixo peso")
elif 18.5 <= imc <= 24.9:
  print("De acordo com a classificação de IMC, seu IMC é Normal")
elif 25 <= imc <= 29.9:
  print("De acordo com a classificação de IMC, seu IMC é Sobrepeso")
elif 30 <= imc <= 34.9:
  print("De acordo com a classificação de IMC, seu IMC é Obesidade de grau 1")
elif 35 <= imc <= 39.9:
  print("De acordo com a classificação de IMC, seu IMC é Obesidade de grau 2")
else:
  print("De acordo com a classificação de IMC, seu IMC é Obesidade de grau 3")
