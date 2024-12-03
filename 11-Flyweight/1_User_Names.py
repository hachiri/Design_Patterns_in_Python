import string
import random


class User:
    strings = []

    def __init__(self, full_name):
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x) for x in full_name.split(' ')]

    def __str__(self):
        return ' '.join(self.strings[x] for x in self.names)


def random_string():
    char = string.ascii_lowercase
    return ''.join(random.choice(char) for i in range(10))


if __name__ == '__main__':
    user = []
    first_names = [random_string() for i in range(100)]
    last_names = [random_string() for i in range(100)]

    for first in first_names:
        for last in last_names:
            user.append(User(f'{first} {last}'))

    print(user[0])
