### Async with FastAPI ###

# FastAPI is built on top of the asyncio library and provides native support for asynchronous request handling. 
# It offers high performance, automatic validation and serialization, and is designed to be easy to use.
from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

# Asynchronous route
@app.get("/")
async def index():
    await some_async_operation()  # Perform an asynchronous operation
    return {"message": "Async operation completed"}

# Asynchronous function
async def some_async_operation():
    # Perform some asynchronous tasks here
    await asyncio.sleep(5)

if __name__ == "__main__":
    uvicorn.run(app)
