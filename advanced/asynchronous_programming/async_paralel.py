### Async with Paralelism ###

from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

async def process_request(request_data):
    # Perform some processing on the request data
    # This can be a time-consuming operation

    # Return the processed result
    await asyncio.sleep(1)
    return f"Processed: {request_data}"

@app.get("/")
async def index():
    request_data = ["request1", "request2", "request3"]  # Example request data

    # Create a list of coroutines
    coroutines = [process_request(data) for data in request_data]

    # Execute coroutines concurrently using asyncio.gather()
    results = await asyncio.gather(*coroutines)

    return results

if __name__ == "__main__":
    uvicorn.run(
        "async_paralel:app",
        host="127.0.0.1",
        port=8000,
        reload=False,
        workers=8  # Set the number of workers for parallelism
    )