import time

input("Press Enter to start the stopwatch...")

start_time = time.time()

print("Stopwatch started. Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    stop_time = time.time()
    elapsed_time = stop_time - start_time

print(int(elapsed_time), "seconds have passed.")