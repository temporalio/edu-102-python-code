import asyncio
import logging

import aiohttp
from activities import TranslationActivities
from shared import TASK_QUEUE_NAME
from temporalio.client import Client
from temporalio.worker import Worker
from workflow import TranslationWorkflow


async def main():
    logging.basicConfig(level=logging.INFO)
    client = await Client.connect("localhost:7233", namespace="default")

    # Run the worker
    async with aiohttp.ClientSession() as session:
        activities = TranslationActivities(session)

        worker = Worker(
            client,
            task_queue=TASK_QUEUE_NAME,
            workflows=[TranslationWorkflow],
            activities=[activities.translate_term],
        )
        logging.info(f"Starting the worker....{client.identity}")
        await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
