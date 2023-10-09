from datetime import timedelta

from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import TranslationActivities
    from shared import (
        TranslationWorkflowInput,
        TranslationWorkflowOutput,
        TranslationActivityInput,
    )


@workflow.defn
class TranslationWorkflow:
    @workflow.run
    async def run(self, input: TranslationWorkflowInput) -> TranslationWorkflowOutput:
        # TODO Create your Activity input data class object and populate it with
        #       two fields from the execute_activity call below

        # TODO Use your input object in the call below
        hello_result = await workflow.execute_activity_method(
            TranslationActivities.translate_term,
            "hello",
            input.language_code,
            start_to_close_timeout=timedelta(seconds=5),
        )
        # TODO Update hello_result to retrieve the value from the Activity output object
        #       returned by the call above
        hello_message = f"{hello_result}, {input.name}"

        # TODO Create your Activity input data class object and populate it with
        #       two fields from the execute_activity call below

        # TODO Use your input object in the call below
        goodbye_result = await workflow.execute_activity_method(
            TranslationActivities.translate_term,
            "hello",
            input.language_code,
            start_to_close_timeout=timedelta(seconds=5),
        )
        # TODO Update hello_result to retrieve the value from the Activity output object
        #       returned by the call above
        goodbye_message = f"{goodbye_result}, {input.name}"

        return TranslationWorkflowOutput(
            hello_message=hello_message, goodbye_message=goodbye_message
        )
