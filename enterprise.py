class Enterprise:
    def __init__(self, name, budget, creation, departments, customers, store) -> None:
        self._name = name
        self._budget = budget
        self._creation = creation
        self._departments = departments
        self._customers = customers
        self._store = store

    def hay_miembros_repetidos(self: object, str_section: str):
        lista_secciones = self.departments
        for seccion in lista_secciones:
            if seccion == str_section:
                lista_miembros = seccion.members
                sin_duplicar = list(set(lista_miembros))
                seccion.members = sin_duplicar

    def existe_presupuesto_suficiente(self: object, float_mem_rrhh: float, float_mem_tec: float, float_mem_dir: float, float_ganancia: float):
        lista_secciones = self.departments
        gastos_rrhh = 0
        gastos_tec = 0
        gastos_dir = 0
        presupuesto_bool = False

        for seccion in lista_secciones:
            if (seccion.section == "RRHH"):
                gastos_rrhh += len(seccion.members)*float_mem_rrhh
                continue
            if (seccion.section == "Tec"):
                gastos_tec += len(seccion.members)*float_mem_tec
                continue
            if (seccion.section == "Dir"):
                gastos_dir += len(seccion.members)*float_mem_dir
                continue
        if ((gastos_tec + gastos_dir + gastos_rrhh) < float_ganancia):
            presupuesto_bool = True
        return presupuesto_bool

    def definir_roles(self: object, list_members: list, list_roles: list):
        list_obj_departments_empresa = self.departments

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
                for members in obj_department_empresa.members:
                    if (members.name == members_roles[0]):
                        members.rol = members_roles[1]
                        break

    def es_antiguedad_adecuada(self: object):
        año_actual = 2022
        antiguedad_empresa = self.creation.split('/', 3)
        list_obj_customers_empresa = self.customers
        for obj_customers in list_obj_customers_empresa:
            if (obj_customers.since < int(antiguedad_empresa[2]) or (año_actual - obj_customers.since) > obj_customers.age):
                return False
        return True

    def obtener_estadisticas_clientes(self: object):
        list_obj_customers_empresa = self.customers

        # declaro las variables sin valor, para no limitar el rango
        minimo_edad = None
        minimo_antiguedad = None
        maximo_edad = None
        maximo_antiguedad = None
        prom_edad = 0
        prom_antiguedad = 0

        for obj_customers in list_obj_customers_empresa:
            # Si es la primera iteracion cargo valores a las variables con el primer cliente
            if (minimo_edad is None):
                minimo_edad = obj_customers.age
                minimo_antiguedad = obj_customers.since
                maximo_edad = obj_customers.age
                maximo_antiguedad = obj_customers.since

            # Minimos
            if (minimo_edad > obj_customers.age):
                minimo_edad = obj_customers.age
            if (minimo_antiguedad > obj_customers.since):
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
        return mpm_edad, mpm_antiguedad

    def es_sucursal_correcta(self: object, list_id_chars: list):
        list_stores_empresa = self.store
        for tienda in list_stores_empresa:
            if (tienda.store_id != list_id_chars[0]):
                continue
            if (tienda.address != list_id_chars[1]):
                return False
            return True
        return False
    
    # def es_misma_empresa(obj_empresa1: object, obj_empresa2: object):
    #     if (obj_empresa1.customers != obj_empresa2.customers or obj_empresa1.departments != obj_empresa2.departments or obj_empresa1.store != obj_empresa2.store):
    #         return False
    #     return True
    
    def __eq__(self, __o: object) -> bool:
        return self.customers == __o.customers and self.departments == __o.departments and self.store == __o.store

    def __str__(self) -> str:
        return "\nName: {}\nBudget: {}\nCreation: {} \nDepartments: {} \nCustomer: {} \nStore: {}".format(self.name, self.budget, self.creation, self.__str_department__(), self.__str_customers__(), self.__str_store__())

    def __str_department__(self) -> str:
        string = ""
        for department in self.departments:
            string += str(department) + " "
        return string

    def __str_customers__(self) -> str:
        string = ""
        for customers in self.customers:
            string += str(customers) + " "
        return string

    def __str_store__(self) -> str:
        string = ""
        for store in self.store:
            string += str(store) + " "
        return string

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, budget):
        self._budget = budget

    @property
    def creation(self):
        return self._creation

    @creation.setter
    def creation(self, creation):
        self._creation = creation

    @property
    def departments(self):
        return self._departments

    @departments.setter
    def departments(self, departments):
        self._departments = departments

    @property
    def customers(self):
        return self._customers

    @customers.setter
    def customers(self, customers):
        self._customers = customers

    @property
    def store(self):
        return self._store

    @store.setter
    def store(self, store):
        self._store = store

# if __name__ == '__main__':
#     e1 = Enterprise()
#     e1.name = "my empresa"
#     e1.budget = 12000
#     e1.creation = "12-10-12"
#     e1.departments = ["gav", "i+d"]
#     e1.customers = ["gaspar", "joaquin"]
#     e1.store = ["ps", "ms"]
#     print(e1)
