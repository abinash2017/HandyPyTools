import secrets
import string
from datetime import datetime

upper = string.ascii_uppercase
lower = string.ascii_lowercase
number = string.digits
symbol = string.punctuation
position = [upper,lower,number,symbol]

def get_password(length=12):
    password = ""
    for _ in range(length):
        random_chice = secrets.choice(position)
        x = secrets.choice(random_chice)
        password += x
    return password
current_time = datetime.now()

