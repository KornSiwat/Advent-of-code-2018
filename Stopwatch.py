import time

status = False
start_time = 0

def start():
    global start_time,status
    start_time = time.time()
    status = True

def stop():
    global status
    if status == False:
        print('Stopwatch is not running')
        return None
    print(f'Runtime: {time.time()-start_time}')
    status = True       