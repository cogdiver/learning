def chapter_11():
    # # attempting to create a race condition
    # import asyncio
 
    # counter: int = 0
    
    # async def increment():
    #     global counter
    #     await asyncio.sleep(0.01)
    #     counter = counter + 1
    
    # async def main():
    #     global counter
    #     for _ in range(1000):
    #         tasks = [asyncio.create_task(increment()) for _ in range(100)]
    #         await asyncio.gather(*tasks)
    #         print(f'Counter is {counter}')
    #         assert counter == 100
    #         counter = 0
    
    # asyncio.run(main())




    # #  a single-threaded race condition
    # import asyncio
    
    # counter: int = 0

    # async def increment():
    #     global counter
    #     temp_counter = counter
    #     temp_counter = temp_counter + 1
    #     await asyncio.sleep(0.01)
    #     counter = temp_counter
    
    # async def main():
    #     global counter
    #     for _ in range(1000):
    #         tasks = [asyncio.create_task(increment()) for _ in range(100)]
    #         await asyncio.gather(*tasks)
    #         print(f'Counter is {counter}')
    #         assert counter == 100
    #         counter = 0
    
    # asyncio.run(main())




    # # using an asyncio lock
    # import asyncio
    # from asyncio import Lock
    # from util import delay
    
    # async def a(lock: Lock):
    #     print('Coroutine a waiting to acquire the lock')
    #     async with lock:
    #         print('Coroutine a is in the critical section')
    #         await delay(2)
    #     print('Coroutine a released the lock')
    
    # async def b(lock: Lock):
    #     print('Coroutine b waiting to acquire the lock')
    #     async with lock:
    #         print('Coroutine b is in the critical section')
    #         await delay(2)
    #     print('Coroutine b released the lock')
    
    # async def main():
    #     lock = Lock()
    #     await asyncio.gather(a(lock), b(lock))
    
    # asyncio.run(main())




    # # using semaphores
    # import asyncio
    # from asyncio import Semaphore
    
    # async def operation(semaphore: Semaphore):
    #     print('Waiting to acquire semaphore...')
    #     async with semaphore:
    #         print('Semaphore acquired!')
    #         await asyncio.sleep(2)
    #     print('Semaphore released!')
    
    # async def main():
    #     semaphore = Semaphore(2)
    #     await asyncio.gather(*[operation(semaphore) for _ in range(4)])
    
    # asyncio.run(main())





    # # releasing more than we acquire
    # import asyncio
    # from asyncio import Semaphore
    
    # async def acquire(semaphore: Semaphore):
    #     print('Waiting to acquire')
    #     async with semaphore:
    #         print('Acquired')
    #         await asyncio.sleep(5)
    #     print('Releasing')
    
    # async def release(semaphore: Semaphore):
    #     print('Releasing as a one off!')
    #     semaphore.release()
    #     print('Released as a one off!')
    
    # async def main():
    #     semaphore = Semaphore(2)
    
    #     print("Acquiring twice, releasing three times...")
    #     await asyncio.gather(acquire(semaphore), acquire(semaphore), release(semaphore))
    
    #     print("Acquiring three times...")
    #     await asyncio.gather(acquire(semaphore), acquire(semaphore), acquire(semaphore))
    
    # asyncio.run(main())




    # # bounded semaphores
    # import asyncio
    # from asyncio import BoundedSemaphore
    
    # async def main():
    #     semaphore = BoundedSemaphore(1)
    
    #     await semaphore.acquire()
    #     semaphore.release()
    #     semaphore.release()
    
    # asyncio.run(main())




    # # event basics
    # import asyncio
    # import functools
    # from asyncio import Event
    
    # def trigger_event(event: Event):
    #     event.set()
    
    # async def do_work_on_event(event: Event):
    #     print('Waiting for event...')
    #     await event.wait()
    #     print('Performing work!')
    #     await asyncio.sleep(1)
    #     print('Finished work!')
    #     event.clear()
    
    # async def main():
    #     event = asyncio.Event()
    #     asyncio.get_running_loop().call_later(5.0, functools.partial(trigger_event, event))
    #     await asyncio.gather(do_work_on_event(event), do_work_on_event(event))
    
    # asyncio.run(main())




    # condition basics
    import asyncio
    from asyncio import Condition
    
    async def do_work(condition: Condition):
        while True:
            print('Waiting for condition lock...')
            async with condition:
                print('Acquired lock, releasing and waiting for condition...')
                await condition.wait()
                print('Condition event fired, re-acquiring lock and doing work...')
                await asyncio.sleep(1)
            print('Work finished, lock released.')
    
    async def fire_event(condition: Condition):
        while True:
            await asyncio.sleep(5)
            print('About to notify, acquiring condition lock...')
            async with condition:
                print('Lock acquired, notifying all workers.')
                condition.notify_all()
            print('Notification finished, releasing lock.')
    
    async def main():
        condition = Condition()
    
        asyncio.create_task(fire_event(condition))
        await asyncio.gather(do_work(condition), do_work(condition))
    
    asyncio.run(main())




    pass