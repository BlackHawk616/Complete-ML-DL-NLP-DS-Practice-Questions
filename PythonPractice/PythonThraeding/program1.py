# Create a progra, where multiple threads incremnet a shared counter

import threading
import time

# shared counter
counter = 0

# lock for synchronizing access to the counter
counter_lock = threading.Lock()

def increment_counter(thread_id, increments):
    global counter
    for i in range(increments):
        # acquire the lock before modifying the counter
        with counter_lock:
            current_value = counter
            time.sleep(0.01)  # Simulate some work
            counter = current_value + 1
        print(f"Thread {thread_id} incremented counter to {counter}")

number_of_threads = 5
increments_per_thread = 10
threads = []
# Create and start threads
for i in range(number_of_threads):
    thread = threading.Thread(target=increment_counter, args=(i, increments_per_thread))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
print("Final counter value: ", counter) 
