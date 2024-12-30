# Key-Value Store with Scalability and Persistence

This project implements a **Key-Value Store** with features like **CRUD operations**, **persistence**, and **batch saving** for scalability. It demonstrates the principles of **reliability**, **scalability**, and **maintainability** as discussed in Chapter 1 of *Designing Data-Intensive Applications* (DDIA).

---

## Features

### **1. Basic Key-Value Store**
- Implements `create`, `read`, `update`, and `delete` operations.
- Handles errors like duplicate keys or missing keys gracefully.

### **2. Persistent Storage**
- Extends the in-memory store to save data to disk using JSON.
- Ensures durability by reloading data from disk on restart.

### **3. Scalability with Batch Saving**
- Reduces frequent disk writes by batching changes and saving them together.
- Includes an **auto-save thread** for periodic persistence.

### **4. Thread Safety**
- Uses locks to handle concurrent operations and prevent race conditions.

### **5. Extensibility**
- Modular design allows easy integration of alternate storage mechanisms (e.g., SQLite).

---

## Class Design

### **1. `KeyValueStore`**
- A basic in-memory store that handles CRUD operations.

#### Methods:
- `create(key, value)`: Adds a new key-value pair.
- `read(key)`: Retrieves the value associated with the key.
- `update(key, value)`: Updates the value for an existing key.
- `delete(key)`: Removes the key-value pair.

### **2. `BatchPersistentKeyValueStore`**
- Extends `KeyValueStore` to add persistence and batch saving.

#### Additional Features:
- **Batch Saving**: Saves the store to disk after a specified number of operations.
- **Auto-Save**: Periodically writes data to disk in the background.
- **Thread Safety**: Ensures consistent state across multiple threads using locks.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/key-value-store.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### **1. Basic Key-Value Store**
```python
store = KeyValueStore()
store.create("name", "Alice")
print(store.read("name"))  # Output: Alice
store.update("name", "Bob")
store.delete("name")
```

### **2. Persistent Store with Batch Saving**
```python
store = BatchPersistentKeyValueStore(batch_size=3, auto_save_interval=10)

store.create("name", "Alice")
store.create("age", 30)
store.create("city", "New York")  # This triggers a save due to batch size.

store.update("name", "Bob")
store.delete("age")  # Changes will be auto-saved after the interval.
```

### **3. Concurrent Updates**
```python
import threading

def update_store():
    store.create("country", "USA")
    store.update("city", "San Francisco")

store = BatchPersistentKeyValueStore(batch_size=5)
threads = [threading.Thread(target=update_store) for _ in range(5)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(store.read("country"))  # Output: USA
print(store.read("city"))     # Output: San Francisco
```

---

## Scalability Techniques

1. **Batch Saving**:
   - Reduces disk I/O overhead by grouping multiple write operations.
   - Ensures durability with periodic auto-saving.

2. **Thread Safety**:
   - Locks prevent race conditions in concurrent environments.

3. **Extensible Storage**:
   - Easily switch from JSON to database backends like SQLite.

---

## Testing

1. Run unit tests:
   ```bash
   python -m unittest discover tests
   ```

2. Test cases include:
   - CRUD functionality.
   - Persistence across restarts.
   - Thread safety with concurrent updates.
   - Scalability with batch saving.

---

## Future Enhancements

1. **Replication**:
   - Add leader-based replication to improve fault tolerance.

2. **Partitioning**:
   - Distribute data across multiple nodes for horizontal scaling.

3. **Advanced Monitoring**:
   - Integrate logging and metrics for better observability.

---

## Conclusion

This project showcases the fundamentals of building scalable, reliable, and maintainable systems. By implementing features like persistence, batching, and thread safety, it aligns with real-world distributed system design principles.

