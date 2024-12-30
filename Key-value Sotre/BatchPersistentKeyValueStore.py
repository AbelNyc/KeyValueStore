import json 
import threading
from KeyValueStore import KeyValueStore
class BatchPersistentKeyValueStorage(KeyValueStore):
    def __init__(self, filepath = "store.json",
                 batch_size = 5,
                 auto_save_interval = 10 
                 ):
        super().__init__()
        self.filepath = filepath
        self.batch_size = batch_size
        self.counter = 0
        self.lock = threading.Lock()
        self.load_store()

        self.auto_Save_thread = threading.Thread(target=auto_save_interval,
                                                 daemon=True)
        self.auto_Save_thread.start()
    def mark_counter(self):
        
        with self.lock:
            self.counter+=1
            if self.counter > self.batch_size:
                self.save_store
        
    def save_store(self):
        """
        Save the current state of the store to the file as JSON.
        """
        with self.lock:
            if self.counter > 0:
                with open(self.filepath, "w") as f:
                    json.dump(self.store, f)  # Serialize the in-memory dictionary to the file.
                self.counter = 0 
    def load_store(self):
        """
        Load the state of the store from the file. If the file does not exist,
        initialize an empty dictionary.
        """
        try:
            with open(self.filepath, "r") as f:
                self.store = json.load(f)  # Load JSON data into the dictionary.
        except FileNotFoundError:
            self.store = {}  # If the file doesn't exist, initialize an empty store.
    def auto_save(self):

        while True:
            threading.Event().wait(10)
            self.save_store()
    def create(self, key, value):
        """
        Add a new key-value pair and persist the change to disk.
        """
        super().create(key, value)  # Call the base class's create method.
        self.mark_counter()
    def update(self, key, value):
        """
        Update an existing key-value pair and persist the change to disk.
        """
        super().update(key, value)  # Call the base class's update method.
        self.mark_counter()

    def delete(self, key):
        """
        Remove a key-value pair and persist the change to disk.
        """
        super().delete(key)  # Call the base class's delete method.
        self.mark_counter()

