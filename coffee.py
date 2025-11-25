class Coffee:
    _all =[]
    def __init__(self, name:str):
        self.name = name
        Coffee._all.append(self)

        def __repr__(self):
            return f"COffee({self.name!r})"
        
        @property 
        def name(self):
            return self._name
        
        @name.setter
        def name(self,value):
            if not isinstance (value, str):
                raise TypeError("Coffee name must be a string")
            value = value.strip()
            if len(value)<3:
                raise ValueError("Coffee name must be at least 3 characters long")
            self._name = value

            def orsers(self):
                from order import Order
                return [o for o in Order._all if o.coffee is self]
            
            def customers(self):
                seen =[]
                for o in self.orders():
                    if o.customer not in seen:
                        seen.append(o.customers)
                return seen 
            


