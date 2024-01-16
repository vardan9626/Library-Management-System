class Person:
    '''This class is representing a person whose first and last name are immutable it constains the basic info about the person'''
    
    def __init__(self, firstname, lastname, age, address, phonenumber):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.address = address
        self.phonenumber = phonenumber
    
    @property
    def name(self):
        return f"{self.__firstname} {self.__lastname}"
    @property
    def age(self):
        return self.__age
    @property
    def firstname(self):
        return self.__firstname
    @property
    def lastname(self):
        return self.__lastname