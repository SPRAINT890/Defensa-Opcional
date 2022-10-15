class Enterprise:
    def __init__(self) -> None:
        self._name = None
        self._budget = None
        self._creation = None
        self._departments = None
        self._customers = None
        self._store = None
    
    def __str__(self) -> str:
        return "Name: {}, Budget: {}, Creation: {}, Departments: {}, Customer: {}, Store: {}".format(self.name, self.budget, self.creation, self.departments, self.customers, self.store)
    
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