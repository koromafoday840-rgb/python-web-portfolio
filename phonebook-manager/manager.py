phonebook = {}
print("___Interactive Phonebook Manager___")

while True:
    print("\nAction: [1] add/update [2] delete [3] search [4] view all [5] exit")
    choice = input("select an option: ").strip()
    
    if choice == "1":
        name = input("enter contact name: ").strip()
        number = input("enter the contact number for " + name + ": ").strip()
        phonebook[name] = number
        print(f"success: {name} saved")
        
    elif choice == "2":
        name = input("enter name to delete: ").strip()
        if name in phonebook:
            del phonebook[name]
            print(f"success: {name} removed")
        else:
            print("error: contact not found")
            
    elif choice == "3":
        name = input("enter search name: ").strip()
        result = phonebook.get(name, 'contact not found')
        print(f"result: {result}")
        
    elif choice == "4":
        if not phonebook:
            print("phonebook is currently empty")
        else:
            for name, number in phonebook.items():
                print(f"{name}: {number}")
                
    elif choice == "5":
        print("Exiting system. goodbye!")
        break
        
    else:
        print("invalid choice. please try again")
  
