#from timer import Timer
import time
if __name__=="__main__":
    start = time.perf_counter()
    print(f"timer started at {start}")

    print("Entering in the time loop")
    while True:
        last_run = time.perf_counter()
        elapsed = time.perf_counter() - start
        print(f"Elapsed time : {elapsed}")

        if elapsed >= 10 :
            print("Timer elapsed. Running the block code")
            time.sleep(2)
            start = time.perf_counter()
