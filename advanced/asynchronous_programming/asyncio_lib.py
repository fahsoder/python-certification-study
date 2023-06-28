### Async Library ###

## Simple async 
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello())


## Multiple Tasks 
async def greet(name):
    print(f"Hello, {name}!")

async def main():
    tasks = [
        asyncio.create_task(greet("Alice")),
        asyncio.create_task(greet("Bob")),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())


## Async File I/O
async def read_file():
    async with open("data.txt", "r") as file:
        content = await file.read()
        print(content)

asyncio.run(read_file())
