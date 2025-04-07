import aiohttp
import pytest
from activities import AgeEstimationActivities
from temporalio.testing import ActivityEnvironment


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input, output",
    [
        ("Mason", 40),
    ],
)
async def test_retrieve_estimate(input, output):
    async with aiohttp.ClientSession() as session:
        activity_environment = ActivityEnvironment()
        activities = AgeEstimationActivities(session)
        result = await activity_environment.run(activities.retrieve_estimate, input)
        assert output == result.age
