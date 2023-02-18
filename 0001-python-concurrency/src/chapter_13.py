def chapter_13():
    # #  running a simple command in a subprocess
    # import asyncio
    # from asyncio.subprocess import Process
    
    # async def main():
    #     process: Process = await asyncio.create_subprocess_exec('ls', '-l')
    #     print(f'Process pid is: {process.pid}')
    #     status_code = await process.wait()
    #     print(f'Status code: {status_code}')
    
    # asyncio.run(main())
    



    # # terminating a subprocess
    # import asyncio
    # from asyncio.subprocess import Process
    
    # async def main():
    #     process: Process = await asyncio.create_subprocess_exec('sleep', '3')
    #     print(f'Process pid is: {process.pid}')
    #     try:
    #         status_code = await asyncio.wait_for(process.wait(), timeout=1.0)
    #         print(status_code)
    #     except asyncio.TimeoutError:
    #         print('Timed out waiting to finish, terminating...')
    #         process.terminate()
    #         status_code = await process.wait()
    #         print(status_code)

    # asyncio.run(main())




    # # using the standard out stream reader
    # import asyncio
    # from asyncio import StreamReader
    # from asyncio.subprocess import Process
    
    # async def write_output(prefix: str, stdout: StreamReader):
    #     while line := await stdout.readline():
    #         print(f'[{prefix}]: {line.rstrip().decode()}')
    
    # async def main():
    #     program = ['ls', '-la']
    #     process: Process = await asyncio.create_subprocess_exec(*program,
    #                                                             stdout=asyncio.subprocess.PIPE)
    #     print(f'Process pid is: {process.pid}')
    #     stdout_task = asyncio.create_task(write_output(' '.join(program), process.stdout))
    
    #     return_code, _ = await asyncio.gather(process.wait(), stdout_task)
    #     print(f'Process returned: {return_code}')
    
    # asyncio.run(main())
    



    # # a deadlock with pipes
    # import asyncio
    # from asyncio.subprocess import Process

    # async def main():
    #     program = ['python', 'util/deadlock.py']
    #     process: Process = await asyncio.create_subprocess_exec(*program,
    #                                                             stdout=asyncio.subprocess.PIPE)
    #     print(f'Process pid is: {process.pid}')
    
    #     return_code = await process.wait()
    #     print(f'Process returned: {return_code}')

    # asyncio.run(main())




    # # using communicate
    # import asyncio
    # from asyncio.subprocess import Process
    
    # async def main():
    #     program = ['python', 'util/deadlock.py']
    #     process: Process = await asyncio.create_subprocess_exec(*program,
    #                                                             stdout=asyncio.subprocess.PIPE)
    #     print(f'Process pid is: {process.pid}')
    
    #     stdout, stderr = await process.communicate()
    #     print(stdout)
    #     print(stderr)
    #     print(f'Process returned: {process.returncode}')
    
    # asyncio.run(main())




    # # encrypting text concurrently
    # import asyncio
    # import random
    # import string
    # import time
    # from asyncio.subprocess import Process
    
    # async def encrypt(text: str) -> bytes:
    #     program = ['gpg', '-c', '--batch', '--passphrase', '3ncryptm3', '--cipher-algo', 'TWOFISH']
    
    #     process: Process = await asyncio.create_subprocess_exec(*program,
    #                                                             stdout=asyncio.subprocess.PIPE,
    #                                                             stdin=asyncio.subprocess.PIPE)
    #     stdout, stderr = await process.communicate(text.encode())
    #     return stdout
    
    # async def main():
    #     text_list = [''.join(random.choice(string.ascii_letters) for _ in range(1000)) for _ in range(100)]
    
    #     s = time.time()
    #     tasks = [asyncio.create_task(encrypt(text)) for text in text_list]
    #     encrypted_text = await asyncio.gather(*tasks)
    #     e = time.time()
    
    #     print(f'Total time: {e - s}')
    #     print(encrypted_text)
    
    # asyncio.run(main())




    # # subprocesses with a semaphore
    # import asyncio
    # import random
    # import string
    # import time
    # import os
    # from asyncio import Semaphore
    # from asyncio.subprocess import Process
    
    # async def encrypt(sem: Semaphore, text: str) -> bytes:
    #     program = ['gpg', '-c', '--batch', '--passphrase', '3ncryptm3', '--cipher-algo', 'TWOFISH']
    
    #     async with sem:
    #         process: Process = await asyncio.create_subprocess_exec(*program,
    #                                                                 stdout=asyncio.subprocess.PIPE,
    #                                                                 stdin=asyncio.subprocess.PIPE)
    #         stdout, stderr = await process.communicate(text.encode())
    #         return stdout
    
    # async def main():
    #     text_list = [''.join(random.choice(string.ascii_letters) for _ in range(1000)) for _ in range(1000)]
    #     semaphore = Semaphore(os.cpu_count())
    #     s = time.time()
    #     tasks = [asyncio.create_task(encrypt(semaphore, text)) for text in text_list]
    #     encrypted_text = await asyncio.gather(*tasks)
    #     e = time.time()
    
    #     print(f'Total time: {e - s}')
    
    # asyncio.run(main())




    # # using communicate with standard in
    # import asyncio
    # from asyncio.subprocess import Process
    
    # async def main():
    #     program = ['python', 'util/standard_in.py']
    #     process: Process = await asyncio.create_subprocess_exec(*program,
    #                                                             stdout=asyncio.subprocess.PIPE,
    #                                                             stdin=asyncio.subprocess.PIPE)
    
    #     stdout, stderr = await process.communicate(b'Zoot')
    #     print(stdout)
    #     print(stderr)
    
    # asyncio.run(main())




    # # using the echo application with subprocesses
    # import asyncio
    # from asyncio import StreamWriter, StreamReader
    # from asyncio.subprocess import Process
    
    # async def consume_and_send(text_list, stdout: StreamReader, stdin: StreamWriter):
    #     for text in text_list:
    #         line = await stdout.read(2048)
    #         print(line)
    #         stdin.write(text.encode())
    #         await stdin.drain()
    
    # async def main():
    #     program = ['python', 'util/echo.py']
    #     process: Process = await asyncio.create_subprocess_exec(*program,
    #                                                             stdout=asyncio.subprocess.PIPE,
    #                                                             stdin=asyncio.subprocess.PIPE)
    
    #     text_input = ['one\n', 'two\n', 'three\n', 'four\n', 'quit\n']
    #     await asyncio.gather(consume_and_send(text_input, process.stdout, process.stdin), process.wait())
    
    # asyncio.run(main())




    # decoupling output reading from input writing
    import asyncio
    from asyncio import StreamWriter, StreamReader, Event
    from asyncio.subprocess import Process
    
    async def output_consumer(input_ready_event: Event, stdout: StreamReader):
        while (data := await stdout.read(1024)) != b'':
            print(data)
            if data.decode().endswith("Enter text to echo: "):
                input_ready_event.set()
    
    async def input_writer(text_data, input_ready_event: Event, stdin: StreamWriter):
        for text in text_data:
            await input_ready_event.wait()
            stdin.write(text.encode())
            await stdin.drain()
            input_ready_event.clear()
    
    async def main():
        program = ['python', 'util/echo_2.py']
        process: Process = await asyncio.create_subprocess_exec(*program,
                                                                stdout=asyncio.subprocess.PIPE,
                                                                stdin=asyncio.subprocess.PIPE)
    
        input_ready_event = asyncio.Event()
    
        text_input = ['one\n', 'two\n', 'three\n', 'four\n', 'quit\n']
    
        await asyncio.gather(output_consumer(input_ready_event, process.stdout),
                            input_writer(text_input, input_ready_event, process.stdin),
                            process.wait())
    
    asyncio.run(main())
    
    
    


    pass