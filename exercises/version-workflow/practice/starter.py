import asyncio
import logging
import sys

from shared import TASK_QUEUE_NAME, WORKFLOW_ID_PREFIX, create_customer_info_db
from temporalio.client import Client
from workflow import LoanProcessingWorkflow


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233", namespace="default")

    db = create_customer_info_db()

    customer_id = sys.argv[1]

    info = db.get(customer_id)

    # Execute a workflow
    handle = await client.start_workflow(
        LoanProcessingWorkflow.process_loan,
        info,
        id=WORKFLOW_ID_PREFIX + info.customer_id,
        task_queue=TASK_QUEUE_NAME,
    )

    logging.info(
        f"Started workflow. Workflow ID: {handle.id}, RunID {handle.result_run_id}"
    )

    result = await handle.result()

    logging.info(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
