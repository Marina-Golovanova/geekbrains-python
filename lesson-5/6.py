def digit(s):
  '''Возвращает строку без букв, разделяя слова в список по пробелам'''
  s_new = ""
  for el in s:
    if el.isdigit() or el == " ":
      s_new += el
  return(s_new.split())

subjects = {}
with open('subjects.txt', 'r') as f:
  content = f.readlines()
  for el in content:
    el = el.split()
    subject, lecture, practice, lab = el[0][:-1], digit(el[1]), digit(el[2]), digit(el[3])
    subjects[subject] = sum(map(int, lecture)) + sum(map(int, practice)) + sum(map(int, lab))
print(subjects)
