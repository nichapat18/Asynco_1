# example of running a corutine
import asyncio

#defind a corutine
async def custom_coro():
# awat for a tak to be done
# await another corutine
    await asyncio.sleep(1)

    #main corutine
    async def main():
        #execute my custom corutine
        await custom_coro()

        #start the corutine programs
        asyncio.run(main())