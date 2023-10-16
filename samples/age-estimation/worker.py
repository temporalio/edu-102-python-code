import asyncio

import aiohttp
from activities import AgeEstimationActivities
from shared import TASK_QUEUE_NAME
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import EstimateAge


async def main():
    client = await Client.connect("localhost:7233", namespace="default")

    # Run the worker
    async with aiohttp.ClientSession() as session:
        activities = AgeEstimationActivities(session)

        worker = Worker(
            client,
            task_queue=TASK_QUEUE_NAME,
            workflows=[EstimateAge],
            activities=[activities.retrieve_estimate],
        )
        print("Starting the worker....")
        await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
