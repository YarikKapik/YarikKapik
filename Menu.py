import random

#символы
a = "qwertyuiopasdfghjklzxcvbnm"
b = "QWERTYUIOPASDFGHJKLZXCVBNM"
c = "1234567890"
d = "_"

while True:
  length = int(input('количество символов>>')) #ввод количиство символов
  ren = int(input('количество сгенерированых паролей>>')) #кол-во сгенерированых паролей
  
  #генерация пароля и кол-во сгенерированых
  for i in range(ren):
      all = a + b + c + d 
      password = "".join(random.sample(all,length)) #генерация пароля и запись в password
      print(password) #ввывод
