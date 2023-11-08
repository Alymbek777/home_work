#1
# def aka (num):
#     if '?' in num:
#         print('Конечно')
#     elif 'ВОТ ТАК' in num:
#         print('Успокойся')
#     elif num =='':
#   print("Как классно когда ты молчишь и продолжай в том же духе")
#     else:
#         print('Ну и что')
# num=input("Напиши что нибудь")
# aka(num)


# 2
# word = "Кыргызская Республика"
# split_word = word.split()
# print(split_word)
# res = ""
# for s in split_word:
#     res +=s[0]
# print(res)
# word = "For your interest"
# split_word = word.split()
# print(split_word)
# res = ""
# for s in split_word:
#     print(s)
#     res +=s[0]
# capital = res.upper()
# print(capital)

#3
# aka = {}
# def user(words):
#     text1 = words.lower().split()
#     for name in text1:
#         aka[name] = text1.count(name)
# user("Money, money, money, it's always sunny, in the richmen's world")
# print(aka)

#4
# def sing(word):
#     izogra1 = list(word)
#     izogra2 = set(word)
#     if len(izogra1) == len(izogra2):
#         return True
#     return False
# print(sing("ak"))

#5 
# 1) вариант
# def num():
#     n = 52
#     num_1 = ""
#     for i in str(n):
#         num_1 = i + num_1
#     num_1 = int(num_1)
#     print(f"n = {num_1}")
# num()
# 2) вариант
# def num():
#     user = input("Введите число:")[:: -1] 
#     print(f"Результат: {user}")
# num()