from customers import Customers
from departments import Departments
from stores import Store
from enterprise import Enterprise

def hay_miembros_repetidos(enterprise: object, str_section: str):
    lista_secciones = enterprise.departments
    for seccion in lista_secciones:
        if seccion == str_section:
            lista_miembros = seccion.members
            sin_duplicar = list(set(lista_miembros))
            seccion.members = sin_duplicar

# miembros
def existe_presupuesto_suficiente(obj_empresa: object, float_mem_rrhh: float, float_mem_tec: float, float_mem_dir: float, float_ganancia: float):
    lista_secciones = obj_empresa.departments

def definir_roles(obj_empresa: object, list_members: list, list_roles: list):
    list_obj_departments_empresa = obj_empresa.departments
    
    # creo una matriz transpuesta de members y roles
    m_members_roles = [list_members, list_roles]
    mt_members_roles = []
    for x in range(len(list_members)):
        matrix_x = []
        for y in range(len(m_members_roles)):
            matrix_x.append(m_members_roles[y][x])
        mt_members_roles.append(matrix_x)
    
    for members_roles in mt_members_roles:
        for obj_department_empresa in list_obj_departments_empresa:
            posicion = 0
            for members in obj_department_empresa.members:
                if(members != members_roles[0]):
                    posicion += 1
                    continue
                obj_department_empresa.roles[posicion] = members_roles[1]
                break

def es_antiguedad_adecuada(obj_empresa: object):
    año_actual = 2022
    antiguedad_empresa = obj_empresa.creation.split('/', 3)
    list_obj_customers_empresa = obj_empresa.customers
    for obj_customers in list_obj_customers_empresa:
        if(obj_customers.since < int(antiguedad_empresa[2]) or (año_actual - obj_customers.since) > obj_customers.age ):
            return False
    return True


def obtener_estadisticas_clientes(obj_empresa: object):
    list_obj_customers_empresa = obj_empresa.customers
    
    # declaro las variables sin valor, para no limitar el rango
    minimo_edad = None
    minimo_antiguedad = None
    maximo_edad = None
    maximo_antiguedad = None
    prom_edad = 0
    prom_antiguedad = 0
    
    for obj_customers in list_obj_customers_empresa:
        # Si es la primera iteracion cargo valores a las variables con el primer cliente
        if(minimo_edad is None):
            minimo_edad = obj_customers.age
            minimo_antiguedad = obj_customers.since
            maximo_edad = obj_customers.age
            maximo_antiguedad = obj_customers.since
        
        # Minimos
        if(minimo_edad > obj_customers.age):
            minimo_edad = obj_customers.age
        if(minimo_antiguedad > obj_customers.since):
            minimo_antiguedad = obj_customers.since
        
        # Maximos
        if (maximo_edad < obj_customers.age):
            maximo_edad = obj_customers.age
        if (maximo_antiguedad < obj_customers.since):
            maximo_antiguedad = obj_customers.since
        
        # suma del promedio
        prom_antiguedad += obj_customers.since
        prom_edad += obj_customers.age
    
    # division del promedio
    prom_antiguedad = prom_antiguedad // len(list_obj_customers_empresa)
    prom_edad = prom_edad // len(list_obj_customers_empresa)
    
    mpm_antiguedad = [minimo_antiguedad, prom_antiguedad, maximo_antiguedad]
    mpm_edad = [minimo_edad, prom_edad, maximo_edad]
    return mpm_edad

def es_sucursal_correcta(obj_empresa: object, list_id_chars: list):
    list_stores_empresa = obj_empresa.store
    for tienda in list_stores_empresa:
        if(tienda.store_id != list_id_chars[0]):
            continue
        if(tienda.address != list_id_chars[1]):
            return False
        return True

def es_misma_empresa(obj_empresa1: object, obj_empresa2: object):
    if (obj_empresa1.customers != obj_empresa2.customers or obj_empresa1.departments != obj_empresa2.departments or obj_empresa1.store != obj_empresa2.store):
        return False
    return True

if __name__ == '__main__':
    
    # declaracion de objetos customers
    c1 = Customers()
    c1.name = "Gaspar"
    c1.since = 2012
    c1.age = 2
    
    c2 = Customers()
    c2.name = "Joaquin"
    c2.since = 1990
    c2.age = 20
    
    # declaracion de objetos departamentos
    d1 = Departments()
    d1.section = "RRHH"
    d1.members = ["Lorena", "Felipe", "Jose", "Felipe"]
    d1.roles = ["Gerente", "AC", "AC", "AC"]
    
    d2 = Departments()
    d2.section = "I+D"
    d2.members = ["Juan", "Jorge", "Pedro", "Juan"]
    d2.roles = ["Gerente", "Investigador", "Limpieza", "gerente"]
    
    # declaracion de objetos Store
    s1 = Store()
    s1.storeid = 0
    s1.address = "Tomas basañes"
    
    s2 = Store()
    s2.storeid = 1
    s2.address = "Av. Italia; Bolivia"
    
    # declaracion de objetos enterprise
    e1 = Enterprise()
    e1.name = "Dovah Systems"
    e1.budget = 20000
    e1.creation = "10/12/2010"
    e1.departments = [d1, d2]
    e1.customers = [c1, c2]
    e1.store = [s1, s2]
    
    e2 = Enterprise()
    e2.name = "fenware"
    e2.budget = 14000
    e2.creation = "15/07/2015"
    e2.departments = [d1, d2]
    e2.customers = [c1, c2]
    e2.store = [s1, s2]
    
    e3 = Enterprise()
    e3.name = "flask"
    e3.budget = 14000
    e3.creation = "15/07/2015"
    e3.departments = [d2]
    e3.customers = [c1]
    e3.store = [s1, s2]
    
    
    # testeo de funciones
    # print(e1.departments)
    # hay_miembros_repetidos(e1, "I+D")
    # hay_miembros_repetidos(e1, "RRHH")
    # 
    # es_antiguedad_adecuada(e1)
    # print(obtener_estadisticas_clientes(e1))
    # print(es_misma_empresa(e1, e2))
    # print(es_misma_empresa(e1, e3))
    print(e1)
    definir_roles(e1, ["Lorena", "Felipe", "Jose"], ["gerente", "ac", "manager"])
    print(e1)
