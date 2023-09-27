import pytest

from temporalio.testing import WorkflowEnvironment
from temporalio.worker import Worker
from temporalio import activity

from workflow import TranslationWorkflow
from shared import (
    TranslationWorkflowInput,
    TranslationActivityInput,
    TranslationActivityOutput,
)


@activity.defn(name="translate_term")
async def translate_term_mocked_french(input: TranslationActivityInput):
    if input.term == "hello":
        return TranslationActivityOutput("Bonjour")
    else:
        return TranslationActivityOutput("Au revoir")


@pytest.mark.asyncio
async def test_successful_translation():
    async with await WorkflowEnvironment.start_time_skipping() as env:
        async with Worker(
            env.client,
            task_queue="test-translation-workflow",
            workflows=[TranslationWorkflow],
            activities=[translate_term_mocked_french],
        ):
            input = TranslationWorkflowInput("Pierre", "fr")
            output = await env.client.execute_workflow(
                TranslationWorkflow.run,
                input,
                id="test-translation-workflow-id",
                task_queue="test-translation-workflow",
            )
            assert "Bonjour, Pierre" == output.hello_message
            assert "Au revoir, Pierre" == output.goodbye_message
