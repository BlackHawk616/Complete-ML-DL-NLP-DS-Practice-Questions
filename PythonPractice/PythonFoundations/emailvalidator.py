# Write a program that takes an email as input and checks whether it is valid based on standard rules (presence of @, domain name, no spaces, etc.).

def email_validator():
    print("Welcome to email validator!")
    email = input("Enter an email address: ")
    if "@" in email and "." in email and " " not in email:
        print(f"{email} is a valid email address")
    else:
        print(f"{email} is not a valid email address")
email_validator()