import random
import string

def generate_password(length: int = 30):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password

password = generate_password()
print(f"Generated password: {password}")



