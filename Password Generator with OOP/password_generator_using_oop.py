#Password Generator using classes

class Pswrdgen():
        
    def __init__(self):
        import string
        self.pswrd = []
        self.letters_str = string. ascii_letters + string.digits  #Alphanumeric string
        self.special_char_str = string.punctuation   #string of special characters

    #Asking for password length
    def pswrd_length(self):
        while True:
            try:
                self.pswrd_len = int(input("What is the length of your required password?\n"))
            except ValueError:
                print("Enter a valid number.")
                continue
            if self.pswrd_len > self.special_char:
                break
            else:
                print("Length of password should be greater than required number of special characters.")
        return self.pswrd_len    
        
    #asking for required special characters
    def special_char_len(self):
        while True:
            try:
                self.special_char = int(input("How many special characters would you like?\n"))
            except ValueError:
                print("Enter a valid number.")
                continue
            else:
                break
        return self.special_char

    #Generating password
    def genpswrd(self):
        import secrets
        import random
        y = self.special_char_len()
        x = self.pswrd_length()
        z = x-y
        
        while y > 0:
            a = str(secrets.choice(self.special_char_str))
            self.pswrd.append(a)
            y -= 1

        while z > 0:
            pswrd_char = str(secrets.choice(self.letters_str))
            self.pswrd.append(pswrd_char)
            z -= 1

        random.shuffle(self.pswrd)
        return "".join(self.pswrd)

def main():
    ob1 = Pswrdgen()
    print(ob1.genpswrd())


if __name__ == "__main__":
    main()

    
            

        

        
