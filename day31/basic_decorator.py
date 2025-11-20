import time
def timer(a):
    def nest():
        start=time.time()
        a()
        end=time.time()
        print(f"Time is in Execution {end-start:.3f}s")
    return nest
@timer
def start():
    print("This is Runned")
    time.sleep(3)
start()
