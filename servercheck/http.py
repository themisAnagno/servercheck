""" Module that implements the requests"""
import asyncio
import os
import requests

CONCURRENCY = 5


def check(request: str) -> int:
    """
    Checks the health of the given server
    """
    debug = os.getenv("DEBUG")
    url = f"http://{request}"
    try:
        req = requests.get(url=url)
        if debug:
            print(f"Successful request at server {request}")
        return req.status_code
    except requests.exceptions.RequestException as err:
        if debug:
            print(f"Unsuccessful request at server {request}", err)
        return -1


async def worker(worker_name: str, task_queue, results: dict) -> None:
    """
    Worker function that takes requests out of the queue and implements them, completing the results dictionary
    """
    # Get the current event loop
    cur_loop = asyncio.get_event_loop()
    while True:
        request = await task_queue.get()
        if os.getenv("DEBUG"):
            print(f"{worker_name} executes request on {request}")
        future_result = cur_loop.run_in_executor(None, check, request)
        result = await future_result
        if result in range(200, 300):
            results["success"].append(request)
        else:
            results["failure"].append(request)

        # Mark the request in queue as done
        task_queue.task_done()


async def distribure_work(server_list: set, results: dict) -> None:
    """
    Create the queue with the requests to be done, create tasks and call
    workers to implement the tasks
    """
    # Create the queue from asyncio Queue class that contains all the tasks (requests) that must be implemented
    queue = asyncio.Queue()

    # Add server request tasks in the queue
    for iserver in server_list:
        queue.put_nowait(iserver)

    # Create the list of workers. Each worker will impement a request from the queue
    workers = []
    for i in range(CONCURRENCY):
        new_worker = asyncio.create_task(worker(f"worker-{i+1}", queue, results))
        workers.append(new_worker)

    # Start the request queue and wait for them to finish. Workers will be triggered
    await queue.join()

    # Cancel/Destroy all the workers in the worker list
    for new_worker in workers:
        new_worker.cancel()


def make_req(server_list: set) -> dict:
    """
    Function that takes as input the list of the servers and returns a dictionary with the results
    """
    # Initiate the results dictionary
    results = {"success": [], "failure": []}
    asyncio.run(distribure_work(server_list, results))

    return results
