# example of waiting for all tasks to complete
import random
import asyncio
import time

# corotine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random.random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'{time.ctime()} >task {arg} done with {value}')

# main corotine
async def main():
    # create many task
    tasks = [asyncio.create_task(task_coro(i)) for i in range(20000)]
    # wait for all tasks to complete #ALL_COMPLETED, FIRST_COMPLETED, FIRST_EXCEPTION
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    # report result
    print(f'{time.ctime()} All done')

# start the asyncio program
asyncio.run(main())