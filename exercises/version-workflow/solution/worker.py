import asyncio

from activities import LoanProcessingActivities
from shared import TASK_QUEUE_NAME
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import LoanProcessingWorkflow


async def main():
    logging.basicConfig(level=logging.INFO)

    client = await Client.connect("localhost:7233", namespace="default")

    activities = LoanProcessingActivities()

    worker = Worker(
        client,
        task_queue=TASK_QUEUE_NAME,
        workflows=[LoanProcessingWorkflow],
        activities=[activities.charge_customer, activities.send_thank_you_to_customer],
    )
    print("Starting the worker....")
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
