import time
import os

class DataHolder:
    def __init__(self, data):
        self.data = data

cache = {}

def process_data(n):
    for i in range(n):
        data = 'x' * 10_000_000  # simulate large object (~10MB)
        obj = DataHolder(data)
        cache[i] = obj  # Leak: old entries never removed
        time.sleep(0.5)  # simulate processing delay
        print(f"processing: {i}")

if __name__ == '__main__':
    print(f"PID: {os.getpid()}")
    while True:
        process_data(10)
        print("-----------")
