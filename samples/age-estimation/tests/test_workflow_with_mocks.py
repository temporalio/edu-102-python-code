import aiohttp
import pytest
from activities import AgeEstimationActivities
from temporalio.testing import WorkflowEnvironment
from temporalio.worker import Worker
from temporalio import activity
from workflow import EstimateAgeWorkflow
from shared import EstimatorResponse


@activity.defn(name="retrieve_estimate")
async def estimate_age_mocked(input: str) -> EstimatorResponse:
    if input == "Stanislav":
        return EstimatorResponse(name="Stanislav", count=8928, age=21)
    else:
        return EstimatorResponse(name="Mason", count=1487, age=40)


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
                activities=[estimate_age_mocked],
            ):
                input = "Stanislav"
                output = await env.client.execute_workflow(
                    EstimateAgeWorkflow.run,
                    input,
                    id="test-age-estimation-workflow-mason",
                    task_queue=tq,
                )
                assert f"{input} has an estimated age of 21" == output
