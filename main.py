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

# def existe_presupuesto_suficiente(enterprise1, float_mem_rrhh, float_mem_tec, float_mem_dir, float_ganancia):
# def definir_roles(enterprise1, list_members, list_roles):

def es_antiguedad_adecuada(obj_empresa: object):
    año_actual = 2022
    antiguedad_empresa = obj_empresa.creation.split('/', 3)
    list_obj_customers_empresa = obj_empresa.customers
    for obj_customers in list_obj_customers_empresa:
        if(obj_customers.since < int(antiguedad_empresa[2]) or (año_actual - obj_customers.since) > obj_customers.age ):
            # codigo que se hace cuando hay un cliente que cumple estas condiciones
            print("efe")
            continue


def obtener_estadisticas_clientes(obj_empresa: object):
    list_obj_customers_empresa = obj_empresa.customers
    #declaro las variables sin valor, para no limitar el rango
    minimo_edad = None
    minimo_antiguedad = None
    maximo_edad = None
    maximo_antiguedad = None
    prom_edad = 0
    prom_antiguedad = 0
    for obj_customers in list_obj_customers_empresa:
        #si es la primera iteracion cargo valores a las variables con el primer cliente
        if(minimo_edad is None):
            minimo_edad = obj_customers.age
            minimo_antiguedad = obj_customers.since
            maximo_edad = obj_customers.age
            maximo_antiguedad = obj_customers.since
        
        #Minimos
        if(minimo_edad > obj_customers.age):
            minimo_edad = obj_customers.age
        if(minimo_antiguedad > obj_customers.since):
            minimo_antiguedad = obj_customers.since
        
        #maximos
        if (maximo_edad < obj_customers.age):
            maximo_edad = obj_customers.age
        if (maximo_antiguedad < obj_customers.since):
            maximo_antiguedad = obj_customers.since
        
        #promedio
        prom_antiguedad += obj_customers.since
        prom_edad += obj_customers.age
    
    prom_antiguedad = prom_antiguedad // len(list_obj_customers_empresa)
    prom_edad = prom_edad // len(list_obj_customers_empresa)
    
    mpm_antiguedad = [minimo_antiguedad, prom_antiguedad, maximo_antiguedad]
    mpm_edad = [minimo_edad, prom_edad, maximo_edad]
    return mpm_edad, mpm_antiguedad

# def es_sucursal_correcta(enterprise1, list_id_chars):
# es_misma_empresa (enterprise1, enterprise2):

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
    e1.creation = "10/12/2010"
    e1.departments = [d1, d2]
    e1.customers = [c1, c2]
    e1.store = [s1, s2]
    
    # print(e1.departments)
    # hay_miembros_repetidos(e1, "I+D")
    # hay_miembros_repetidos(e1, "RRHH")
    # 
    # es_antiguedad_adecuada(e1)
    print(obtener_estadisticas_clientes(e1))
