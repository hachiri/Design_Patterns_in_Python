import random


def singleton(class_):
    instance = {}

    def get_instance(*args, **kwargs):
        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)
        return instance[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        self.id = random.randint(1, 100)
        print('id = ', self.id)


if __name__ == '__main__':
    db1 = Database()
    db2 = Database()
    print(db1 is db2)
    print(db1.id, db2.id)
