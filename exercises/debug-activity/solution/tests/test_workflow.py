import pytest
from activities import PizzaOrderActivities
from shared import Address, Distance
from temporalio import activity
from temporalio.client import WorkflowFailureError
from temporalio.exceptions import ApplicationError
from temporalio.testing import WorkflowEnvironment
from temporalio.worker import Worker
from utils import create_pizza_order_for_test
from workflow import PizzaOrderWorkflow


@pytest.mark.asyncio
async def test_successful_pizza_order():
    async with await WorkflowEnvironment.start_time_skipping() as env:
        activities = PizzaOrderActivities()
        async with Worker(
            env.client,
            task_queue="test-pizza-order",
            workflows=[PizzaOrderWorkflow],
            activities=[activities.get_distance, activities.send_bill],
        ):
            order = create_pizza_order_for_test()
            confirmation = await env.client.execute_workflow(
                PizzaOrderWorkflow.order_pizza,
                order,
                id="test-translation-workflow-id",
                task_queue="test-pizza-order",
            )

            assert "XD001" == confirmation.order_number
            assert "SUCCESS" == confirmation.status
            assert "P24601" == confirmation.confirmation_number
            assert 2700 == confirmation.amount
            assert "" != confirmation.billing_timestamp


@activity.defn(name="get_distance")
async def get_distance_mocked(address: Address):
    return Distance(30)


@pytest.mark.asyncio
async def test_failed_pizza_order_outside_delivery_error():
    async with await WorkflowEnvironment.start_time_skipping() as env:
        with pytest.raises(WorkflowFailureError) as e:
            activities = PizzaOrderActivities()
            async with Worker(
                env.client,
                task_queue="test-pizza-order",
                workflows=[PizzaOrderWorkflow],
                activities=[get_distance_mocked, activities.send_bill],
            ):
                order = create_pizza_order_for_test()

                confirmation = await env.client.execute_workflow(
                    PizzaOrderWorkflow.order_pizza,
                    order,
                    id="test-translation-workflow-id",
                    task_queue="test-pizza-order",
                )
        assert isinstance(e.value.cause, ApplicationError)
        assert "Customer lives outside the service area" == str(e.value.cause)
