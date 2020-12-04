def int_func(word):
  """Возвращает слово с заглавной буквой"""
  first_small_letter = word[0]
  first_big_letter = chr(ord(first_small_letter) - ord('a') + ord('A'))
  return first_big_letter + word[1::]

def int_func_2():
  """Возвращает список слов с заглавными буквами"""
  words = input("Введите слова: ").split(" ")
  words_new = []
  for word in words:
    word_new = int_func(word)
    words_new.append(word_new)
  return words_new

print(*int_func_2())
