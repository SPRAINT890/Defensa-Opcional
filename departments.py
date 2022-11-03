class Departments:
    def __init__(self, section, members) -> None:
        self._section = section
        self._members = members

    def __eq__(self, __o: object) -> bool:
        return self.section == __o

    @property
    def section(self):
        return self._section

    @property
    def members(self):
        return self._members

    @section.setter
    def section(self,section):
        self._section = section

    @members.setter
    def members(self,member):
        self._members = member

    def __str__(self) -> str:
        return "\n  sections: {}\n  members: {}\n".format(self._section, self.__str_members__())
    
    def __str_members__(self) -> str:
        string = ""
        for member in self.members:
            string += str(member) + " "
        return string
    
# if __name__ == "__main__":
#     departments = Departments()
#     departments.section = "gav"
#     departments.members = "Diego"
#     departments.roles = "programer"
#     print(departments)
    
#     if departments == "gav":
#         print("entro")
