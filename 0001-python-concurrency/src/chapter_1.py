

def chapter_1():
    # # Processes and threads in a simple Python application
    # import os
    # import threading

    # print(f'Python process running with process id: {os.getpid()}')

    # total_threads = threading.active_count()
    # thread_name = threading.current_thread().getName()

    # print(f'Python is currently running {total_threads} thread(s)')
    # print(f'The current thread is {thread_name}')




    # # creating a multithreaded Python application
    # import threading


    # def hello_from_thread():
    #     thread_name = threading.current_thread()
    #     print(f'Hello from thread {thread_name}!')


    # hello_thread = threading.Thread(target=hello_from_thread)
    # hello_thread.start()

    # total_threads = threading.active_count()
    # thread_name = threading.current_thread().getName()

    # print(f'Python is currently running {total_threads} thread(s)')
    # print(f'The current thread is {thread_name}')

    # hello_thread.join()




    # # Creating multiple processes
    # import multiprocessing
    # import os


    # def hello_from_process():
    #     print(f'Hello from child process {os.getpid()}!')


    # # if __name__ == '__main__':
    # hello_process = multiprocessing.Process(target=hello_from_process)
    # hello_process.start()

    # print(f'Hello from parent process {os.getpid()}')

    # hello_process.join()




    # # Generating and timing the Fibonacci sequence
    # import time

    # def print_fib(number: int) -> None:
    #     def fib(n: int) -> int:
    #         if n == 1:
    #             return 0
    #         elif n == 2:
    #             return 1
    #         else:
    #             return fib(n - 1) + fib(n - 2)

    #     print(f'fib({number}) is {fib(number)}')


    # def fibs_no_threading():
    #     print_fib(40)
    #     print_fib(41)


    # start = time.time()

    # fibs_no_threading()

    # end = time.time()

    # print(f'Completed in {end - start} seconds.')




    # # Multithreading the Fibonacci sequence
    # import threading
    # import time

    # def fibs_with_threads():
    #     fortieth_thread = threading.Thread(target=print_fib, args=(40,))
    #     forty_first_thread = threading.Thread(target=print_fib, args=(41,))

    #     fortieth_thread.start()
    #     forty_first_thread.start()

    #     fortieth_thread.join()
    #     forty_first_thread.join()


    # start_threads = time.time()

    # fibs_with_threads()

    # end_threads = time.time()

    # print(f'Threads took {end_threads - start_threads} seconds.')




    # Synchronously reading status codes
    # import time
    # import requests


    # def read_example() -> None:
    #     response = requests.get('https://www.example.com')
    #     print(response.status_code)


    # sync_start = time.time()

    # read_example()
    # read_example()

    # sync_end = time.time()

    # print(f'Running synchronously took {sync_end - sync_start} seconds.')




    # Multithreaded status code reading
    import time
    import threading
    import requests


    def read_example() -> None:
        response = requests.get('https://www.example.com')
        print(response.status_code)


    thread_1 = threading.Thread(target=read_example)
    thread_2 = threading.Thread(target=read_example)

    thread_start = time.time()

    thread_1.start()
    thread_2.start()

    print('All threads running!')

    thread_1.join()
    thread_2.join()

    thread_end = time.time()

    print(f'Running with threads took {thread_end - thread_start} seconds.')
