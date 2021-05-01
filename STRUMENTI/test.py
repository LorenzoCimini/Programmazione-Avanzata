from types import FunctionType


def decoratore(func):
    def wrapper(*args):
        print("Sto decorando")
        function = func(*args)
        return function
    return wrapper


class MetaClass(type):
    def __new__(mcs, clsname, supers, clsdict):
        for attrame, attrvalue in clsdict.items():
            if isinstance(attrvalue, FunctionType):
                clsdict[attrame] = decoratore(attrvalue)
        return super().__new__(mcs, clsname, supers, clsdict)


class Person(metaclass=MetaClass):
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return "Nome: {0} - Cognome: {1}".format(self.nome, self.cognome)


lorenzo = Person("Lorenzo", "Cimini")
print(lorenzo)
