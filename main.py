from Customers import Customers
from Members import Members
from Departments import Departments
from Stores import Store
from Enterprise import Enterprise



if __name__ == '__main__':
    
    # declaracion de objetos customers
    c1 = Customers("Gaspar", 2012, 2)
    c2 = Customers("Joaquin", 1990, 20)

    # declaracion de objetos members
    m1 = Members("Lorena", "Gerente")
    m2 = Members("Felipe", "AC")
    m3 = Members("Jose", "AC")
    m4 = Members("Juan", "Gerente")
    m5 = Members("Jorge", "Investigador")
    m6 = Members("Pedro", "Limpieza")
    
    
    # declaracion de objetos departamentos
    d1 = Departments("RRHH", [m1, m2, m3, m1])

    d2 = Departments("I+D", [m4, m5, m6, m4])

    # declaracion de objetos Store
    s1 = Store(0, "Tomas basañes")
    
    s2 = Store(1, "Av. Italia; Bolivia")

    # declaracion de objetos enterprise
    e1 = Enterprise("Dovah Systems", 20000, "10/12/2010", [d1, d2], [c1, c2], [s1, s2])

    e2 = Enterprise("fenware", 14000, "15/07/2015", [d1, d2], [c1, c2], [s1, s2])

    e3 = Enterprise("flask", 14000, "15/07/2015", [d2], [c1], [s1, s2])

    # testeo de funciones
    print("Funcion 1")
    print(e1.__str_department__())
    e1.hay_miembros_repetidos( "I+D")
    e1.hay_miembros_repetidos("RRHH")
    print("despues")
    print(e1.__str_department__())
    print("\n")
    print("----------------------------")
    print("Funcion 2")
    print(e1.existe_presupuesto_suficiente(10.0, 15.0, 20.0, 100.0))
    print("\n")
    print("----------------------------")
    print("Funcion 3")
    e1.definir_roles(["Lorena", "Felipe", "Jose"], ["gerente", "ac", "manager"])
    print(e1.__str_department__())
    print("\n")
    print("----------------------------")
    print("Funcion 4")
    print(e1.es_antiguedad_adecuada())
    print("\n")
    print("----------------------------")
    print("Funcion 5")
    print(e1.obtener_estadisticas_clientes())
    print("\n")
    print("----------------------------")
    print("Funcion 6")
    print(e1.es_sucursal_correcta([0, "Tomas basañes"]))
    print("\n")
    print("----------------------------")
    print("Funcion 7")
    print(e1 == e2)
    print(e1 == e3)
    # print(es_misma_empresa(e1, e2))
    # print(es_misma_empresa(e1, e3))
