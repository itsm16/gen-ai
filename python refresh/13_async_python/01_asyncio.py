import asyncio

async def brew():
    print("line one")
    await asyncio.sleep(2)
    print("after sleep")

asyncio.run(brew());