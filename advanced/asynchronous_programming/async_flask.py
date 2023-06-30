### Async with Flask ###

# When working with Flask, which is a synchronous web framework, the use of async and await directly in Flask routes is not supported. 
# However, you can still leverage asynchronous programming by combining Flask with an asynchronous web server or using asynchronous libraries for specific tasks. 


from flask import Flask
import asyncio

app = Flask(__name__)

# Asynchronous task
async def perform_async_task():
    await asyncio.sleep(10)  # Simulating an asynchronous operation
    return "Async task completed"

# Flask route
@app.route("/")
def index():
    result = asyncio.run(perform_async_task())
    return result

if __name__ == "__main__":
    # Setting threaded=True in app.run() allows the Flask application to handle multiple requests concurrently in separate threads.
    app.run(threaded=True)
