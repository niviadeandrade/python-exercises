def pressao ():
    while True:
        try:
            pressao = int(input("Digite a pressão desejada: "))
            if 1 <= pressao <= 40:
              return pressao
            else:
                print("Por favor digite um valor válido!")
        except ValueError:
            print("Entrada Inválida!")

def pressao_lida ():
    while True:
        try:
            pressao_lida = int(input("Pressão lida pela bomba: "))
            if 1 <= pressao_lida <= 40:
              return pressao_lida
            else:
                print("Pressão inválida!")
        except ValueError:
            print("Pressão Inválida!")

n = pressao()
m = pressao_lida()

print(f"A diferença da pressão desejada e pressão atual é de:", n - m)
