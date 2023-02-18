def chapter_4():
    # # an asynchronous context manager to wait for a client connection
    # import asyncio
    # import socket
    # from types import TracebackType
    # from typing import Optional, Type


    # class ConnectedSocket:
    #     _connection = None

    #     def __init__(self, server_socket):
    #         self.server_socket = server_socket

    #     async def __aenter__(self):
    #         print('Entering context manager, waiting for connection')
    #         loop = asyncio.get_event_loop()
    #         connection, address = await loop.sock_accept(self.server_socket)
    #         self._connection = connection
    #         print('Accepted a connection')
    #         return self._connection

    #     async def __aexit__(self,
    #                         exc_type: Optional[Type[BaseException]],
    #                         exc_val: Optional[BaseException],
    #                         exc_tb: Optional[TracebackType]):
    #         print('Exiting context manager')
    #         self._connection.close()
    #         print('Closed connection')

    # async def main():
    #     loop = asyncio.get_event_loop()

    #     server_socket = socket.socket()
    #     server_address = ('localhost', 8000)
    #     server_socket.setblocking(False)
    #     server_socket.bind(server_address)
    #     server_socket.listen()

    #     async with ConnectedSocket(server_socket) as connection:
    #         data = await loop.sock_recv(connection, 1024)
    #         print(data)

    # asyncio.run(main())




    # # making a single aiohttp web request
    # import asyncio
    # import aiohttp
    # from aiohttp import ClientSession
    # from util import async_timed


    # @async_timed()
    # async def fetch_status(session: ClientSession, url: str) -> int:
    #     async with session.get(url) as result:
    #         return result.status


    # @async_timed()
    # async def main():
    #     async with aiohttp.ClientSession() as session:
    #         url = 'http://www.example.com'
    #         status = await fetch_status(session, url)
    #         print(f'Status for {url} was {status}')

    # asyncio.run(main())




    # # setting timeouts with aiohttp
    # import asyncio
    # import aiohttp
    # from aiohttp import ClientSession

    # async def fetch_status(session: ClientSession, url: str) -> int:
    #     ten_millis = aiohttp.ClientTimeout(total=.01)

    #     async with session.get(url, timeout=ten_millis) as result:
    #             return result.status


    # async def main():
    #     session_timeout = aiohttp.ClientTimeout(total=1, connect=1)
    #     async with aiohttp.ClientSession(timeout=session_timeout) as session:
    #         url = 'http://www.example.com'
    #         status = await fetch_status(session, url)
    #         print(f'Status for {url} was {status}')

    # asyncio.run(main())




    # # using tasks with a list comprehension
    # import asyncio
    # from util import async_timed, delay


    # @async_timed()
    # async def main() -> None:
    #     delay_times = [1,2,3,4,5]
    #     tasks = [asyncio.create_task(delay(seconds)) for seconds in delay_times]
    #     [await task for task in tasks]

    # asyncio.run(main())




    # multiple requests concurrently with gather
    import asyncio
    import aiohttp
    from util import async_timed, fetch_status


    @async_timed()
    async def main():
        async with aiohttp.ClientSession() as session:
            urls = ['https://example.com' for _ in range(1000)]
            requests = [fetch_status(session, url) for url in urls]
            status_codes = await asyncio.gather(*requests)
            print(status_codes)

    asyncio.run(main())




    # # awaitables finishing out of order
    # import asyncio
    # from util import delay


    # async def main():
    #     results = await asyncio.gather(delay(3), delay(1))
    #     print(results)

    # asyncio.run(main())




    # # Handling exceptions with gather
    # import asyncio
    # import aiohttp
    # from util import async_timed, fetch_status

    # # # Throw a exception
    # # @async_timed()
    # # async def main():
    # #     async with aiohttp.ClientSession() as session:
    # #         urls = ['https://example.com', 'python://example.com']
    # #         tasks = [fetch_status(session, url) for url in urls]
    # #         status_codes = await asyncio.gather(*tasks)
    # #         print(status_codes)

    # @async_timed()
    # async def main():
    #     async with aiohttp.ClientSession() as session:
    #         urls = ['https://example.com', 'python://example.com']
    #         tasks = [fetch_status(session, url) for url in urls]
    #         results = await asyncio.gather(*tasks, return_exceptions=True)

    #         exceptions = [res for res in results if isinstance(res, Exception)]
    #         successful_results = [res for res in results if not isinstance(res, Exception)]

    #         print(f'All results: {results}')
    #         print(f'Finished successfully: {successful_results}')
    #         print(f'Threw exceptions: {exceptions}')

    # asyncio.run(main())




    # # using as_completed
    # import asyncio
    # import aiohttp
    # from util import async_timed, fetch_status


    # @async_timed()
    # async def main():
    #     async with aiohttp.ClientSession() as session:
    #         fetchers = [fetch_status(session, 'https://www.example.com', 2),
    #                     fetch_status(session, 'https://www.example.com', 1),
    #                     fetch_status(session, 'https://www.example.com', 10)]

    #         for finished_task in asyncio.as_completed(fetchers):
    #             print(await finished_task)

    # asyncio.run(main())




    # # setting a timeout on as_completed
    # import asyncio
    # import aiohttp
    # from util import async_timed, fetch_status


    # @async_timed()
    # async def main():
    #     async with aiohttp.ClientSession() as session:
    #         fetchers = [fetch_status(session, 'https://example.com', 1),
    #                     fetch_status(session, 'https://example.com', 10),
    #                     fetch_status(session, 'https://example.com', 10)]

    #         for done_task in asyncio.as_completed(fetchers, timeout=2):
    #             try:
    #                 result = await done_task
    #                 print(result)
    #             except asyncio.TimeoutError:
    #                 print('We got a timeout error!')

    #         for task in asyncio.tasks.all_tasks():
    #             print(task)

    # asyncio.run(main())




    # # examining the default behavior of wait
    # import asyncio
    # from aiohttp import ClientSession
    # from util import async_timed, fetch_status


    # @async_timed()
    # async def main():
    #     async with ClientSession() as session:
    #         fetchers = [fetch_status(session, 'https://example.com'),
    #                     fetch_status(session, 'https://example.com')]
    #         done, pending = await asyncio.wait(fetchers)

    #         print(f'Done task count: {len(done)}')
    #         print(f'Pending task count: {len(pending)}')

    #         for done_task in done:
    #             result = await done_task
    #             print(result)

    # asyncio.run(main())




    # # exceptions with wait
    # import asyncio
    # import logging
    # from aiohttp import ClientSession
    # from util import async_timed, fetch_status

    # @async_timed()
    # async def main():
    #     async with ClientSession() as session:
    #         good_request = fetch_status(session, 'https://www.example.com')
    #         bad_request = fetch_status(session, 'python://bad')

    #         fetchers = [asyncio.create_task(good_request),
    #                     asyncio.create_task(bad_request)]

    #         done, pending = await asyncio.wait(fetchers)

    #         print(f'Done task count: {len(done)}')
    #         print(f'Pending task count: {len(pending)}')

    #         for done_task in done:
    #             # result = await done_task will throw an exception
    #             if not done_task.exception():
    #                 print(done_task.result())
    #             else:
    #                 logging.error("Request got an exception",
    #                             exc_info=done_task.exception())

    # asyncio.run(main())




    # # canceling running requests on an exception
    # import aiohttp
    # import asyncio
    # import logging
    # from util import async_timed, fetch_status


    # @async_timed()
    # async def main():
    #     async with aiohttp.ClientSession() as session:
    #         fetchers = [asyncio.create_task(fetch_status(session, 'python://bad.com')),
    #                     asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3)),
    #                     asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3))]

    #         done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

    #         print(f'Done task count: {len(done)}')
    #         print(f'Pending task count: {len(pending)}')

    #         for done_task in done:
    #             if done_task.exception() is None:
    #                 print(done_task.result())
    #             else:
    #                 logging.error("Request got an exception",
    #                             exc_info=done_task.exception())

    #         for pending_task in pending:
    #             pending_task.cancel()

    # asyncio.run(main())




    # # processing as they complete
    # import asyncio
    # import aiohttp
    # from util import async_timed, fetch_status


    # @async_timed()
    # async def main():
    #     async with aiohttp.ClientSession() as session:
    #         url = 'https://www.example.com'
    #         fetchers = [asyncio.create_task(fetch_status(session, url)),
    #                     asyncio.create_task(fetch_status(session, url)),
    #                     asyncio.create_task(fetch_status(session, url))]

    #         done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

    #         print(f'Done task count: {len(done)}')
    #         print(f'Pending task count: {len(pending)}')

    #         for done_task in done:
    #             print('Hecho: ', await done_task)

    # asyncio.run(main())




    # # Processing all results as they come in
    # import asyncio
    # import aiohttp
    # from util import async_timed, fetch_status

    # @async_timed()
    # async def main():
    #     async with aiohttp.ClientSession() as session:
    #         url = 'https://www.example.com'
    #         pending = [asyncio.create_task(fetch_status(session, url)),
    #                 asyncio.create_task(fetch_status(session, url)),
    #                 asyncio.create_task(fetch_status(session, url))]

    #         while pending:
    #             done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

    #             print(f'Done task count: {len(done)}')
    #             print(f'Pending task count: {len(pending)}')

    #             for done_task in done:
    #                 print(await done_task)

    # asyncio.run(main())




    # # using timeouts with wait
    # import asyncio
    # import aiohttp
    # from util import async_timed, fetch_status

    # @async_timed()
    # async def main():
    #     async with aiohttp.ClientSession() as session:
    #         example_url = 'https://example.com'
    #         fetchers = [fetch_status(session, example_url),
    #                     fetch_status(session, example_url),
    #                     fetch_status(session, example_url, delay=3)]

    #         done, pending = await asyncio.wait(fetchers, timeout=1)

    #         print(f'Done task count: {len(done)}')
    #         print(f'Pending task count: {len(pending)}')

    #         for done_task in done:
    #             result = await done_task
    #             print(result)

    # asyncio.run(main())




    # cancelling a slow request
    import asyncio
    import aiohttp
    from util import fetch_status


    async def main():
        async with aiohttp.ClientSession() as session:
            api_a = fetch_status(session, 'https://www.example.com')
            api_b = asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=2))

            done, pending = await asyncio.wait([api_a, api_b], timeout=1)

            for task in pending:
                if task is api_b:
                    print('API B too slow, cancelling')
                    task.cancel()

    asyncio.run(main())
