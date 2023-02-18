# from threading import Lock
# counter_lock = Lock()
# counter: int = 0

from typing import List
from threading import RLock
class IntListThreadsafe():
    lock = RLock()

    def __init__(self, wrapped_list: List[int]):
        self.inner_list = wrapped_list

    def indices_of(self, to_find: int) -> List[int]:
        with self.lock:
            enumerator = enumerate(self.inner_list)
            return [index for index, value in enumerator if value == to_find]

    def find_and_replace(self, to_replace: int, replace_with: int) -> None:
        with self.lock:
            indices = self.indices_of(to_replace)
            for index in indices:
                self.inner_list[index] = replace_with

    def __str__(self):
        return f'{self.inner_list}'


def chapter_7():

    # # a multithreaded echo server
    # from threading import Thread
    # from socket import socket, AF_INET, SOCK_STREAM

    # def echo(client: socket):
    #     while True:
    #         data = client.recv(2048)
    #         print(f'Received {data}, sending!')
    #         client.sendall(data)

    # with socket(AF_INET, SOCK_STREAM) as server:
    #     server.bind(('0.0.0.0', 8000))
    #     server.listen()
    #     while True:
    #         connection, _ = server.accept()
    #         thread = Thread(target=echo, args=(connection,))
    #         thread.start()




    # # Subclassing the thread class for a clean shutdown
    # from threading import Thread
    # from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR

    # class ClientEchoThread(Thread):

    #     def __init__(self, client):
    #         super().__init__()
    #         self.client = client

    #     def run(self):
    #         try:
    #             while True:
    #                 data = self.client.recv(2048)
    #                 if data == bytes(0):
    #                     raise BrokenPipeError('Connection closed!')
    #                 print(f'Received {data}, sending!')
    #                 self.client.sendall(data)
    #         except OSError as e:
    #             print(f'Thread interrupted by {e} exception, shutting down!')

    #     def close(self):
    #         if self.is_alive():
    #             self.client.sendall(bytes('Shutting down!', encoding='utf-8'))
    #             self.client.shutdown(SHUT_RDWR)


    # with socket(AF_INET, SOCK_STREAM) as server:
    #     server.bind(('0.0.0.0', 8000))
    #     server.listen()
    #     connection_threads = []
    #     try:
    #         while True:
    #             connection, addr = server.accept()
    #             thread = ClientEchoThread(connection)
    #             connection_threads.append(thread)
    #             thread.start()
    #     except KeyboardInterrupt:
    #         print('Shutting down!')
    #         [thread.close() for thread in connection_threads]




    # # basic usage of requests
    # import requests
    # from time import time

    # def get_status_code(url: str) -> int:
    #     response = requests.get(url)
    #     return response.status_code


    # url = 'https://www.example.com'
    # start = time()
    # [get_status_code(url) for _ in range(200)]
    # print(f'{time() - start:.4f} seconds')




    # # running requests with a thread pool
    # from time import time
    # import requests
    # from concurrent.futures import ThreadPoolExecutor

    # def get_status_code(url: str) -> int:
    #     response = requests.get(url)
    #     return response.status_code

    # start = time()
    # with ThreadPoolExecutor() as pool:
    #     urls = ['https://www.example.com' for _ in range(1000)]
    #     results = pool.map(get_status_code, urls)
    #     for result in results:
    #         print(result)

    # print(f'finished requests in {time() - start:.4f} second(s)')




    # # using a thread pool executor with asyncio
    # import functools
    # import requests
    # import asyncio
    # from concurrent.futures import ThreadPoolExecutor
    # from util import async_timed


    # def get_status_code(url: str) -> int:
    #     response = requests.get(url)
    #     return response.status_code

    # @async_timed()
    # async def main():
    #     loop = asyncio.get_running_loop()
    #     with ThreadPoolExecutor() as pool:
    #         urls = ['https://www.example.com' for _ in range(100)]
    #         tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
    #         results = await asyncio.gather(*tasks)
    #         print(results)

    # asyncio.run(main())

    # from time import time

    # start = time()
    # results = [get_status_code('https://www.example.com') for _ in range(100)]
    # print(results)
    # print(f'finished in {time() - start} seconds')




    # # using the default executor
    # import functools
    # import requests
    # import asyncio
    # from util import async_timed

    # def get_status_code(url: str) -> int:
    #     response = requests.get(url)
    #     return response.status_code

    # @async_timed()
    # async def main():
    #     loop = asyncio.get_running_loop()
    #     urls = ['https://www.example.com' for _ in range(100)]
    #     tasks = [loop.run_in_executor(None, functools.partial(get_status_code, url)) for url in urls]
    #     results = await asyncio.gather(*tasks)
    #     print(results)

    # asyncio.run(main())




    # # using the to_thread coroutine
    # import requests
    # import asyncio
    # from util import async_timed

    # print(dir(asyncio))

    # def get_status_code(url: str) -> int:
    #     response = requests.get(url)
    #     return response.status_code

    # @async_timed()
    # async def main():
    #     urls = ['https://www.example.com' for _ in range(1000)]
    #     tasks = [asyncio.to_thread(get_status_code, url) for url in urls]
    #     results = await asyncio.gather(*tasks)
    #     print(results)

    # asyncio.run(main())




    # # printing status of requests
    # import functools
    # import requests
    # import asyncio
    # from concurrent.futures import ThreadPoolExecutor
    # from util import async_timed

    # def get_status_code(url: str) -> int:
    #     global counter
    #     response = requests.get(url)
    #     with counter_lock:
    #         counter = counter + 1
    #     return response.status_code

    # async def reporter(request_count: int):
    #     while counter < request_count:
    #         print(f'Finished {counter}/{request_count} requests')
    #         await asyncio.sleep(.5)

    # @async_timed()
    # async def main():
    #     loop = asyncio.get_running_loop()
    #     with ThreadPoolExecutor() as pool:
    #         request_count = 200
    #         urls = ['https://www.example.com' for _ in range(request_count)]
    #         reporter_task = asyncio.create_task(reporter(request_count))
    #         tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
    #         results = await asyncio.gather(*tasks)
    #         await reporter_task
    #         print(results)

    # asyncio.run(main())




    # # recursion with locks
    # from threading import Lock, Thread
    # from typing import List

    # list_lock = Lock()
    # list = [1, 2, 3, 4]

    # def sum_list(int_list: List[int]) -> int:
    #     print('Waiting to acquire lock...')
    #     with list_lock:
    #         print('Acquired lock.')
    #         if len(int_list) == 1:
    #             print('Finished summing.')
    #             return int_list[0]
    #         else:
    #             head, *tail = int_list
    #             print('Summing rest of list.')
    #             return head + sum_list(tail)

    # thread = Thread(target=sum_list, args=(list,))
    # thread.start()
    # thread.join()




    # # a thread safe list class
    # threadsafe_list = IntListThreadsafe([1, 2, 1, 2, 1])
    # print(threadsafe_list)
    # threadsafe_list.find_and_replace(1, 3)
    # print(threadsafe_list)




    # # a deadlock in code
    # from threading import Lock, Thread
    # import time

    # lock_a = Lock()
    # lock_b = Lock()

    # def a():
    #     with lock_a:
    #         print('Acquired lock a from method a!')
    #         time.sleep(1)
    #         with lock_b:
    #             print('Acquired both locks from method a!')

    # def b():
    #     with lock_b:
    #         print('Acquired lock b from method b!')
    #         with lock_a:
    #             print('Acquired both locks from method b!')

    # thread_1 = Thread(target=a)
    # thread_2 = Thread(target=b)
    # thread_1.start()
    # thread_2.start()
    # thread_1.join()
    # thread_2.join()




    # # hello world with tkinter
    # import tkinter
    # from tkinter import ttk
    # from time import sleep

    # window = tkinter.Tk()
    # window.title('Hello world app')
    # window.geometry('200x100')

    # def say_hello():
    #     print('Hello there!')
    #     sleep(5)

    # hello_button = ttk.Button(window, text='Say hello', command=say_hello)
    # hello_button.pack()

    # window.mainloop()




    # # the load tester app
    # from util import LoadTester, ThreadedEventLoop
    # import asyncio

    # loop = asyncio.new_event_loop()

    # asyncio_thread = ThreadedEventLoop(loop)
    # asyncio_thread.start()

    # app = LoadTester(loop)
    # app.mainloop()




    # # hashing passwords with scrypt
    # import hashlib
    # import os
    # from time import time
    # import random


    # def random_password(length: int) -> bytes:
    #     ascii_lowercase = b'abcdefghijklmnopqrstuvwxyz'
    #     return b''.join(bytes(random.choice(ascii_lowercase)) for _ in range(length))

    # passwords = [random_password(10) for _ in range(10000)]

    # def hash(password: bytes) -> str:
    #     salt = os.urandom(16)
    #     return str(hashlib.scrypt(password, salt=salt, n=2, p=24, r=16))

    # start = time()

    # for password in passwords:
    #     hash(password)

    # print(time() - start)




    # # hashing with multithreading and asyncio
    # import asyncio
    # import functools
    # import hashlib
    # import os
    # from concurrent.futures.thread import ThreadPoolExecutor
    # import random
    # from time import time

    # def random_password(length: int) -> bytes:
    #     ascii_lowercase = b'abcdefghijklmnopqrstuvwxyz'
    #     return b''.join(bytes(random.choice(ascii_lowercase)) for _ in range(length))

    # passwords = [random_password(10) for _ in range(10000)]

    # def hash(password: bytes) -> str:
    #     salt = os.urandom(16)
    #     return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))

    # async def main():
    #     loop = asyncio.get_running_loop()
    #     tasks = []

    #     with ThreadPoolExecutor() as pool:
    #         start = time()
    #         for password in passwords:
    #             tasks.append(loop.run_in_executor(pool, functools.partial(hash, password)))

    #         await asyncio.gather(*tasks)
    #         print(time() - start)

    # asyncio.run(main())




    # # means of a large matrix with numpy
    # import numpy as np
    # from time import time

    # data_points = 400000000
    # rows = 50
    # columns = int(data_points / rows)
    # matrix = np.arange(data_points).reshape(rows, columns)
    # s = time()
    # res = np.mean(matrix, axis=1)

    # print(time() - s)




    # threading with numpy
    import functools
    from concurrent.futures.thread import ThreadPoolExecutor
    import numpy as np
    import asyncio
    from time import time

    def mean_for_row(arr, row):
        return np.mean(arr[row])

    data_points = 400000000
    rows = 50
    columns = int(data_points / rows)
    matrix = np.arange(data_points).reshape(rows, columns)

    async def main():
        loop = asyncio.get_running_loop()
        with ThreadPoolExecutor() as pool:
            tasks = []
            s = time()
            for i in range(rows):
                mean = functools.partial(mean_for_row, matrix, i)
                tasks.append(loop.run_in_executor(pool, mean))

            results = asyncio.gather(*tasks)
            print(time() - s)

    asyncio.run(main())
