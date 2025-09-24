import asyncio

async def brew(name):
    print(f"Brewing {name}")
    await asyncio.sleep(2)  # exactly wait in non blocking fashion
    print("Ready")

async def main():
    await asyncio.gather(brew("Ginger tea"), brew("Chai"), brew("Oolong tea"))

asyncio.run(main()) 
# we waited combinely 2 seconds , non blocking operation