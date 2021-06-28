import asyncio
import time


async def func():
    print('world')
    await asyncio.sleep(3)

async def new_func():
    print('hello everyone')    

async def main():
    print('hello')
    task = asyncio.create_task(func())
    await new_func()
    

start_time = time.time()
asyncio.run(main())

# task = asyncio.create_task(func())

print("\n--- %s seconds ---" % (time.time() - start_time))