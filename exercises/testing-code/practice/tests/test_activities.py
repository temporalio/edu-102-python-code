import aiohttp
import pytest
from activities import TranslationActivities
from shared import TranslationActivityInput, TranslationActivityOutput
from temporalio.testing import ActivityEnvironment


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input, output",
    [
        (
            TranslationActivityInput(term="hello", language_code="de"),
            TranslationActivityOutput("Hallo"),
        ),
        # TODO add a second test cases input and output here
    ],
)
async def test_success_translate_activity_hello_german(input, output):
    async with aiohttp.ClientSession() as session:
        activity_environment = ActivityEnvironment()
        activities = TranslationActivities(session)
        assert output == await activity_environment.run(
            activities.translate_term, input
        )


# TODO add `test_failed_translate_acivity_bad_language_code` here
