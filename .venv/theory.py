# Function

# print("Rock my microphone", "5")
# print("Freestyle", "10")
# print("\n\n\n")
# print("\tHello,world!")
# print('Egni book\'s')
# print("Johny\'s \\Cage")
# Int Function
# print(-10 + -2 % 2.5)
# print(6 ** 4)
# print(min(6, 2, 0, 4))
# print(max(9, 7, 0, 3))
# print(abs(-7))
# print(pow(2, 3))
# print(round(3.59993123))

# Getting value/meaning
# ==, !=, <, >, <=, >=

# print(hobby)

# data = 'Info'
# if data == 'Info':
#    correct = True
# else:
#    correct = False
#
# correct = True if data == 'Info' else False
# print(correct)

# Some program
# a = float(input("Enter num 1:")) # int
# b = input("Enter num 2:") # string
#
# a /= 2
# print(a + float(b))

# Cycle
# for i in range(-5, 16, 5):
#     print("El: ", i)
#
# print("\n\n\n\n")
#
# word = 'Some text'
# for i in word:
#     if i == 'm':
#         print('m in word')

# Cycle while
# i = 100
# while i >= 10:
#     print(i)
#     i -= 10

# Operator in cycle

# for i in range(1, 11):
#
#     if i % 2 == 0:
#         continue
#
#     if i == 7:
#         break
#
#     print("EL:", i)

# Else for cycle

# for i in "Hello world":
#     if i =='l':
#         print("Done")
#         break
# else:
#     print("Not found")

# Massive
#
# nums = [5, 7, -4, 5.45, 6, 6]
# nums[0] = 34.34
# # print(nums[3])
#
# nums2 = [5, 7, 3, [5, "Text", False]]
# # print(nums2[-1][-1])
#
# nums.append(45) # додавання нового елементу в кінець вашого списку
# nums.insert(1, False) # вставити новий елемент, по конкретному індексу
# # nums.extend(nums2) # додавання списку до списку
#
# nums.sort() # сртування списку/списків
# nums.reverse() # функція перевертае список
# # nums.pop() # видалиння останього елементу в списку
#
# nums.remove(34.34) # видаляе елемент по значенню
# # nums.clear() # повністю очищае список
#
# print(nums.count(6)) # функція дозволяє дізнатися скільки елементів є з певним значенням
# print(nums)
# print(len(nums)) # функція дозволяє дізнатися довжину списку(кількість)

# Massive and cycle
#
# nums = [5, 3, 2, 6.5]
#
# for el in nums:
#     res = el ** 2
#     print(res)

# Work with text

# word = list('itproger') # створення змінної (список)
# word[0] = 'I'  # звернення до індексу
# word.append('!') # додавання символа в кінець значення
# result = ','.join(word)  # поєднання
# print(result.upper())

# print(result.upper()) # перетворення символів в верхній регістр
# print(result.lower()) # перетворення символів в нижній регістр
# print(result.capitalize()) # перетворення перешого символа в слові в верхній регістр
# print(result.isupper()) # перевірка символа, чи він в верхньому регістрі
# print(result.islower()) # перевірка символа, чи він в нижньому регістрі

# text = 'football,basketball,skate,drive' # ствроли змінну
# hobbies = text.split(',') # ще одна змінна зі зверненням функції
# Цикл ітерації
# for i in range(0, len(hobbies)): # звернення до змінної "і" в діапазоні "hobbies"
#     hobbies[i] = hobbies[i].capitalize() # Функція
#
# result = ','.join(hobbies) # отримання текстового напису з об'єднанням ","
# print(hobbies)

# Індекси та зрізи

# lis = [5, 3, True, "Some", [5, 4]] #список з єлементами(значення)
# print(lis[:-4:-1]) # звернення до певногоj єлементу *індекс:номер:крок вибору*