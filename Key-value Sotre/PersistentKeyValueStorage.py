import json  # For JSON serialization/deserialization.
from KeyValueStore import KeyValueStore
class PersistentKeyValueStore(KeyValueStore):
    """
    A persistent key-value store that extends the base KeyValueStore class.
    Data is saved to and loaded from a JSON file for durability.
    """
    def __init__(self, filepath="store.json"):
        """
        Initialize the persistent store. If the file exists, load data from it;
        otherwise, start with an empty store.
        """
        # Correct use of super() in Python 3.
        super().__init__()  # Initialize the base KeyValueStore.
        self.filepath = filepath  # Path to the JSON file where data is persisted.
        self.load_store()  # Load existing data from the file during initialization.

    def save_store(self):
        """
        Save the current state of the store to the file as JSON.
        """
        with open(self.filepath, "w") as f:
            json.dump(self.store, f)  # Serialize the in-memory dictionary to the file.

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

    def create(self, key, value):
        """
        Add a new key-value pair and persist the change to disk.
        """
        super().create(key, value)  # Call the base class's create method.
        self.save_store()  # Save the updated state to disk.

    def update(self, key, value):
        """
        Update an existing key-value pair and persist the change to disk.
        """
        super().update(key, value)  # Call the base class's update method.
        self.save_store()  # Save the updated state to disk.

    def delete(self, key):
        """
        Remove a key-value pair and persist the change to disk.
        """
        super().delete(key)  # Call the base class's delete method.
        self.save_store()  # Save the updated state to disk.
