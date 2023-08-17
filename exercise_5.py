import unicodedata

def acentos_off(input_str):
    forma_nkfd = unicodedata.normalize('NFKD', input_str)
    return ''.join([letra for letra in forma_nkfd if not unicodedata.combining(letra)])

word = str(input("Digite uma palavra ou frase que direi se ela é palíndromo: ")).lower()
sem_caractere = word.replace(",", "").replace(" ", "").replace("!","").replace(".","").replace("-","").replace("_","")
sem_acento = acentos_off(sem_caractere)
reverso = sem_acento[::-1]
if sem_acento == reverso:
  print(f"A palavra/frase ", word, "é palíndromo!")
else:
  print("Sua palavra/frase não é palíndromo")
