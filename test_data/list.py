import random
import string


def random_string(length, symbols=None):
    if symbols is None:
        symbols = string.ascii_letters + string.digits + ' ' + string.punctuation
    return ''.join(random.choice(symbols) for i in range(length))

records = ['123', 'new_record'] + \
          [random_string(3), random_string(40), random_string(random.choice(range(3, 40)))] + \
          [random_string(length=3, symbols=string.digits), random_string(length=3, symbols=string.digits),
           random_string(length=random.choice(range(3, 40)), symbols=string.digits)] + \
          [random_string(length=3, symbols=string.punctuation), random_string(length=3, symbols=string.punctuation),
           random_string(length=random.choice(range(3, 40)), symbols=string.punctuation)]

incorrect_records = ['', '12', '.', random_string(2), random_string(41), random_string(128)]
