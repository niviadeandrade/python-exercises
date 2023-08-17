print("------- Calculadora Simples -------")

def numero():
  while True:
    try:
      numero =  float(input("Por favor, digite um número: "))
      return numero
    except ValueError:
      print("Entrada Inválida.")
def operador():
  while True:
    try:
      operador = int(input("Escolha seu operador: \n 1. Soma(+) \n 2. Subtração(-) \n 3. Multiplicação(*) \n 4. Divisão(/)\n\n"))
      if 1 <= operador <= 4:
        return operador
      else:
        print("Por favor, digite uma opção válida!")
    except ValueError:
       print("\nEntrada Inválida.")


valor_1 = numero()
valor_2 = numero()
operador = operador()
if operador == 1:
  print("O resultado é: ", valor_1 + valor_2)
elif operador == 2:
  print("O resultado é: ", valor_1 - valor_2)
elif operador == 3:
  print("O resultado é: ", valor_1 * valor_2)
elif operador == 4:
  print("O resultado é: ", valor_1 / valor_2)
else:
  print("Erro")
