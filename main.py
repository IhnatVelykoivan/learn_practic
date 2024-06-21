# Practic work

# Hello = True
# while Hello:
#     user_input = input("Enter letter: ")
#     if user_input == 'l':
#         print("Hello World!")
#         continue
#     if user_input == 'd':
#         print("You Doomed!")
#         continue
#     if user_input == 'o':
#         Hello = False
#         print("Oh, no!")
#     else:
#         print("Not found") #


# user_count_hobby = int(input("Enter hobby number: "))
#
# i = 0
# hobby = []
# while i < user_count_hobby:
#     text = "Enter hobby: " + str(i + 1) + ": "
#     hobby.append(input(text))
#
#     i += 1
#
# print(hobby)



# num = int(input("Enter num: "))
# Happy = True
# if num <= 5:
#     print("I'm happy!")  # I'm Happy!
# else:
#     print("I'm don't happy!")
#     correct = True
#
# if num == 11:
#         print("Oh No! Doomed!")
#         pass
# if num == 4:
#     print("\tNum is \n4")  # \t \n
#     pass
#
# print("Bye!")



# work = True
# while work:
#     user_input = input("Enter word STOP: ")
#     if user_input =='STOP':
#         work = False
#
# print("While loop is done")



# user_count_hobby = int(input("Enter hobby number: "))

# i = 0
# hobby = []
# while i < user_count_hobby:
#     text = "Enter hobby: " + str(i + 1) + ": "
#     hobby.append(input(text))
#
#     i += 1


# text = 'f,b,c,a'
# hobbies = text.split(',')
#
# for i in range(0, len(hobbies)):
#     hobbies[i] = hobbies[i].capitalize()
# result = ','.join(hobbies)
# print(hobbies)


# person = {'name': 'Alex', 'age': 15, 'sex': 'Man'}
#
# for key, values in person.items():
#     print(key, values, sep=" - ")




# people = {
#     'user_1': {
#         'name': 'John',
#         'age': 27,
#         'address': ('Seattle', 'Some street', 345),
#         'grades': {'math': 5, 'physics': 2}
#     },
#     'user_2': {
#        'name': 'Kate',
#         'age': 23,
#         'address': ('Seattle', 'Some street', 244),
#         'grades': {'math': 4, 'physics': 4},
#     },
#     'user_3': {
#         'name': 'Stive',
#         'age': 25,
#         'address': ('Seattle', 'Some street', 135),
#         'grades': {'math': 3, 'physics': 5},
#     }
# }
# work = True
# while work:
#     user_input = input("Enter number 1-3: ")
#     if user_input == '1':
#         print(people['user_1'])
#         continue
#     if user_input == '2':
#         print(people['user_2'])
#         continue
#     if user_input == '3':
#         print(people['user_3'])
#         continue
# else:
#     user_input <= '4':
#     print('Not found!')
#     work = False
#     break


people = { # constans
    'user_1': {
        'name': 'John',
        'age': 27,
        'address': ('Seattle', 'Some street', 345),
        'grades': {'math': 5, 'physics': 2}
    },
    'user_2': {
       'name': 'Kate',
        'age': 23,
        'address': ('Seattle', 'Some street', 244),
        'grades': {'math': 4, 'physics': 4},
    },
    'user_3': {
        'name': 'Steve',  # виправлено ім'я
        'age': 25,
        'address': ('Seattle', 'Some street', 135),
        'grades': {'math': 3, 'physics': 5},
    }
}

work = True
while work:
    user_input = input("Enter number 1-3: ")
    if user_input == '1':
        print(people['user_1'])
    elif user_input == '2':
        print(people['user_2'])
    elif user_input == '3':
        print(people['user_3'])
    else:
        print('Not found!')
        work = False
