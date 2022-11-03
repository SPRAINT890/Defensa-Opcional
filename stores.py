class Store:
    def __init__(self, store_id, address) -> None:
        self._store_id = store_id
        self._address = address
    
    @property
    def store_id(self):
        return self._store_id
    
    @store_id.setter
    def store_id(self,store):
        self._store_id = store
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, adrs):
        self._address = adrs
    
    def __str__(self) -> str:
        return f"\n  Storeid: {self._store_id}\n  Address: {self._address}\n"

if __name__ == '__main__':
    s1 = Store()
    s1.storeid = 0
    s1.address = "gral. nariño 2388"
    print(s1)
