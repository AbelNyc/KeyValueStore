class KeyValueStore:
     """
    A basic in-memory key-value store implementation with CRUD functionality.
    """
     def __init__(self):
        self.store = dict()
     def create(self, key, value ):
        """
        Add a new key-value pair to the store.
        Raises an error if the key already exists.
        """ 

        if key not in self.store:
            self.store[key] = value
        else:
            raise KeyError("Already Exists.")
        
     def read(self, key):
        """
        Retrieve the value associated with the given key.
        Raises an error if the key does not exist.
        """ 
        if key not in self.store:
            raise KeyError("Key doesn't Exist.")
        return self.store[key]
     
     def update(self, key, value):
        if key not in self.store:
            raise KeyError("Key doesn't Exist.") 
        self.store[key] = value
     def delete(self, key):
         if key not in self.store:
            raise KeyError("Key doesn't Exist.")
         del self.store[key] 
