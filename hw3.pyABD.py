# Задание 1
# age = int(input("Введите ваш возраст: "))
# if age<18:
#     print("Вы являетесть несовершеннолетним")
# elif 18<age<65:
#     print("Вы являетесть взрослым")
# else:
#     print("Вы являетесть пожилым")
# # Задание 2
# num1 = int(input("Введите первое число:"))
# num2 = int(input("Введите второе число:")) 
# num3 = int(input("Введите третье число:"))   
# min_num = min(num1,num2,num3)
# print("Наименьшее число:", min_num)

# Задание 3
# user = ["Bishkek", "Asia", "Batken", "Kol", "Aksay","Reutov", "Belka","Tiger","Nookat", "Alay", "Uzgen","Peshka"," Talas","Knopka","Der"]
# print(user[2:8])

# Задние 4
# user = ["Bishkek", "Asia", "Batken", "Kol", "Aksay","Reutov", "Belka","Tiger","Nookat", "Alay"]
# user.pop(2)
# user.pop(8)
# print(user)
# user.append("paplandia")
# user.append("paplandia")
# user.append("paplandia")
# user.append("paplandia")
# user.append("paplandia")
# print(user)

# Задание 5
# user = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# user.pop(2)
# print(user)
# user.remove(16)
# print(user)
# user.insert(0, 5)
# print(user)
# user.insert(0, 9)
# print(user)
# Задание 6
# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8, 909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]
# numbers.sort()
# print(numbers)

# Задание 7
# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8, 909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]
# numbers.reverse()
# print(numbers)

# Задание 8
# numbers = [2,3,1,52,56,8,3,58,0,98,75,3,45,21,44,2,1,4,5,6,8, 909,4,24,653,12,43,2,5,8,5,3,6,8,0,2,12,4,32,5,7,43,8,0,8,654,235,65,2,3,6,0,9,8,6,43,2,4,56,2,36,7,954,2,34,6,8,45,2,4,5,73,1,32,5,321,452,3,]
# print("2: ", numbers.count(2))
# print("3: ", numbers.count(3))
# print("5: ", numbers.count(5))

# Задание 9
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(sum(numbers) / len(numbers))

# # Доп.задание
# numbers = [1,2,3,4,5,6,7,8,9,10,]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# playlist = ["Bishkek", "Asia", "Batken", "Kol", "Aksay","Reutov", "Belka","Tiger","Nookat", "Alay"]
# playlist[3] = 'Tiger'
# playlist[7] = 'Kol'
# print(playlist)

# numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for num in numbers:
#     if num % 2 == 0:
#         numbers.remove(num)
# print(numbers)
