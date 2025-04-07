import aiohttp
import pytest
from activities import AgeEstimationActivities
from temporalio.testing import WorkflowEnvironment
from temporalio.worker import Worker
from workflow import EstimateAgeWorkflow


@pytest.mark.asyncio
async def test_successful_age_estimation():
    async with await WorkflowEnvironment.start_time_skipping() as env:
        tq = "age-estimation-workflow"
        async with aiohttp.ClientSession() as session:
            activities = AgeEstimationActivities(session)
            async with Worker(
                env.client,
                task_queue=tq,
                workflows=[EstimateAgeWorkflow],
                activities=[activities.retrieve_estimate],
            ):
                input = "Mason"
                output = await env.client.execute_workflow(
                    EstimateAgeWorkflow.run,
                    input,
                    id="test-age-estimation-workflow-mason",
                    task_queue=tq,
                )
                assert f"{input} has an estimated age of 40" == output
