# Create a persistent store.
from KeyValueStore import KeyValueStore
from PersistentKeyValueStorage import PersistentKeyValueStore
persistent_store = PersistentKeyValueStore()

# Perform operations.
persistent_store.create("name", "Alice")
persistent_store.create("age", 30)

# Restart the program (simulated by creating a new store instance).
new_store = PersistentKeyValueStore()
print(new_store.read("name"))  # Output: Alice
print(new_store.read("age"))   # Output: 30

# Update and delete.
persistent_store.update("name", "Bob")
print(new_store.read("name"))  # Output after restart: Bob
persistent_store.delete("age")
try:
    print(new_store.read("age"))  # Should raise a KeyError after restart.
except KeyError:
    print("Key 'age' not found.")  # Confirms data was deleted.
