import multiprocessing
import time

data = list(range(0, 100_000_000))
def quad(data): # Принимаеи список
    return sum(n**2 for n in data)

def split_list(alist, wanted_parts=2):
    length = len(alist)
    return [alist[i*(length // wanted_parts): (i+1)*(length//wanted_parts)]
            for i in range(wanted_parts)]

def simple(process_num = 1):
    # Последовательное выполнение
    start = time.time()
    result = (quad(data))
    delta =time.time()-start
    print("Время",delta)
    return delta

def parallel(process_num = 1):
    # Параллельое выполнение
    start = time.time()
    splitted_list = split_list(data, process_num)
    with multiprocessing.Pool(processes=process_num) as pool:
        results = sum(pool.map(quad, splitted_list))
        delta =time.time()-start
    print("Время",delta)
    return delta

def optimizer1():
    best_time = 5
    times = []
    for proc in range (1,15):
        current_time = simple(process_num = 1)
        if current_time < best_time:
            best_time = current_time
            optimal_procs = proc
            times.append(current_time)
    print(f"djdjdjj {optimal_procs} frfhiouw {best_time}")

def optimizer2():
    best_time = 5
    times = []
    for proc in range (1,15):
        current_time = parallel(process_num = 1)
        if current_time < best_time:
            best_time = current_time
            optimal_procs = proc
            times.append(current_time)
    print(f"djdjdjj {optimal_procs} frfhiouw {best_time}")

if __name__ == "__main__":
    optimizer1()
    optimizer2()