import asyncio
from datetime import timedelta

from temporalio import workflow

# Import activity, passing it through the sandbox without reloading the module
with workflow.unsafe.imports_passed_through():
    from activities import LoanProcessingActivities
    from shared import ChargeInput, CustomerInfo


@workflow.defn
class LoanProcessingWorkflow:
    @workflow.run
    async def process_loan(self, info: CustomerInfo) -> str:
        workflow.logger.info(
            f"started process_loan workflow for customer: {info.customer_id}"
        )

        is_patched = workflow.patched("moved-thank-you-after-loop")

        if is_patched is False:
            confirmation = await workflow.execute_activity_method(
                LoanProcessingActivities.send_thank_you_to_customer,
                info,
                start_to_close_timeout=timedelta(seconds=5),
            )

        total_paid = 0
        for period in range(1, info.number_of_periods + 1):
            charge_input = ChargeInput(
                customer_id=info.customer_id,
                amount=info.amount,
                period_number=period,
                number_of_periods=info.number_of_periods,
            )

            charge_confirmation = await workflow.execute_activity_method(
                LoanProcessingActivities.charge_customer,
                charge_input,
                start_to_close_timeout=timedelta(seconds=5),
            )

            total_paid += charge_input.amount
            workflow.logger.info(
                f"payment complete for period {period} total paid: {charge_input.amount}"
            )

            await asyncio.sleep(10)

        if is_patched:
            confirmation = await workflow.execute_activity_method(
                LoanProcessingActivities.send_thank_you_to_customer,
                info,
                start_to_close_timeout=timedelta(seconds=5),
            )

        return f"loan for customer {info.customer_id} has been full paid(total={total_paid})"
