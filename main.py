from customers import Customers
from departments import Departments
from stores import Store
from enterprise import Enterprise

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
    d1.section = "I+D"
    d1.members = ["Juan", "Jorge", "Pedro"]
    d1.roles = ["Gerente", "Investigador", "Limpieza"]
    
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
    e1.departments = [d1, d2]
    e1.customers = [c1, c2]
    e1.store = [s1, s2]
    
    print(e1)
