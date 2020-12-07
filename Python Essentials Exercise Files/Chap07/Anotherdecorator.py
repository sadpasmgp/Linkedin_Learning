import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2-t1)*1000}ms')
    return wrapper

@elapsed_time
def big_sum():
    print(sum(list(range(100000000))))
    
big_sum()

