from BatchPersistentKeyValueStore import BatchPersistentKeyValueStorage
import threading
store = BatchPersistentKeyValueStorage(batch_size=3)

# Perform operations
store.create("name", "Alices")
store.create("age", 30)
store.create("city", "New York")  # This triggers a save due to batch size.

store.update("name", "Bob")
store.delete("age")  # Changes will be auto-saved after the interval.

# Simulate concurrent updates
def update_store():
    store.create("country", "USA")
    store.update("city", "San Francisco")
    #store.update("city", "Boston")

threads = [
           threading.Thread(target=update_store)
           for _ in range(5)
           ]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
print(store.read("country"))  # Output: USA
print(store.read("city"))    