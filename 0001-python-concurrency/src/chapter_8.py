def chapter_8():
    # # using the protocol
    # import asyncio
    # from asyncio import AbstractEventLoop
    # from util import HTTPGetClientProtocol
    
    # async def make_request(host: str, port: int, loop: AbstractEventLoop) -> str:
    #     def protocol_factory():
    #         return HTTPGetClientProtocol(host, loop)
    
    #     _, protocol = await loop.create_connection(protocol_factory, host=host, port=port)
    
    #     return await protocol.get_response()
    
    # async def main():
    #     loop = asyncio.get_running_loop()
    #     result = await make_request('www.example.com', 80, loop)
    #     print(result)
    
    # asyncio.run(main())




    # # an http request with stream readers and writers
    # import asyncio
    # from asyncio import StreamReader
    # from typing import AsyncGenerator
    
    # async def read_until_empty(stream_reader: StreamReader) -> AsyncGenerator[str, None]:
    #     while response := await stream_reader.readline():
    #         yield response.decode()
    
    # async def main():
    #     host: str = 'www.example.com'
    #     request: str = f"GET / HTTP/1.1\r\n" \
    #                 f"Connection: close\r\n" \
    #                 f"Host: {host}\r\n\r\n"
    
    #     stream_reader, stream_writer = await asyncio.open_connection(host, 80)
    
    #     try:
    #         stream_writer.write(request.encode())
    #         await stream_writer.drain()
    
    #         responses = [response async for response in read_until_empty(stream_reader)]
    
    #         print(''.join(responses))
    #     finally:
    #         stream_writer.close()
    #         await stream_writer.wait_closed()
    
    # asyncio.run(main())




    # # attempting background tasks
    # import asyncio
    # from util import delay
    
    # async def main():
    
    #     while delay_time := input('Enter a time to sleep:'):
    #         asyncio.create_task(delay(int(delay_time)))
    
    # asyncio.run(main())




    # # using stream readers for input
    # import asyncio
    # from util import create_stdin_reader
    # from util import delay
    
    # async def main():
    #     stdin_reader = await create_stdin_reader()
    #     while True:
    #         delay_time = await stdin_reader.readline()
    #         if delay_time == b'\n':
    #             break
    #         asyncio.create_task(delay(int(delay_time)))
    
    # asyncio.run(main())




    # # 
    # import asyncio
    # import os
    # import tty
    # import sys
    # from collections import deque
    # from util.stdin_reader import MessageStore, create_stdin_reader, read_line
    # from util.stdin_reader import move_to_bottom_of_screen, save_cursor_position, restore_cursor_position
    # from util.stdin_reader import move_to_bottom_of_screen, move_to_top_of_screen, delete_line
    
    
    # async def sleep(delay: int, message_store: MessageStore):
    #     await message_store.append(f'Starting delay {delay}')
    #     await asyncio.sleep(delay)
    #     await message_store.append(f'Finished delay {delay}')
    
    
    # async def main():
    #     tty.setcbreak(sys.stdin)
    #     os.system('clear')
    #     rows = move_to_bottom_of_screen()
    
    #     async def redraw_output(items: deque):
    #         save_cursor_position()
    #         move_to_top_of_screen()
    #         for item in items:
    #             delete_line()
    #             print(item)
    #         restore_cursor_position()
    
    #     messages = MessageStore(redraw_output, rows - 1)
    
    #     stdin_reader = await create_stdin_reader()
    
    #     while True:
    #         line = await read_line(stdin_reader)
    #         delay_time = int(line)
    #         asyncio.create_task(sleep(delay_time, messages))
    
    # asyncio.run(main())




    # a chat server
    from util import ChatServer
    import asyncio

    async def main():
        chat_server = ChatServer()
        await chat_server.start_chat_server('0.0.0.0', 8000)
    
    
    asyncio.run(main())








    pass