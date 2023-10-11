import asyncio

from shared import TASK_QUEUE_NAME, WORKFLOW_ID_PREFIX, create_pizza_order
from temporalio.client import Client
from workflow import PizzaOrderWorkflow


async def main():
    # Create client connected to server at the given address
    client = await Client.connect("localhost:7233", namespace="default")

    order = create_pizza_order()

    # Execute a workflow
    handle = await client.start_workflow(
        PizzaOrderWorkflow.order_pizza,
        order,
        id=WORKFLOW_ID_PREFIX + f"{order.order_number}",
        task_queue=TASK_QUEUE_NAME,
    )

    print(f"Started workflow. Workflow ID: {handle.id}, RunID {handle.result_run_id}")

    result = await handle.result()

    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
