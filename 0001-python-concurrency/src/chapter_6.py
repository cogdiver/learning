from util import async_timed
from time import time
from multiprocessing import Value
from typing import Dict, List
import asyncpg
import asyncio

shared_counter: Value
map_progress: Value
password = 'mysecretpassword'

def say_hello(name: str) -> str:
    return f"Hi there, {name}"

def count(count_to: int) -> int:
    start = time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time()
    print(f'Finished counting to {count_to} in {end - start}')
    return counter

def increment():
    with shared_counter.get_lock():
        shared_counter.value += 1

def map_frequencies(chunk: List[str]) -> Dict[str, int]:
        counter = {}
        for line in chunk:
            word, _, _, count = line.split('\t')
            if counter.get(word):
                counter[word] = counter[word] + int(count)
            else:
                counter[word] = int(count)

        with map_progress.get_lock():
            map_progress.value += 1

        return counter

async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow("SELECT * FROM product;")

@async_timed()
async def query_products_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)

def run_in_new_loop(num_queries: int) -> List[Dict]:
    async def run_queries():
        async with asyncpg.create_pool(host='127.0.0.1',
                                    port=5432,
                                    user='postgres',
                                    password=password,
                                    database='products',
                                    min_size=6,
                                    max_size=6) as pool:
            return await query_products_concurrently(pool, num_queries)

    results = [dict(result) for result in asyncio.run(run_queries())]
    return results

def chapter_6():
    # # two parallel processes with multiprocessing
    # from time import time
    # from multiprocessing import Process


    # def count(count_to: int) -> int:
    #     start = time()
    #     counter = 0
    #     while counter < count_to:
    #         counter = counter + 1
    #     end = time()
    #     print(f'Finished counting to {count_to} in {end-start}')
    #     return counter

    # # if __name__ == "__main__":
    # # This is a quirk of the multiprocessing library and if you
    # # don’t add this you may see an error that “An attempt has been
    # # made to start a new process before the current process has
    # # finished its bootstrapping phase.”. The reason this happens
    # # is to prevent others who may import your code from accidentally
    # # launching multiple processes.
    # start_time = time()

    # from_two_hundred_million = Process(target=count, args=(200000000,))
    # from_one_hundred_million = Process(target=count, args=(100000000,))

    # from_two_hundred_million.start()
    # from_one_hundred_million.start()

    # from_two_hundred_million.join()
    # from_one_hundred_million.join()

    # end_time = time()
    # print(f'Completed in {end_time-start_time}')




    # # creating a process pool
    # from multiprocessing import Pool
    # from time import time

    # t0 = time()
    # with Pool() as process_pool:
    #     hi_jeff = process_pool.apply(say_hello, args=('Jeff',))
    #     hi_john = process_pool.apply(say_hello, args=('John',))
    #     print(hi_jeff)
    #     print(hi_john)
    #     print(f'{time() - t0:.4f}')




    # # using async results with process pools
    # from multiprocessing import Pool

    # t0 = time()
    # with Pool() as process_pool:
    #     hi_jeff = process_pool.apply_async(say_hello, args=('Jeff',))
    #     hi_john = process_pool.apply_async(say_hello, args=('John',))
    #     print(hi_jeff.get())
    #     print(hi_john.get())
    #     print(f'{time() - t0:.4f}')




    # # process pool executors
    # from concurrent.futures import ProcessPoolExecutor

    # with ProcessPoolExecutor() as process_pool:
    #     numbers = [1, 3, 5, 22, 100000000]
    #     for result in process_pool.map(count, numbers):
    #         print(result)




    # #  process pool executors with asyncio
    # import asyncio
    # from asyncio.events import AbstractEventLoop
    # from concurrent.futures import ProcessPoolExecutor
    # from functools import partial
    # from typing import List

    # async def main():
    #     with ProcessPoolExecutor() as process_pool:
    #         loop: AbstractEventLoop = asyncio.get_event_loop()
    #         nums = [1, 3, 5, 22, 100000000]
    #         calls: List[partial[int]] = [partial(count, num) for num in nums]
    #         call_coros = []

    #         for call in calls:
    #             call_coros.append(loop.run_in_executor(process_pool, call))

    #         results = await asyncio.gather(*call_coros)

    #         for result in results:
    #             print(result)

    # asyncio.run(main())




    # # single-threaded map reduce
    # import functools
    # from typing import Dict

    # def map_frequency(text: str) -> Dict[str, int]:
    #     words = text.split(' ')
    #     frequencies = {}
    #     for word in words:
    #         if word in frequencies:
    #             frequencies[word] = frequencies[word] + 1
    #         else:
    #             frequencies[word] = 1
    #     return frequencies


    # def merge_dictionaries(first: Dict[str, int],
    #                     second: Dict[str, int]) -> Dict[str, int]:
    #     merged = first
    #     for key in second:
    #         if key in merged:
    #             merged[key] = merged[key] + second[key]
    #         else:
    #             merged[key] = second[key]
    #     return merged

    # lines = ["I know what I know",
    #         "I know that I know",
    #         "I don't know much",
    #         "They don't know much"]

    # mapped_results = [map_frequency(line) for line in lines]

    # for result in mapped_results:
    #     print(result)

    # print('Final Resul:')
    # print(functools.reduce(merge_dictionaries, mapped_results))




    # # counting frequencies of words that start with ‘a’
    # from time import time

    # freqs = {}

    # with open('data/googlebooks-eng-all-1gram-20120701-a') as f:
    #     lines = f.readlines()

    #     start = time()

    #     for line in lines:
    #         data = line.split('\t')
    #         word = data[0]
    #         count = int(data[2])
    #         if word in freqs:
    #             freqs[word] = freqs[word] + count
    #         else:
    #             freqs[word] = count

    #     print(f'{time() - start:.4f} segundos')




    # # parallel map reduce with process pools
    # import asyncio
    # from concurrent.futures import ProcessPoolExecutor
    # import functools
    # from time import time
    # from typing import Dict, List

    # def partition(data: List, chunk_size: int) -> List:
    #     for i in range(0, len(data), chunk_size):
    #         yield data[i:i + chunk_size]

    # def merge_dictionaries(first: Dict[str, int],
    #                     second: Dict[str, int]) -> Dict[str, int]:
    #     merged = first
    #     for key in second:
    #         if key in merged:
    #             merged[key] = merged[key] + second[key]
    #         else:
    #             merged[key] = second[key]
    #     return merged

    # async def main(partition_size: int):
    #     with open('data/googlebooks-eng-all-1gram-20120701-a') as f:
    #         contents = f.readlines()

    #         loop = asyncio.get_event_loop()
    #         tasks = []
    #         start = time()
    #         with ProcessPoolExecutor() as pool:
    #             for chunk in partition(contents, partition_size):
    #                 tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

    #             intermediate_results = await asyncio.gather(*tasks)
    #             final_result = functools.reduce(merge_dictionaries, intermediate_results)
    #             end = time()

    #             print(f"Aardvark has appeared {final_result['Aardvark']} times.")

    #             print(f'Map reduce took: {(end - start):.4f} seconds')

    # asyncio.run(main(partition_size=60000))




    # # parallelizing the reduce operation
    # import asyncio
    # from concurrent.futures import ProcessPoolExecutor
    # import functools
    # from time import time
    # from typing import Dict, List

    # def partition(data: List, chunk_size: int) -> List:
    #     for i in range(0, len(data), chunk_size):
    #         yield data[i:i + chunk_size]


    # async def reduce(loop, pool, counters, chunk_size) -> Dict[str, int]:
    #     chunks: List[List[Dict]] = list(partition(counters, chunk_size))
    #     reducers = []
    #     while len(chunks[0]) > 1:
    #         for chunk in chunks:
    #             reducer = functools.partial(functools.reduce, merge_dictionaries, chunk)
    #             reducers.append(loop.run_in_executor(pool, reducer))
    #         reducer_chunks = await asyncio.gather(*reducers)
    #         chunks = list(partition(reducer_chunks, chunk_size))
    #         reducers.clear()
    #     return chunks[0][0]

    # async def main(partition_size: int):
    #     with open('data/googlebooks-eng-all-1gram-20120701-a') as f:
    #         contents = f.readlines()
    #         loop = asyncio.get_event_loop()
    #         tasks = []
    #         with ProcessPoolExecutor() as pool:
    #             start = time()

    #             for chunk in partition(contents, partition_size):
    #                 tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

    #             intermediate_results = await asyncio.gather(*tasks)
    #             final_result = await reduce(loop, pool, intermediate_results, 500)

    #             print(f"Aardvark has appeared {final_result['Aardvark']} times.")
    #             print(f'Map reduce took: {(time() - start):.4f} seconds')

    # asyncio.run(main(partition_size=60000))




    # # shared values and arrays
    # from multiprocessing import Process, Value, Array

    # def increment_value(shared_int: Value):
    #     shared_int.value = shared_int.value + 1

    # def increment_array(shared_array: Array):
    #     for index, integer in enumerate(shared_array):
    #         shared_array[index] = integer + 1


    # integer = Value('i', 0)
    # integer_array = Array('i', [0, 0])

    # procs = [Process(target=increment_value, args=(integer,)),
    #          Process(target=increment_value, args=(integer,)),
    #          Process(target=increment_array, args=(integer_array,)),
    #          Process(target=increment_array, args=(integer_array,))]

    # [p.start() for p in procs]
    # [p.join() for p in procs]

    # print(integer.value)
    # print(integer_array[:])




    # # incrementing a shared counter in parallel
    # from multiprocessing import Process, Value

    # def increment_value(shared_int: Value):
    #     shared_int.value = shared_int.value + 1

    # for _ in range(100):
    #     integer = Value('i', 0)
    #     procs = [Process(target=increment_value, args=(integer,)),
    #              Process(target=increment_value, args=(integer,))]

    #     [p.start() for p in procs]
    #     [p.join() for p in procs]
    #     print(integer.value)
    #     assert(integer.value == 2)




    # # acquiring and releasing a lock
    # from multiprocessing import Process, Value

    # def increment_value(shared_int: Value):
    #     # with shared_int.get_lock():
    #     shared_int.get_lock().acquire()
    #     shared_int.value = shared_int.value + 1
    #     shared_int.get_lock().release()


    # for _ in range(100):
    #     integer = Value('i', 0)
    #     procs = [Process(target=increment_value, args=(integer,)),
    #             Process(target=increment_value, args=(integer,))]

    #     [p.start() for p in procs]
    #     [p.join() for p in procs]
    #     print(integer.value)
    #     assert (integer.value == 2)




    # # initializing a process pool
    # from concurrent.futures import ProcessPoolExecutor
    # import asyncio
    # from multiprocessing import Value

    # def init(counter: Value):
    #     global shared_counter
    #     shared_counter = counter

    # async def main():
    #     counter = Value('d', 0)
    #     with ProcessPoolExecutor(initializer=init, initargs=(counter,)) as pool:
    #         await asyncio.get_event_loop().run_in_executor(pool, increment)
    #         print(counter.value)

    # asyncio.run(main())




    # # keeping track of map operation progress
    # from concurrent.futures import ProcessPoolExecutor
    # import functools
    # import asyncio
    # from multiprocessing import Value
    # from typing import List, Dict
    # from time import time
    # from util import partition, merge_dictionaries

    # def init(progress: Value):
    #     global map_progress
    #     map_progress = progress

    # async def progress_reporter(total_partitions: int):
    #     while map_progress.value < total_partitions:
    #         print(f'Finished {map_progress.value}/{total_partitions} map operations')
    #         await asyncio.sleep(1)

    # async def main(partiton_size: int):
    #     global map_progress

    #     with open('data/googlebooks-eng-all-1gram-20120701-a') as f:
    #         contents = f.readlines()
    #         loop = asyncio.get_event_loop()
    #         tasks = []
    #         map_progress = Value('i', 0)

    #         start = time()
    #         with ProcessPoolExecutor(initializer=init, initargs=(map_progress,)) as pool:
    #             total_partitions = len(contents) // partiton_size
    #             reporter = asyncio.create_task(progress_reporter(total_partitions))

    #             for chunk in partition(contents, partiton_size):
    #                 tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))

    #             counters = await asyncio.gather(*tasks)
    #             await reporter
    #             final_result = functools.reduce(merge_dictionaries, counters)

    #             print(f"Aardvark has appeared {final_result['Aardvark']} times.")
    #             print(f'Map reduce took: {(time() - start):.4f} seconds')

    # asyncio.run(main(partiton_size=60000))




    # one event loop per process
    import asyncio
    from util import async_timed
    from typing import List, Dict
    from concurrent.futures.process import ProcessPoolExecutor
    import functools

    @async_timed()
    async def main():
        loop = asyncio.get_running_loop()
        pool = ProcessPoolExecutor()
        tasks = []
        for _ in range(5):
            tasks.append(loop.run_in_executor(pool, functools.partial(run_in_new_loop, 5)))
        all_results: List[List[Dict]] = await asyncio.gather(*tasks)
        total_queries = sum([len(result) for result in all_results])
        print(f'Retrieved {total_queries} products the product database.')

    asyncio.run(main())
