import random


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.id = random.randint(1, 100)
        print('id = ', self.id)


if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 is db2)
    print(db1.id, db2.id)