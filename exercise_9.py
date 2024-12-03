import unicodedata

def remover_acento(texto):
    remover = unicodedata.normalize('NFKD', texto)
    return ' '.join([letra for letra in remover if not unicodedata.combining(letra)])


def contar_vogais ():
    while True:
        try:
            texto = str(input("Digita uma frase e direi quantas vogais ela tem:"))
            texto_sem_acentos = remover_acento(texto.lower())
            vogais = "aeiou"
            total_vogais = 0
            continuar = 1
            for v in vogais:
                total_vogais += texto_sem_acentos.count(v)
            print(f"O total de vogais de tua frase é: {total_vogais}")
        except Exception as e:
             print(f"Erro {e}! Favor digitar um texto.")
        while True:
            try:
                continuar = int(input("Deseja continuar? (Sim = 1 / Não = 0): "))
                if continuar == 0:
                    return
                elif continuar > 1:
                    print("Entrada inválida!")
                else:
                    break
            except ValueError: 
                print("Favor digitar um valor válido")
      
contar_vogais()
