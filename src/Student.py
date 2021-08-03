
class Student:
    def __init__(self, name:str,surname:str,email:str,album:int,age:int):
        self._name:str = name
        self._surname:str = surname
        self._email:str = email
        self._album:int = album
        self._age:int = age

    def __repr__(self):
        result:str = "Imie {}\nNazwisko {}\nemail {}\nalbum {}\nage {}\n".format(
            self._name, self._surname, self._email, self._album, self._age)
        return result

    @staticmethod
    def getBuilder()->'BuilderStudent':
        return BuilderStudent()


class BuilderStudent:
    def __init__(self):
        self._name:str = str() 
        self._surname:str = str()
        self._email:str = str()
        self._album:int = int()
        self._age:int = int()

    def withName(self,name):
        self._name = name
        return self

    def withSurname(self,surname):
        self._surname = surname
        return self

    def withEmail(self,email):
        self._email = email
        return self

    def withAlbum(self,album):
        self._album = album
        return self

    def withAge(self,age):
        self._age = age
        return self

    def build(self):
        return Student(self._name,self._surname,self._email,self._album,self._age
        )           
