#  Add a person to a phonebook in dictonary

# Phonebook = {}

# while True:
#     print('''
# 1 -> Add a person to phone book
# 2 -> View a person from phonebook
# 3 -> Delete a person from phone book
# 4 -> Change a person from phone number
# 5 -> Change a person name
# 6 -> Show all users in the phonebook
# 7 -> Quit
# ''')
    
#     option = int(input("Enter your option : "))
#     if option == 1:
#         name = input("Enter a user name : ")
#         phone = int(input("Enter the user number : "))
#         person = {
#             "name" : name.lower(),
#             "phone" : phone        
#         }

#         Phonebook[name.lower()] = person

#     elif option == 2:
#         search_person = input("Enter a person to search : ")
#         search_person = search_person.lower()

#         if search_person in Phonebook.keys():
#             print("Person Name : ", Phonebook[search_person]["name"])
#             print("Person Number : ", Phonebook[search_person]["phone"])
#         else:
#             print("Not Found")

#     elif option == 3:
#         delete_person = input("Enter a person to delete : ").lower()
#         if delete_person in Phonebook.keys():
#             del Phonebook[delete_person]

#     elif option == 4:
#         n = input(" Enter a name : ").lower
#         if n in Phonebook.keys():
#             change_num = int(input("Enter a number to be changed : "))
#             Phonebook[n]["phone"] = change_num

#     elif option == 5:
#         person_name = input("Enter a name : ").lower()
#         if person_name in Phonebook.keys():
#             changed_name = input("Enter a name : ")
#             Phonebook[person_name]['name'] = changed_name.lower()
#             poped_person = Phonebook.pop(person_name)
#             Phonebook[changed_name] = poped_person

#     elif option == 6:
#         print(Phonebook)

#     elif option == 7:
#         break