import asyncio
import aiohttp

from temporalio.client import Client
from temporalio.worker import Worker

from activities import PizzaOrderActivities
from workflow import PizzaOrderWorkflow
from shared import TASK_QUEUE_NAME


async def main():
    client = await Client.connect("localhost:7233", namespace="default")

    activities = PizzaOrderActivities()

    worker = Worker(
        client,
        task_queue=TASK_QUEUE_NAME,
        workflows=[PizzaOrderWorkflow],
        activities=[activities.get_distance, activities.send_bill],
    )
    print("Starting the worker....")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
