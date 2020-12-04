def user_information(name, last_name, birth, city, email, telephone):
  print(f"name: {name}; last name: {last_name}; birth: {birth}, city: {city}, email: {email}, telephone: {telephone}")

user_information(
  name = input("Введите имя: "),
  last_name = input("Введите фамилию: "),
  birth = int(input("Введите год рождения: ")),
  city = input("Введите город проживания: "),
  email = input("Введите email: "),
  telephone = input("Введите номер телефона: ")
)