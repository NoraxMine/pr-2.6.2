import multiprocessing
import time
import math

def calculate_chunk(data_chunk):
    return sum(x**2 for x in data_chunk)

def split_data(data, num_parts):
    n = len(data)
    chunk_size = math.ceil(n / num_parts)
    return [data[i*chunk_size : min((i+1)*chunk_size, n)] #разбиение данных
            for i in range(num_parts)] #i*chunk_size – начало диапазона (сдвигает индекс на i).
                                       #min((i+1)*chunk_size, n) – конец диапазона, но не больше n.
                                       #for i in range(num_parts) – итерация num_parts раз.

if __name__ == "__main__": 
    data = list(range(100_000_000)) 
    # Синхронное вычисление
    start = time.time()
    result = calculate_chunk(data)
    sync_time = time.time() - start
    print(f"Синхронное вычисление: {sync_time:.2f} сек")

    # Многопроцессорное вычисление
    num_processes = 20
    start = time.time()
    # Надежное разделение данных
    chunks = split_data(data, num_processes)
    
    with multiprocessing.Pool(processes=num_processes) as pool: #оздает пул (группу) процессов, которые могут работать одновременно.
        results = pool.map(calculate_chunk, chunks) #разделяет работу между процессами
        result_parallel = sum(results)
    
    mp_time = time.time() - start
    print(f"Многопроцессорное вычисление: {mp_time:.2f} сек")
    print(f"Результаты совпадают: {result == result_parallel}")