def chapter_12():
    # # a supermarket checkout queue
    # import asyncio
    # from asyncio import Queue
    # from random import randrange
    # from typing import List
    
    # class Product:
    #     def __init__(self, name: str, checkout_time: float):
    #         self.name = name
    #         self.checkout_time = checkout_time
    
    # class Customer:
    #     def __init__(self, customer_id: int, products: List[Product]):
    #         self.customer_id = customer_id
    #         self.products = products
    
    # async def checkout_customer(queue: Queue, cashier_number: int):
    #     while not queue.empty():
    #         customer: Customer = queue.get_nowait()
    #         print(f'Cashier {cashier_number} checking out customer {customer.customer_id}')
    #         for product in customer.products:
    #             print(f"Cashier {cashier_number} checking out customer {customer.customer_id}'s {product.name}")
    #             await asyncio.sleep(product.checkout_time)
    #         print(f'Cashier {cashier_number} finished checking out customer {customer.customer_id}')
    #         queue.task_done()
    
    # async def main():
    #     customer_queue = Queue()
    
    #     all_products = [Product('beer', 2),
    #                     Product('bananas', .5),
    #                     Product('sausage', .2),
    #                     Product('diapers', .2)]
    
    #     for i in range(10):
    #         products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]
    #         customer_queue.put_nowait(Customer(i, products))
    
    #     cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(3)]
    
    #     await asyncio.gather(customer_queue.join(), *cashiers)
    
    # asyncio.run(main())




    # asyncio.queues.QueueEmpty
    # import asyncio
    # from asyncio import Queue
    
    # async def main():
    #     customer_queue = Queue()
    #     customer_queue.get_nowait()
    
    # asyncio.run(main())




    # # asyncio.queues.QueueFull
    # import asyncio
    # from asyncio import Queue
    
    # async def main():
    #     queue = Queue(maxsize=1)
    
    #     queue.put_nowait(1)
    #     queue.put_nowait(2)
    
    # asyncio.run(main())




    # # using coroutine queue methods
    # import asyncio
    # from asyncio import Queue
    # from random import randrange
    
    # class Product:
    #     def __init__(self, name: str, checkout_time: float):
    #         self.name = name
    #         self.checkout_time = checkout_time
    
    # class Customer:
    #     def __init__(self, customer_id, products):
    #         self.customer_id = customer_id
    #         self.products = products
    
    # async def checkout_customer(queue: Queue, cashier_number: int):
    #     while True:
    #         customer: Customer = await queue.get()
    #         print(f'Cashier {cashier_number} checking out customer {customer.customer_id}')
    #         for product in customer.products:
    #             print(f"Cashier {cashier_number} checking out customer {customer.customer_id}'s {product.name}")
    #             await asyncio.sleep(product.checkout_time)
    #         print(f'Cashier {cashier_number} finished checking out customer {customer.customer_id}')
    #         queue.task_done()
    
    # def generate_customer(customer_id: int) -> Customer:
    #     all_products = [Product('beer', 2),
    #                     Product('bananas', .5),
    #                     Product('sausage', .2),
    #                     Product('diapers', .2)]
    #     products = [all_products[randrange(len(all_products))] for _ in range(randrange(10))]
    #     return Customer(customer_id, products)
    
    # async def customer_generator(queue: Queue):
    #     customer_count = 0
    
    #     while True:
    #         customers = [generate_customer(i) for i in range(customer_count, customer_count + randrange(5))]
    #         for customer in customers:
    #             print('Waiting to put customer in line...')
    #             await queue.put(customer)
    #             print('Customer put in line!')
    #         customer_count = customer_count + len(customers)
    #         await asyncio.sleep(1)
    
    # async def main():
    #     customer_queue = Queue(5)
    #     customer_producer = asyncio.create_task(customer_generator(customer_queue))
    #     cashiers = [asyncio.create_task(checkout_customer(customer_queue, i)) for i in range(3)]
    #     await asyncio.gather(customer_producer, *cashiers)
    
    # asyncio.run(main())




    # # priority queues with tuples
    # import asyncio
    # from asyncio import Queue, PriorityQueue
    # from typing import Tuple
    
    # async def worker(queue: Queue):
    #     while not queue.empty():
    #         work_item: Tuple[int, str] = await queue.get()
    #         print(f'Processing work item {work_item}')
    #         queue.task_done()
    
    # async def main():
    #     priority_queue = PriorityQueue()
    
    #     work_items = [(3, 'Lowest priority'),
    #                 (2, 'Medium priority'),
    #                 (2, 'Medium priority'),
    #                 (1, 'High priority')]
    
    #     worker_task = asyncio.create_task(worker(priority_queue))
    
    #     for work in work_items:
    #         priority_queue.put_nowait(work)
    
    #     await asyncio.gather(priority_queue.join(), worker_task)
    
    # asyncio.run(main())




    # # priority queues with data classes
    # import asyncio
    # from asyncio import Queue, PriorityQueue
    # from dataclasses import dataclass, field
    
    # @dataclass(order=True)
    # class WorkItem:
    #     priority: int
    #     data: str = field(compare=False)
    
    # async def worker(queue: Queue):
    #     while not queue.empty():
    #         work_item: WorkItem = await queue.get()
    #         print(f'Processing work item {work_item}')
    #         queue.task_done()
    
    # async def main():
    #     priority_queue = PriorityQueue()
    
    #     work_items = [WorkItem(3, 'Lowest priority'),
    #                 WorkItem(2, 'Medium priority'),
    #                 WorkItem(1, 'High priority')]
    
    #     worker_task = asyncio.create_task(worker(priority_queue))
    
    #     for work in work_items:
    #         priority_queue.put_nowait(work)
    
    #     await asyncio.gather(priority_queue.join(), worker_task)
    
    # asyncio.run(main())




    # a lifo queue
    import asyncio
    from asyncio import Queue, LifoQueue
    from dataclasses import dataclass, field
    
    @dataclass(order=True)
    class WorkItem:
        priority: int
        order: int
        data: str = field(compare=False)
    
    async def worker(queue: Queue):
        while not queue.empty():
            work_item: WorkItem = await queue.get()
            print(f'Processing work item {work_item}')
            queue.task_done()
    
    async def main():
        lifo_queue = LifoQueue()
    
        work_items = [WorkItem(3, 1, 'Lowest priority first'),
                    WorkItem(3, 2, 'Lowest priority second'),
                    WorkItem(3, 3, 'Lowest priority third'),
                    WorkItem(2, 4, 'Medium priority'),
                    WorkItem(1, 5, 'High priority')]
    
        worker_task = asyncio.create_task(worker(lifo_queue))
    
        for work in work_items:
            lifo_queue.put_nowait(work)
    
        await asyncio.gather(lifo_queue.join(), worker_task)
    
    asyncio.run(main())





    pass