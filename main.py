import contacts
from os import system

main_message = """ Welcome to Phonebook
-----------------------------
Please choose:
1. add contact
2. find contact
-----------------------------
"""

def prompt_add_contact():
  name = input('Please enter name: ')
  number = input('Number: ')
  print(f'Adding {name} with {number}')
  contacts.add_contact(name, number)

def prompt_get_contact():
  name = input('Search: ')
  number = contacts.get_contact(name)
  if number:
    print(f"{name}'s number is {number}")
  else:
    print(f'{name} does not exist')

def main():
  print(main_message)
  choice = input('Please make your choice: ').strip()
  if choice == '1':
    prompt_add_contact()
  elif choice == '2':
    prompt_get_contact()
  else:
    print('Invalid input')

while True:
  system('clear')
  main()
  input('Press enter to continue: ')