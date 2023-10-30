# Uses up loads of CPU power and RAM (Configurable)

import multiprocessing
import os
import time
import threading

def task():
    process_id = os.getpid()
    print(f"Process {process_id} started.")
    
    memory = [bytearray(1024 * 1024 * 1200)]  # Allocate 1200 MB of memory per process
    
    def cpu_task():
        while True:
            pass
    
    num_threads = 4  # Number of CPU-intensive threads
    threads = []
    
    for _ in range(num_threads):
        thread = threading.Thread(target=cpu_task)
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    num_processes = 6  # You can change the number of processes to adjust the CPU and RAM load

    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=task)
        processes.append(process)
        process.start()

    try:
        while True:
            time.sleep(1)

    # Testing
    except KeyboardInterrupt:
        for process in processes:
            process.terminate()
            print(f"Process {process.pid} terminated.")
        print("KeyboardInterrupt: Stopping CPU and RAM hogs.")
