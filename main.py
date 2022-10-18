from customers import Customers
from departments import Departments
from stores import Store
from enterprise import Enterprise

def hay_miembros_repetidos(enterprise: object, str_section: str):
    lista_secciones = enterprise.departments
    for seccion in lista_secciones:
        if seccion == str_section:
            lista_miembros = seccion.members
            sin_duplicar = [*set(lista_miembros)]
            seccion.members = sin_duplicar

# def existe_presupuesto_suficiente(enterprise1, float_mem_rrhh, float_mem_tec, float_mem_dir, float_ganancia):
# def definir_roles(enterprise1, list_members, list_roles):

def es_antiguedad_adecuada(obj_empresa: object):
    año_actual = 2022
    antiguedad_empresa = obj_empresa.creation.split('/', 3)
    list_obj_customers_empresa = obj_empresa.customers
    for obj_customers in list_obj_customers_empresa:
        # la condicion esta mal
        if(not obj_customers.since > int(antiguedad_empresa[0]) or obj_customers.since > obj_customers.age ):
            print("efe")
            continue


# def obtener_estadisticas_clientes(enterprise1):
# def es_sucursal_correcta(enterprise1, list_id_chars):
# es_misma_empresa (enterprise1, enterprise2):

if __name__ == '__main__':
    
    # declaracion de objetos customers
    c1 = Customers()
    c1.name = "Gaspar"
    c1.since = 2020
    c1.age = 19
    
    c2 = Customers()
    c2.name = "Joaquin"
    c2.since = 1990
    c2.age = 20
    
    # declaracion de objetos departamentos
    d1 = Departments()
    d1.section = "RRHH"
    d1.members = ["Lorena", "Felipe", "Jose", "Felipe"]
    d1.roles = ["Gerente", "AC", "AC"]
    
    d2 = Departments()
    d2.section = "I+D"
    d2.members = ["Juan", "Jorge", "Pedro", "Juan"]
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
    e1.departments = [d1, d2]
    e1.customers = [c1, c2]
    e1.store = [s1, s2]
    
    # print(e1.departments)
    hay_miembros_repetidos(e1, "I+D")
    hay_miembros_repetidos(e1, "RRHH")
    
    es_antiguedad_adecuada(e1)
    
