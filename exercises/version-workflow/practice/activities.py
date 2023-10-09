from shared import ChargeInput, CustomerInfo
from temporalio import activity


class LoanProcessingActivities:
    @activity.defn
    async def charge_customer(self, input: ChargeInput) -> str:
        activity.logger.info(
            f"*** charging customer***: customer_id: {input.customer_id}, amount {input.amount}, number_of_periods: {input.number_of_periods}"
        )

        # Pretend we charge them

        return f"charged {input.amount} to customer {input.customer_id}"

    @activity.defn
    async def send_thank_you_to_customer(self, input: CustomerInfo) -> str:
        activity.logger.info(
            f"*** sending thank you message to customer ***: customer_id: {input.customer_id}, email {input.email_address}"
        )

        # Pretend we send a thank you

        return f"sent thank you message to customer {input.customer_id}"
