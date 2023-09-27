import asyncio
import sys

from workflow import TranslationWorkflow
from temporalio.client import Client
from shared import (
    TASK_QUEUE_NAME,
    WORKFLOW_ID,
    TranslationWorkflowInput,
)


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    # Execute a workflow
    handle = await client.start_workflow(
        TranslationWorkflow.run,
        TranslationWorkflowInput(name=sys.argv[1], language_code=sys.argv[2]),
        id=WORKFLOW_ID,
        task_queue=TASK_QUEUE_NAME,
    )

    print(f"Started workflow. Workflow ID: {handle.id}, RunID {handle.result_run_id}")

    result = await handle.result()

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
