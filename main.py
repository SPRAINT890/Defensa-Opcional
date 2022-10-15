from itertools import count
from customers import Customers
from departments import Departments
from stores import Store
from enterprise import Enterprise
def hay_miembros_repetidos(enterprise, str_section):
    lista_secciones = enterprise.departments()
    for seccion in lista_secciones:
        if seccion == str_section:
            lista_miembros = seccion.member()
            print(lista_miembros)
            sin_duplicar = [*set(lista_miembros)]
            print(sin_duplicar)
            break
    
if __name__ == '__main__':
    
    # declaracion de objetos customers
    c1 = Customers()
    c1.name = "Gaspar"
    c1.since = 2020
    c1.age = 19
    
    c2 = Customers()
    c2.name = "Joaquin"
    c2.since = 2019
    c2.age = 20
    
    # declaracion de objetos departamentos
    d1 = Departments()
    d1.section = "RRHH"
    d1.members = ["Lorena", "Felipe", "Jose"]
    d1.roles = ["Gerente", "AC", "AC"]
    
    d2 = Departments()
    d2.section = "I+D"
    d2.members = ["Juan", "Jorge", "Pedro", "juan"]
    d2.roles = ["Gerente", "Investigador", "Limpieza"]
    
    # declaracion de objetos Store
    s1 = Store()
    s1.storeid = 0
    s1.address = "Tomas basañes"
    
    s2 = Store()
    s2.storeid = 1
    s2.address = "Av. Italia y Bolivia"
    
    # declaracion de objetos enterprise
    e1 = Enterprise()
    e1.name = "Dovah Systems"
    e1.budget = 20000
    e1.creation = "10/12/2022"
    e1.departments = [str(d1), str(d2)]
    e1.customers = [str(c1), str(c2)]
    e1.store = [str(s1), str(s2)]
    
    # print(e1)
    hay_miembros_repetidos(e1, "I+D")
