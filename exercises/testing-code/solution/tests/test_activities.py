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
        (
            TranslationActivityInput(term="goodbye", language_code="lv"),
            TranslationActivityOutput("Ardievu"),
        ),
    ],
)
async def test_success_translate_activity_hello_german(input, output):
    async with aiohttp.ClientSession() as session:
        activity_environment = ActivityEnvironment()
        activities = TranslationActivities(session)
        assert output == await activity_environment.run(
            activities.translate_term, input
        )


@pytest.mark.asyncio
async def test_failed_translate_activity_bad_language_code():
    with pytest.raises(Exception) as e:
        input = TranslationActivityInput("goodbye", "xq")
        async with aiohttp.ClientSession() as session:
            activity_environment = ActivityEnvironment()
            activities = TranslationActivities(session)
            await activity_environment.run(activities.translate_term, input)
    assert "Invalid language code" in str(e)
