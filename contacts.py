from replit import db

def add_contact(name, phone_number):
  if name in db:
    print('Name already exists')
  else:
    db[name] = phone_number

def get_contact(name):
  number = db.get(name)
  return number