phonebook = {}
print("___Interactive Phonebook Manager___")
while True:
  print()
  print("Action: [1] add/update [2] delete [3] search [4] view all [5] exit")
  choice = input("select an option")
  if choice == "1":
    name = input("enter contact name").strip()
    number = input("enter the contact number").strip()
    phonebook[name] = number
    print(f"success: {name} saved")
  elif choice == "2":
    name = input("enter name to delete").strip()
    if name in phonebook:
      del phonebook[name]
    else:
      print("error. contact not found")
  elif choice == "3":
    name = input("search name").strip()
    result = phonebook.get(name, 'contact not found')
    print(f"result: {result}")
  elif choice == "4":
    if not phonebook:
      print("phonebook is currently empty")
    else:
      for name, number in phonebook.items():
        print(f"- {name} {number}")
  elif choice == "5":
    print("exiting system. goodbye!")
    break
  print("invalid choice. please try again")  
    
    
  
