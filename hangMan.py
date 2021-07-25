from random import randint

words = ["Acender", "Afilhado", "Afobado", "Amarelo", "Amendoim", "Amiga", "Amor", "Ardiloso", "Assombração", "Áspero", "Asterisco", "Ave", "Avião", "Avó", "Balão", "Banheiro", "Basquete", "Bebê", "Bolo", "Branco", "Caatinga", "Cachorro", "Cama", "Caminho", "Campeonato", "Caneca", "Capricórnio", "Catapora", "Celular", "Champanhe", "Chiclete", "Chuveiro", "Clube", "Coelho", "Contexto", "Convivência", "Copo", "Coração", "Corrupção", "Crepúsculo", "Desalmado", "Doce", "Elefante", "Eloquente", "Empenhado", "Escola", "Esfirra", "Esparadrapo", "Esquerdo", "Estojo", "Exceção", "Faca", "Forca", "Foto", "Fugaz", "Galáxia", "Garfo", "Geleia", "Girafa", "Gororoba", "Heterossexual", "História", "Horrorizado", "Impacto", "Independência", "Janela", "Limonada", "Magenta", "Manjericão", "Meia", "Menta", "Modernidade", "Moeda", "Mãe", "Noite", "Óculos", "ônibus", "Oftalmologista", "Oração", "Otorrinolaringologista", "Ovo", "Pai", "Palavra", "Paralelepípedo", "Parque", "Passarinho", "Paçoca", "Pedreiro", "Peixe", "Pijama", "Pneumonia", "Pororoca", "Prognósticio", "Pulmão", "Pão", "Quarentena", "Quimera", "Rato", "Refeição", "Reportagem", "Rotatória", "Serenata", "Sino", "Taciturno", "Transeunte", "Trilogia", "Tênue", "Umbigo", "Visceral", "Xícara"]

lives = 7
selected_word = list(words[randint(0, len(words) - 1)].lower())
count_correct = 0
count_all = len(selected_word)
hang_word = list('-' * count_all)
typed_letters = []

def slugify_letter(letter):
  if (letter == "a"):
    return ['a', 'á', 'ã', 'â', 'à']
  if (letter == "e"):
    return ['e', 'é', 'ê']
  if (letter == "i"):
    return ['i', 'í']
  if (letter == "o"):
    return ['o', 'ó', 'õ']
  if (letter == "u"):
    return ['u', 'ú']
  if (letter == "c"):
    return ['c', 'ç']

  return [letter]

while(count_correct < count_all):
  if (lives == 0):
    print(f"Você perdeu ;(. A palavra correta era: {''.join(selected_word)}")
    break

  print(f"\n{' '.join(hang_word)} / Letras digitadas: {' '.join(typed_letters)} / Você tem {lives} vida{'' if lives == 1 else 's'}")
  letter = input("Digite uma letra para a forca: ")
  arr_letter = slugify_letter(letter)
  has_letter = False

  for i in range(len(arr_letter)):
    if (arr_letter[i] in hang_word):
      has_letter = True
      break

    if (arr_letter[i] in selected_word):
      for j in range(len(selected_word)):
        if (selected_word[j] == arr_letter[i]):
          hang_word[j] = arr_letter[i]
          has_letter = True
          count_correct = count_correct + 1

  if (not(has_letter) and not(letter in typed_letters)):
    typed_letters.append(letter)
    lives = lives - 1

if (lives > 0):
  print(f"Parabéns!!! A palavra correta é {''.join(selected_word)}")




