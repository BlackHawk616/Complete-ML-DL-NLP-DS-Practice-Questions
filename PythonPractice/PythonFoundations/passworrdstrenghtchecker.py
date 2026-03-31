# Create a program that evaluates a password and classifies it as Weak, Medium, or Strong based on criteria like length, uppercase/lowercase letters, numbers, and special characters.
def password_strength_checker():
    print("Welcome to password strength checker!")
    password = input("Enter a password: ")
    if len(password) < 6:
        print("Password is Weak")
    elif len(password) < 10 and password.isalnum() and not password.isalpha() and not password.isdigit() and not password.islower() and not password.isupper():
        print("Password is Medium")
    else:
        print("Password is Strong")