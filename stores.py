class Store:
    def __init__(self) -> None:
        self._store_id = None
        self._address = None
    
    @property
    def storeid(self):
        return self._store_id
    
    @storeid.setter
    def storeid(self,store):
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
