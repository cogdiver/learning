

def chapter_3():
    # # Working with blocking sockets
    # import socket

    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # server_address = ('localhost', 8000)
    # server_socket.bind(server_address)
    # server_socket.listen()

    # connection, client_address = server_socket.accept()
    # print(f'I got a connection from {client_address}!')
    # print(connection)




    # # reading data from a socket
    # import socket
 
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # server_address = ('localhost', 8000)
    # server_socket.bind(server_address)
    # server_socket.listen()

    # try:
    #     connection, client_address = server_socket.accept()
    #     print(f'I got a connection from {client_address}!')

    #     buffer = connection.recv(2)
    #     print(f'I got data: {buffer}!')

    #     while buffer[-2:] != b'\r\n':
    #         data = connection.recv(2)
    #         print(f'I got data: {data}!')
    #         buffer = buffer + data

    #     print(f"All the data is: {buffer}")
    #     connection.sendall(buffer)

    # finally:
    #     server_socket.close()




    # # allowing multiple clients to connect
    # import socket

    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # server_address = ('localhost', 8000)
    # server_socket.bind(server_address)
    # server_socket.listen()

    # connections = []

    # try:
    #     while True:
    #         connection, client_address = server_socket.accept()
    #         print(f'I got a connection from {client_address}!')
    #         connections.append(connection)

    #         for connection in connections:
    #             buffer = connection.recv(2)
    #             print(f'I got data: {buffer}!')

    #             while buffer[-2:] != b'\r\n':
    #                 data = connection.recv(2)
    #                 print(f'I got data: {data}!')
    #                 buffer = buffer + data

    #             print(f"All the data is: {buffer}")

    #             connection.send(buffer)
    # finally:
    #     server_socket.close()




    # # a first attempt at a non-blocking server
    # import socket
 
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # server_address = ('localhost', 8000)
    # server_socket.bind(server_address)
    # server_socket.listen()
    # server_socket.setblocking(False)

    # connections = []

    # try:
    #     while True:
    #         connection, client_address = server_socket.accept()
    #         connection.setblocking(False)
    #         print(f'I got a connection from {client_address}!')
    #         connections.append(connection)

    #         for connection in connections:
    #             buffer = connection.recv(2)
    #             print(f'I got data: {buffer}!')

    #             while buffer[-2:] != b'\r\n':
    #                 data = connection.recv(2)
    #                 print(f'I got data: {data}!')
    #                 buffer = buffer + data

    #             print(f"All the data is: {buffer}")

    #             connection.send(buffer)
    # finally:
    #     server_socket.close()




    # # catching and ignoring blocking IO errors
    # import socket
 
    # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # server_address = ('localhost', 8000)
    # server_socket.bind(server_address)
    # server_socket.listen()
    # server_socket.setblocking(False)

    # connections = []

    # try:
    #     while True:
    #         try:
    #             connection, client_address = server_socket.accept()
    #             connection.setblocking(False)
    #             print(f'I got a connection from {client_address}!')
    #             connections.append(connection)
    #         except BlockingIOError:
    #             pass

    #         for connection in connections:
    #             try:
    #                 buffer = connection.recv(2)

    #                 print(f'I got data: {buffer}!')

    #                 while buffer[-2:] != b'\r\n':
    #                     data = connection.recv(2)
    #                     print(f'I got data: {data}!')
    #                     buffer = buffer + data

    #                 print(f"All the data is: {buffer}")
    #                 connection.send(buffer)
    #             except BlockingIOError:
    #                 pass

    # finally:
    #     server_socket.close()




    # # using selectors to build a non-blocking server
    # import selectors
    # import socket
    # from selectors import SelectorKey
    # from typing import List, Tuple

    # selector = selectors.DefaultSelector()

    # server_socket = socket.socket()
    # server_address = ('localhost', 8000)
    # server_socket.setblocking(False)
    # server_socket.bind(server_address)
    # server_socket.listen()

    # selector.register(server_socket, selectors.EVENT_READ)

    # while True:
    #     events: List[Tuple[SelectorKey, int]] = selector.select(timeout=10)

    #     if len(events) == 0:
    #         print('No events, waiting a bit more!')

    #     for event, _ in events:
    #         event_socket = event.fileobj

    #         if event_socket == server_socket:
    #             connection, address = server_socket.accept()
    #             connection.setblocking(False)
    #             print(f"I got a connection from {address}")
    #             selector.register(connection, selectors.EVENT_READ)
    #         else:
    #             data = event_socket.recv(1024)
    #             print(f"I got some data: {data}")
    #             event_socket.send(data)




    # # an asyncio echo server
    # import asyncio
    # import socket
    # from asyncio import AbstractEventLoop


    # async def echo(connection: socket,
    #             loop: AbstractEventLoop) -> None:
    #     while data := await loop.sock_recv(connection, 1024):
    #         await loop.sock_sendall(connection, data)


    # async def listen_for_connection(server_socket: socket,
    #                                 loop: AbstractEventLoop):
    #     while True:
    #         connection, address = await loop.sock_accept(server_socket)
    #         connection.setblocking(False)
    #         print(f"Got a connection from {address}")
    #         asyncio.create_task(echo(connection, loop))


    # async def main():
    #     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     server_address = ('localhost', 8000)
    #     server_socket.setblocking(False)
    #     server_socket.bind(server_address)
    #     server_socket.listen()

    #     await listen_for_connection(server_socket, asyncio.get_event_loop())

    # asyncio.run(main())




    # # Handling errors in tasks
    # import logging
    # import asyncio
    # import socket
    # from asyncio import AbstractEventLoop
 
    # async def echo(connection: socket,
    #             loop: AbstractEventLoop) -> None:
    #     try:
    #         while data := await loop.sock_recv(connection, 1024):
    #             print('got data!')
    #             if data == b'boom\r\n':
    #                 raise Exception("Unexpected network error")
    #             await loop.sock_sendall(connection, data)
    #     except Exception as ex:
    #         logging.exception(ex)
    #     finally:
    #         connection.close()

    # tasks = []
 
    # async def listen_for_connection(server_socket: socket,
    #                                 loop: AbstractEventLoop):
    #     while True:
    #         connection, address = await loop.sock_accept(server_socket)
    #         connection.setblocking(False)
    #         print(f"Got a connection from {address}")
    #         tasks.append(asyncio.create_task(echo(connection, loop)))

    # async def main():
    #     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     server_address = ('localhost', 8000)
    #     server_socket.setblocking(False)
    #     server_socket.bind(server_address)
    #     server_socket.listen()

    #     await listen_for_connection(server_socket, asyncio.get_event_loop())

    # asyncio.run(main())




    # # adding a signal handler to cancel all tasks
    # import asyncio, signal
    # from asyncio import AbstractEventLoop
    # from typing import Set

    # from util.delay_functions import delay


    # def cancel_tasks():
    #     print('Got a SIGINT!')
    #     tasks: Set[asyncio.Task] = asyncio.all_tasks()
    #     print(f'Cancelling {len(tasks)} task(s).')
    #     [task.cancel() for task in tasks]


    # async def main():
    #     loop: AbstractEventLoop = asyncio.get_event_loop()

    #     loop.add_signal_handler(signal.SIGINT, cancel_tasks)

    #     d1 = asyncio.create_task(delay(10))
    #     d2 = asyncio.create_task(delay(10))
    #     d3 = asyncio.create_task(delay(10))

    #     await d1
    #     await d2
    #     await d3

    # asyncio.run(main())




    # Waiting for pending tasks to finish
    # import asyncio, signal
    # from util.delay_functions import delay

    # async def await_all_tasks():
    #     tasks = asyncio.all_tasks()
    #     [await task for task in tasks]


    # async def main():
    #     loop = asyncio.get_event_loop()
    #     loop.add_signal_handler(signal.SIGINT,
    #                             lambda: asyncio.create_task(await_all_tasks()))

    #     d1 = asyncio.create_task(delay(10))
    #     d2 = asyncio.create_task(delay(10))
    #     d3 = asyncio.create_task(delay(10))

    #     await d1
    #     await d2
    #     await d3

    # asyncio.run(main())




    # Graceful Exit
    import asyncio
    from asyncio import AbstractEventLoop, Task
    import socket
    import logging
    import signal
    from typing import List


    async def echo(connection: socket,
                loop: AbstractEventLoop) -> None:
        try:
            while data := await loop.sock_recv(connection, 1024):
                print('got data!')
                if data == b'boom\r\n':
                    raise Exception("Unexpected network error")
                await loop.sock_sendall(connection, data)
        except Exception as ex:
            logging.exception(ex)
        finally:
            connection.close()

    async def connection_listener(server_socket, loop):
        while True:
            connection, address = await loop.sock_accept(server_socket)
            connection.setblocking(False)
            print(f"Got a connection from {address}")
            yield asyncio.create_task(echo(connection, loop))


    class GracefulExit(SystemExit):
        pass


    def shutown():
        raise GracefulExit()


    async def close_echo_tasks(echo_tasks: List[asyncio.Task]):
        waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
        for task in waiters:
            try:
                await task
            except asyncio.exceptions.TimeoutError:
                # We expect a timeout error here
                pass


    echo_tasks = []


    async def listen_for_connections(server_socket, loop):
        async for echo_task in connection_listener(server_socket, loop):
            echo_tasks.append(echo_task)


    async def main():
        server_socket = socket.socket()
        server_address = ('localhost', 8000)
        server_socket.setblocking(False)
        server_socket.bind(server_address)
        server_socket.listen()

        for signame in {'SIGINT', 'SIGTERM'}:
            loop.add_signal_handler(getattr(signal, signame), shutown)
        await listen_for_connections(server_socket, loop)


    loop = asyncio.new_event_loop()

    try:
        loop.run_until_complete(main())
    except GracefulExit:
        loop.run_until_complete(close_echo_tasks(echo_tasks))
    finally:
        loop.close()
