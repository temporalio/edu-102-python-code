import asyncio

from temporalio.client import Client

from workflow import PizzaOrderWorkflow
from shared import TASK_QUEUE_NAME, WORKFLOW_ID
from utils import create_pizza_order


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233")

    order = create_pizza_order()

    # Execute a workflow
    handle = await client.start_workflow(
        PizzaOrderWorkflow.order_pizza,
        order,
        id=WORKFLOW_ID + f"{order.order_number}",
        task_queue=TASK_QUEUE_NAME,
    )

    print(f"Started workflow. Workflow ID: {handle.id}, RunID {handle.result_run_id}")

    result = await handle.result()

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())