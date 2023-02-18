
def chapter_2():
    # # comparing coroutines to normal functions
    # async def coroutine_add_one(number: int) -> int:
    #     return number + 1


    # def add_one(number: int) -> int:
    #     return number + 1


    # function_result = add_one(1)
    # coroutine_result = coroutine_add_one(1)

    # print(f'Function result is {function_result} and the type is {type(function_result)}')
    # print(f'Coroutine result is {coroutine_result} and the type is {type(coroutine_result)}')




    # # running a coroutine
    # import asyncio

    # async def coroutine_add_one(number: int) -> int:
    #     return number + 1


    # def add_one(number: int) -> int:
    #     return number + 1


    # function_result = add_one(1)
    # coroutine_result = asyncio.run(coroutine_add_one(2))

    # print(f'Function result is {function_result} and the type is {type(function_result)}')
    # print(f'Coroutine result is {coroutine_result} and the type is {type(coroutine_result)}')




    # # using await to wait for the result of coroutine
    # import asyncio

    # async def add_one(number: int) -> int:
    #     return number + 1


    # async def main() -> None:
    #     one_plus_one = await add_one(1)
    #     two_plus_one = await add_one(2)
    #     print(one_plus_one)
    #     print(two_plus_one)

    # asyncio.run(main())




    # # a first application with sleep
    # import asyncio

    # async def hello_world_message() -> str:
    #     await asyncio.sleep(1)
    #     return "Hello World!"

    # async def main() -> None:
    #     message = await hello_world_message()
    #     print(message)

    # asyncio.run(main())




    # # runing two coroutines
    # import asyncio
    # from util import delay


    # async def add_one(number: int) -> int:
    #     return number + 1

    # async def hello_world_message() -> str:
    #     await delay(1)
    #     return "Hello World!"

    # async def main() -> None:
    #     message = await hello_world_message()
    #     one_plus_one = await add_one(1)
    #     print(one_plus_one)
    #     print(message)

    # asyncio.run(main())




    # # running code while other operations complete
    # import asyncio
    # from util import delay


    # async def hello_every_second():
    #     for i in range(3):
    #         await asyncio.sleep(1)
    #         print("I'm running other code while I'm waiting!")


    # async def main():
    #     first_delay = asyncio.create_task(delay(4))
    #     second_delay = asyncio.create_task(delay(4))
    #     await hello_every_second()
    #     await first_delay
    #     await second_delay

    # asyncio.run(main())




    # # canceling a task
    # import asyncio
    # from asyncio import CancelledError
    # from util import delay


    # async def main():
    #     long_task = asyncio.create_task(delay(10))

    #     seconds_elapsed = 0

    #     while not long_task.done():
    #         print('Task not finished, checking again in a second.')
    #         await asyncio.sleep(1)
    #         seconds_elapsed = seconds_elapsed + 1
    #         if seconds_elapsed == 5:
    #             long_task.cancel()

    #     try:
    #         await long_task
    #     except CancelledError:
    #         print('Our task was cancelled')

    # asyncio.run(main())




    # # creating a timeout for a task with wait_for
    # import asyncio
    # from util import delay

    # async def main():
    #     delay_task = asyncio.create_task(delay(2))
    #     try:
    #         result = await asyncio.wait_for(delay_task, timeout=1)
    #         print(result)
    #     except asyncio.exceptions.TimeoutError:
    #         print('Got a timeout!')
    #         print(f'Was the task cancelled? {delay_task.cancelled()}')

    # asyncio.run(main())




    # # shielding a task from cancellation
    # import asyncio
    # from util import delay


    # async def main():
    #     task = asyncio.create_task(delay(10))

    #     try:
    #         result = await asyncio.wait_for(asyncio.shield(task), 5)
    #         print(result)
    #     except asyncio.exceptions.TimeoutError:
    #         print("Task took longer than five seconds, it will finish soon!")
    #         result = await task
    #         print(result)

    # asyncio.run(main())




    # # the basics of futures
    # from asyncio import Future

    # my_future = Future()

    # print(f'Is my_future done? {my_future.done()}')

    # my_future.set_result(42)

    # print(f'Is my_future done? {my_future.done()}')
    # print(f'What is the result of my_future? {my_future.result()}')




    # # awaiting a future
    # from asyncio import Future
    # import asyncio

    # def make_request() -> Future:
    #     future = Future()
    #     asyncio.create_task(set_future_value(future))
    #     return future


    # async def set_future_value(future) -> None:
    #     await asyncio.sleep(1)
    #     future.set_result(42)


    # async def main():
    #     future = make_request()
    #     print(f'Is the future done? {future.done()}')
    #     value = await future
    #     print(f'Is the future done? {future.done()}')
    #     print(value)

    # asyncio.run(main())




    # # timing two concurrent tasks with a decorator
    # import asyncio
    # from util import async_timed

    # @async_timed()
    # async def delay(delay_seconds: int) -> int:
    #     await asyncio.sleep(delay_seconds)
    #     return delay_seconds


    # @async_timed()
    # async def main():
    #     task_one = asyncio.create_task(delay(2))
    #     task_two = asyncio.create_task(delay(3))

    #     await task_one
    #     await task_two


    # asyncio.run(main())




    # # attempting to run CPU bound code concurrently
    # import asyncio
    # from util import delay, async_timed


    # @async_timed()
    # async def cpu_bound_work() -> int:
    #     counter = 0
    #     for i in range(100000000):
    #         counter = counter + 1
    #     return counter


    # @async_timed()
    # async def main():
    #     task_one = asyncio.create_task(cpu_bound_work())
    #     task_two = asyncio.create_task(cpu_bound_work())
    #     await task_one
    #     await task_two

    # asyncio.run(main())




    # #  CPU bound code with a task
    # import asyncio
    # from util import async_timed, delay


    # @async_timed()
    # async def cpu_bound_work() -> int:
    #     counter = 0
    #     for i in range(100000000):
    #         counter = counter + 1
    #     return counter


    # @async_timed()
    # async def main():
    #     task_one = asyncio.create_task(cpu_bound_work())
    #     task_two = asyncio.create_task(cpu_bound_work())
    #     delay_task = asyncio.create_task(delay(4))
    #     await task_one
    #     await task_two
    #     await delay_task

    # asyncio.run(main())




    # # Accessing the event loop
    # import asyncio
    # from util import delay

    # def call_later():
    #     print("I'm being called in the future!")

    # async def main():
    #     loop = asyncio.get_event_loop()
    #     loop.call_soon(call_later)
    #     await delay(1)

    # asyncio.run(main())




    # running cpu bound code in debug mode
    import asyncio

    async def cpu_bound_work():
        total = 0
        
        for i in range(1000000):
            total += i
        
        return total

    async def main():
        # changing the slow callback duration
        loop = asyncio.get_event_loop()
        loop.slow_callback_duration = 250

        task_one = asyncio.create_task(cpu_bound_work())
        await task_one
        print(task_one)

    asyncio.run(main(), debug=True)
