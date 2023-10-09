import asyncio
import sys

from temporalio.client import Client

from workflow import LoanProcessingWorkflow
from shared import TASK_QUEUE_NAME, WORKFLOW_ID, create_customer_info_db


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    db = create_customer_info_db()

    customer_id = sys.argv[1]

    info = db.get(customer_id)

    # Execute a workflow
    handle = await client.start_workflow(
        LoanProcessingWorkflow.process_loan,
        info,
        id=WORKFLOW_ID + info.customer_id,
        task_queue=TASK_QUEUE_NAME,
    )

    print(f"Started workflow. Workflow ID: {handle.id}, RunID {handle.result_run_id}")

    result = await handle.result()

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
