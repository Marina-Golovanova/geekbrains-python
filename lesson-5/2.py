with open("text.txt") as f:
  content = f.readlines()
  print(f"Количество строк: {len(content)}")
  for index, el in enumerate(content):
    print(f"Количество слов в строке {index+1}: {len(el)-1}")
