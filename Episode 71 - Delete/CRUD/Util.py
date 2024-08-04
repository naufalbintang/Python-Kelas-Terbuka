import string
import random

def random_string(panjang):
    hasil_str = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasil_str