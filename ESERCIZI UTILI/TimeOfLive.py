import datetime
import time


class MetaClasse(type):
    def __new__(meta, classname, supers, dizionario):
        dizionario['__del__'] = MetaClasse.delete
        return type.__new__(meta, classname, supers, dizionario)

    def __call__(cls, *args):
        instance = super().__call__(*args)
        setattr(cls, str(id(instance)), datetime.datetime.now())
        return instance

    def delete(self, object_to_destroy):
        cls = type(object_to_destroy)
        time_of_birth = getattr(cls, str(id(object_to_destroy)))
        time_of_death = datetime.datetime.now()
        setattr(cls, str(id(object_to_destroy)), time_of_death - time_of_birth)


class Person(metaclass=MetaClasse):
    def __init__(self, nome, cognome, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.stipendio = stipendio


lorenzo = Person("lorenzo", "Cimini", 200)
print(Person.__dict__)
time.sleep(5)
del lorenzo
print(lorenzo)
print(Person.__dict__)
