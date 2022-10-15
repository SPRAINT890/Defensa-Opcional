class Departments:
    def __init__(self) -> None:
        self._section = None
        self._members = None
        self._roles = None

    def __eq__(self, __o: object) -> bool:
        return self.section == __o

    @property
    def section(self):
        return self._section

    @property
    def members(self):
        return self._members

    @property
    def roles(self):
        return self._roles

    @section.setter
    def section(self,section):
        self._section = section

    @members.setter
    def members(self,member):
        self._members = member

    @roles.setter
    def roles(self,role):
        self._roles = role

    def __str__(self) -> str:
        return "sections: {}, members: {}, roles: {}".format(self._section, self._members, self._roles)
    
# if __name__ == "__main__":
#     departments = Departments()
#     departments.section = "gav"
#     departments.members = "Diego"
#     departments.roles = "programer"
#     print(departments)
    
#     if departments == "gav":
#         print("entro")
