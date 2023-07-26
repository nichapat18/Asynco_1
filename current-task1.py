# example of getting the current task from the main corytine
import asyncio

#define a main corutine
async def main():
    #report a message
    print('main corutine started')
    #get the current task
    task = asyncio.current_task()
    #report its details
    print(task)

#start the asyncio program
asyncio.run(main())