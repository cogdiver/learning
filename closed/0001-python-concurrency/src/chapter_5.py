password = 'mysecretpassword'

def chapter_5():
    # # connecting to a Postgres database as the default user
    # import asyncpg
    # import asyncio

    # async def main():
    #     connection = await asyncpg.connect(host='0.0.0.0',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='postgres',
    #                                     password=password)

    #     version = connection.get_server_version()
    #     print(f'Connected! Postgres version is {version}')
    #     await connection.close()

    # asyncio.run(main())




    # # Using a execute to run create statements
    # import asyncpg
    # import asyncio
    # from util.queries import CREATE_BRAND_TABLE
    # from util.queries import CREATE_PRODUCT_TABLE
    # from util.queries import CREATE_PRODUCT_COLOR_TABLE
    # from util.queries import CREATE_PRODUCT_SIZE_TABLE
    # from util.queries import CREATE_SKU_TABLE
    # from util.queries import SIZE_INSERT
    # from util.queries import COLOR_INSERT


    # async def main():
    #     connection = await asyncpg.connect(host='0.0.0.0',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)
    #     statements = [CREATE_BRAND_TABLE,
    #                 CREATE_PRODUCT_TABLE,
    #                 CREATE_PRODUCT_COLOR_TABLE,
    #                 CREATE_PRODUCT_SIZE_TABLE,
    #                 CREATE_SKU_TABLE,
    #                 SIZE_INSERT,
    #                 COLOR_INSERT]

    #     print('Creating the product database...')
    #     for statement in statements:
    #         status = await connection.execute(statement)
    #         print(status)
    #     print('Finished creating the product database!')
    #     await connection.close()

    # asyncio.run(main())




    # # Inserting and selecting brands
    # import asyncpg
    # import asyncio
    # from asyncpg import Record
    # from typing import List
    # from util import async_timed

    # @async_timed()
    # async def main():
    #     connection = await asyncpg.connect(host='0.0.0.0',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)

    #     # await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    #     # await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

    #     brand_query = 'SELECT brand_id, brand_name FROM brand'
    #     results: List[Record] = await connection.fetch(brand_query)
    #     results_2: Record = await connection.fetchrow(brand_query)

    #     print('-'*20)
    #     print(results)
    #     print(results_2)
    #     print('-'*20)

    #     for brand in results:
    #         print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')

    #     await connection.close()

    # asyncio.run(main())




    # inserting random brands
    import asyncpg
    import asyncio
    from typing import List, Tuple, Union
    from random import sample


    def load_common_words() -> List[str]:
        with open('data/common_words.txt') as common_words:
            return [w.replace('\n','') for w in common_words.readlines()]


    def generate_brand_names(words: List[str]) -> List[List]:
        return [[words[index]] for index in sample(range(100), 100)]


    async def insert_brands(common_words, connection) -> int:
        brands = generate_brand_names(common_words)
        insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
        return await connection.executemany(insert_brands, brands)


    async def main():
        common_words = load_common_words()
        connection = await asyncpg.connect(host='127.0.0.1',
                                        port=5432,
                                        user='postgres',
                                        database='products',
                                        password=password)

        await insert_brands(common_words, connection)
        await connection.close()

    asyncio.run(main())




    # # inserting random products and skus
    # import asyncpg
    # import asyncio
    # from random import randint
    # from typing import List, Tuple
    # from random import sample

    # def load_common_words() -> List[str]:
    #     with open('data/common_words.txt') as common_words:
    #         return [w.replace('\n','') for w in common_words.readlines()]


    # def gen_products(common_words: List[str],
    #                 brand_id_start: int,
    #                 brand_id_end: int,
    #                 products_to_create: int) -> List[Tuple[str, int]]:

    #     products = []
    #     for _ in range(products_to_create):
    #         description = [common_words[index] for index in sample(range(1000), 10)]
    #         brand_id = randint(brand_id_start, brand_id_end)
    #         products.append((" ".join(description), brand_id))
    #     return products


    # def gen_skus(product_id_start: int,
    #             product_id_end: int,
    #             skus_to_create: int) -> List[Tuple[int, int, int]]:

    #     skus = []
    #     for _ in range(skus_to_create):
    #         product_id = randint(product_id_start, product_id_end)
    #         size_id = randint(1, 3)
    #         color_id = randint(1, 2)
    #         skus.append((product_id, size_id, color_id))
    #     return skus


    # async def main():
    #     common_words = load_common_words()
    #     connection = await asyncpg.connect(host='127.0.0.1',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)

    #     product_tuples = gen_products(common_words,
    #                                 brand_id_start=1,
    #                                 brand_id_end=100,
    #                                 products_to_create=1000)
    #     await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)",
    #                                 product_tuples)

    #     sku_tuples = gen_skus(product_id_start=1,
    #                         product_id_end=1000,
    #                         skus_to_create=100000)
    #     await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)",
    #                                 sku_tuples)

    #     await connection.close()

    # asyncio.run(main())




    # # Try to apply asyncio.gather with our existing connection
    # import asyncio
    # import asyncpg
    # from util.queries import product_query

    # async def main():
    #     connection = await asyncpg.connect(host='0.0.0.0',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)
    #     print('Creating the product database...')
    #     queries = [connection.execute(product_query),
    #             connection.execute(product_query)]
    #     results = await asyncio.gather(*queries)

    # asyncio.run(main())




    # # establishing a connection pool and running queries concurrently
    # import asyncio
    # import asyncpg
    # from util.queries import product_query

    # async def query_product(pool):
    #     async with pool.acquire() as connection:
    #         return await connection.fetchrow(product_query)


    # async def main():
    #     async with asyncpg.create_pool(host='127.0.0.1',
    #                                 port=5432,
    #                                 user='postgres',
    #                                 password=password,
    #                                 database='products',
    #                                 min_size=6,
    #                                 max_size=6) as pool:

    #         await asyncio.gather(query_product(pool),
    #                             query_product(pool))


    # asyncio.run(main())




    # # Synchronous queries versus concurrent
    # import asyncio
    # import asyncpg
    # from util import async_timed
    # from util.queries import product_query

    # async def query_product(pool):
    #     async with pool.acquire() as connection:
    #         return await connection.fetchrow(product_query)

    # @async_timed()
    # async def query_products_synchronously(pool, queries):
    #     return [await query_product(pool) for _ in range(queries)]


    # @async_timed()
    # async def query_products_concurrently(pool, queries):
    #     queries = [query_product(pool) for _ in range(queries)]
    #     return await asyncio.gather(*queries)


    # async def main():
    #     async with asyncpg.create_pool(host='127.0.0.1',
    #                                 port=5432,
    #                                 user='postgres',
    #                                 password=password,
    #                                 database='products',
    #                                 min_size=6,
    #                                 max_size=6) as pool:

    #         await query_products_synchronously(pool, 10000)
    #         await query_products_concurrently(pool, 10000)

    # asyncio.run(main())




    # # creating a transaction
    # import asyncio
    # import asyncpg

    # async def main():
    #     connection = await asyncpg.connect(host='127.0.0.1',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)

    #     async with connection.transaction():
    #         await connection.execute("INSERT INTO brand "
    #                                 "VALUES(DEFAULT, 'brand_1')")
    #         await connection.execute("INSERT INTO brand "
    #                                 "VALUES(DEFAULT, 'brand_2')")

    #     query = """SELECT brand_name FROM brand
    #                 WHERE brand_name LIKE 'brand%'"""
    #     brands = await connection.fetch(query)
    #     print(brands)

    #     await connection.close()

    # asyncio.run(main())




    # # handling an error in a transaction
    # import asyncio
    # import logging
    # import asyncpg

    # async def main():
    #     connection = await asyncpg.connect(host='127.0.0.1',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)
    #     try:
    #         async with connection.transaction():
    #             insert_brand = "INSERT INTO brand VALUES(9999, 'big_brand')"
    #             await connection.execute(insert_brand)
    #             await connection.execute(insert_brand)
    #     except Exception:
    #         logging.exception('Error while running transaction')
    #     finally:
    #         query = """SELECT brand_name FROM brand
    #                     WHERE brand_name LIKE 'big_%'"""
    #         brands = await connection.fetch(query)
    #         print(f'Query result was: {brands}')

    #         await connection.close()

    # asyncio.run(main())




    # # Nested transactions
    # import asyncio
    # import asyncpg
    # import logging


    # async def main():
    #     connection = await asyncpg.connect(host='127.0.0.1',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)

    #     async with connection.transaction():
    #         await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'my_new_brand')")

    #         try:
    #             async with connection.transaction():
    #                 await connection.execute("INSERT INTO product_color VALUES(1, 'black')")
    #         except Exception as ex:
    #             logging.warning('Ignoring error inserting product color', exc_info=ex)

    #     await connection.close()

    # asyncio.run(main())




    # # manually managing a transaction
    # import asyncio
    # import asyncpg
    # from asyncpg.transaction import Transaction


    # async def main():
    #     connection = await asyncpg.connect(host='127.0.0.1',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)

    #     transaction: Transaction = connection.transaction()
    #     await transaction.start()
    #     try:
    #         await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_1')")
    #         await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'brand_2')")
    #     except asyncpg.PostgresError:
    #         print('Errors, rolling back transaction!')
    #         await transaction.rollback()
    #     else:
    #         print('No errors, committing transaction!')
    #         await transaction.commit()

    #     query = """SELECT brand_name FROM brand
    #                 WHERE brand_name LIKE 'brand%'"""
    #     brands = await connection.fetch(query)
    #     print(brands)

    #     await connection.close()

    # asyncio.run(main())




    # # a simple asynchronous generator
    # import asyncio
    # from util import delay, async_timed

    # async def positive_integers_async(until: int):
    #     for integer in range(1, until):
    #         await delay(integer)
    #         yield integer

    # @async_timed()
    # async def main():
    #     async_generator = positive_integers_async(3)
    #     print(type(async_generator))
    #     async for number in async_generator:
    #         print(f'Got number {number}')

    # asyncio.run(main())




    # # streaming results one by one
    # import asyncpg
    # import asyncio
    # import asyncpg
    # from util import async_timed

    # @async_timed()
    # async def main():
    #     connection = await asyncpg.connect(host='127.0.0.1',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)

    #     query = 'SELECT product_id, product_name FROM product'
    #     async with connection.transaction():
    #         async for product in connection.cursor(query):
    #             print(product)

    #     await connection.close()

    # asyncio.run(main())




    # # moving the cursor and fetching records
    # import asyncpg
    # import asyncio


    # async def main():
    #     connection = await asyncpg.connect(host='127.0.0.1',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)

    #     async with connection.transaction():
    #         query = 'SELECT product_id, product_name from product'
    #         cursor = await connection.cursor(query)
    #         await cursor.forward(500)
    #         products = await cursor.fetch(100)
    #         for product in products:
    #             print(product)

    #     await connection.close()

    # asyncio.run(main())




    # # getting a specific number of elements with an asynchronous generator
    # import asyncpg
    # import asyncio


    # async def take(generator, to_take: int):
    #     item_count = 0
    #     async for item in generator:
    #         yield item
    #         item_count = item_count + 1
    #         if item_count > to_take - 1:
    #             return


    # async def main():
    #     connection = await asyncpg.connect(host='127.0.0.1',
    #                                     port=5432,
    #                                     user='postgres',
    #                                     database='products',
    #                                     password=password)

    #     async with connection.transaction():
    #         query = 'SELECT product_id, product_name from product'
    #         product_generator = connection.cursor(query)

    #         async for product in take(product_generator, 5):
    #             print(product)

    #         print('Got the first five products!')

    #     await connection.close()

    # asyncio.run(main())
