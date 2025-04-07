from datetime import timedelta

from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import AgeEstimationActivities


@workflow.defn
class EstimateAgeWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        age_estimate = await workflow.execute_activity_method(
            AgeEstimationActivities.retrieve_estimate,
            name,
            start_to_close_timeout=timedelta(seconds=5),
        )

        return f"{name} has an estimated age of {age_estimate.age}"
