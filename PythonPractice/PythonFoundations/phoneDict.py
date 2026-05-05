# Create a phonebook application using a dictionary where users can add, update, delete, and search contacts by name.

def create_phonebook(name, phno):

    global phone_dict
    phone_dict = {}
    phone_dict.update({name:phno})
    print(phone_dict)

def main():
    print("1.Show Phone Book")
    print("2.Add In Phone Book")
    print("Choose The Above Option")
    user = int(input("Here : "))
    if user == 1:
        print(phone_dict)
    if user == 2:
        name = input("Enter The Name : ")
        phno = int(input("Enter The Phone Number : "))
        create_phonebook(name, phno)

main()