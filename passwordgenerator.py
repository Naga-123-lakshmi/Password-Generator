import random
import string
def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password
if __name__=="__main__":
    try:
        length=int(input("enter the length of password:"))
        if length<=0:
            print("Invalid length")
        else:
            password=generate_password(length)
            print("generated password:",password)
    except ValueError:
        print("Invalid input")
