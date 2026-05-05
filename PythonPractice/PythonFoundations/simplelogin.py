# Creating a simple login system

# Create a dictornay to store the username and password
def create_user():
    users = {}
    while True:
        username = input("Enter a username : ")
        if username in users:
            print("username already exists")
        else:
            password = input("Enter a password : ")
            users[username] = password
            print("user created sucessfully")
            break
    return users

def login(users, username, password):
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    users = create_user()
    while True:
        username = input("Enter your username to login: ")
        password = input("Enter your password: ")
        login(users, username, password)

if __name__ == "__main__":
    main()