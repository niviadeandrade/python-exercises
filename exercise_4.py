#solicitar entrada de strings e contar as vogais
texto = input("Por favor digite um texto, frase ou trecho de música, que contarei o total das vogais:")
vogais  =("AaEeIiOoUu"
)
contagem = 0
print(texto)

for x in texto:
  if x in vogais:
    contagem += 1


print(f"O total de vogais é:",{contagem})
