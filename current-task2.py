import asyncio
import time

async def main():
    # report a massage
    print(f'{time.ctime()} main coroutine started ')
    # get the current task
    task = asyncio.current_task()
    # report its detail
    print(f'{time.ctime()}{task}')

    asyncio.run(main())