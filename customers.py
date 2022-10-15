class Customers:
    def __init__(self) -> None:
        self._name = None
        self._since = None
        self._age = None
    
    @property   
    def name(self):
        return self._name
    
    @name.setter
    def name(self,nomie):
        self._name = nomie
    
    @property
    def since(self):
        return self._since
    
    @since.setter
    def since(self,since):
        self._since = since
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
    
    def __str__(self) -> str:
        return f"\n  Name: {self._name}\n  Since: {self._since}\n  Age: {self._age}\n"
    
# if __name__== "__main__":
#     custu=Customers()
#     custu.name="nazi"
#     custu.since = 1750
#     custu.age = 19
#     print(custu)