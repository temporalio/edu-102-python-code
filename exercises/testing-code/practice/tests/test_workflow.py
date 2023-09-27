import pytest
import aiohttp

from temporalio.testing import WorkflowEnvironment
from temporalio.worker import Worker

from workflow import TranslationWorkflow
from activities import TranslationActivities
from shared import TranslationWorkflowInput


@pytest.mark.asyncio
async def test_successful_translation():
    async with await WorkflowEnvironment.start_time_skipping() as env:
        async with aiohttp.ClientSession() as session:
            activities = TranslationActivities(session)
            async with Worker(
                env.client,
                task_queue="test-translation-workflow",
                workflows=[TranslationWorkflow],
                activities=[activities.translate_term],
            ):
                input = TranslationWorkflowInput("Pierre", "fr")
                output = await env.client.execute_workflow(
                    TranslationWorkflow.run,
                    input,
                    id="test-translation-workflow-id",
                    task_queue="test-translation-workflow",
                )
                # TODO add assertions here
