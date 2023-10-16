import asyncio
import sys

from shared import TASK_QUEUE_NAME, TranslationWorkflowInput
from temporalio.client import Client
from workflow import TranslationWorkflow


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233", namespace="default")

    # Execute a workflow
    handle = await client.start_workflow(
        TranslationWorkflow.run,
        TranslationWorkflowInput(name=sys.argv[1], language_code=sys.argv[2]),
        id="translation-tasks-example",
        task_queue=TASK_QUEUE_NAME,
    )

    print(f"Started workflow. Workflow ID: {handle.id}, RunID {handle.result_run_id}")

    result = await handle.result()

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
