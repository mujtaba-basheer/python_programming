def encode (password, n):
    encoded_pass = ""
    
    for ch in password:
        c = ord(ch)
        
        if c >= 65 and c <= 90:
            if c + n > 90:
                a = ((c + n) % 90) + 64
            else:
                a = c + n
        elif c >= 97 and c <= 122:
            if c + n > 122:
                a = ((c + n) % 122) + 96
            else:
                a = c + n
        
        encoded_pass += chr(a)
            
    return encoded_pass

class User:
    def __init__ (self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = encode(password, 13)
        
    def checkUser (self, email, password):
        if email == self.email:
            if self.password == encode(password, 13):
                return True
            else:
                return False
        else:
            return False

first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email: ")
password = input("Password: ")

user = User(first_name, last_name, email, password)

print("\nEnter login details...")

email = input("Email: ")
password = input("Password: ")

if(user.checkUser(email, password)):
    print('Logged in successfully')
else:
    print('Invalid Details')