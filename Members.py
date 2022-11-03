class Members:
    def __init__(self, name, rol) -> None:
        self._name = name
        self._rol = rol
    
    def __str__(self) -> str:
        return "\n  name: {}\n  rol: {}".format(self._name, self._rol)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, rol):
        self._rol = rol

# if __name__ == "__main__":
#     member = Members("gaspar", "gerente")
#     print(member.name)
