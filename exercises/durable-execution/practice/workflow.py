from datetime import timedelta

from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import TranslationActivities
    from shared import (
        TranslationActivityInput,
        TranslationWorkflowInput,
        TranslationWorkflowOutput,
    )


@workflow.defn
class TranslationWorkflow:
    @workflow.run
    async def run(self, input: TranslationWorkflowInput) -> TranslationWorkflowOutput:
        workflow.logger.info(f"TranslationWorkflow invoked with {input}")

        hello_input = TranslationActivityInput(
            language_code=input.language_code, term="hello"
        )

        # TODO Add a log message using the workflow logger at the debug level
        # stating that the Activity has been invoked. Include the term and
        # language code
        hello_result = await workflow.execute_activity_method(
            TranslationActivities.translate_term,
            hello_input,
            start_to_close_timeout=timedelta(seconds=5),
        )
        hello_message = f"{hello_result.translation}, {input.name}"

        # TODO Add a log message using the workflow logger stating that the
        # Workflow is sleeping between translation calls

        # TODO Add a Timer that sleeps for 10 seconds

        # TODO Add a log message using the workflow logger at the debug level
        # stating that the Activity has been invoked. Include the term and language code
        goodbye_input = TranslationActivityInput(
            language_code=input.language_code, term="goodbye"
        )
        goodbye_result = await workflow.execute_activity_method(
            TranslationActivities.translate_term,
            goodbye_input,
            start_to_close_timeout=timedelta(seconds=5),
        )
        goodbye_message = f"{goodbye_result.translation}, {input.name}"

        return TranslationWorkflowOutput(
            hello_message=hello_message, goodbye_message=goodbye_message
        )
