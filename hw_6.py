# #1
# dictinary_1 = {'a':300,'b':400}
# dictinary_2 = {'c':500,'d':600}
# dictinary_1.update(dictinary_2)
# print(dictinary_1)
# 2
# numbers = {'num_1':1, 'num_2':2, 'num_3':3, 'num_100':100}
# print(numbers['num_1' ] * 5) 
# print(numbers['num_2'] * 5)
# print(numbers['num_3'] * 5)
# print(numbers['num_100'] * 5)
# 3
# student = {'name': 'Askhat', 'age': 17}
# print(student['age'] * 2)
# 4
# student = {'name': 'Askhat', 'age': 17, 'color': 'White'}
# student ['age'] = 16
# print(student['age'])

# #5
# student = {'name': 'Askhat', 'age': 17}
# student.pop('age')
# print(student)

# #6
# student = {'name': 'Askhat', 'age': 17}
# student.setdefault('adress', 'Западный анар')
# print(student)

# 7
# while True:
#     password = input("Введите новый пароль: ")
#     if len(password) < 8:
#         print("Короткий пароль")
#     elif '123' in password:
#         print("Простой пароль")
#     else: 
#         break
# while True:
#     aka_password = input("Введите парль еще раз: ")
#     if password != aka_password:
#         print("Различаются")
#     else:
#         print("Пароль создан")
#         break