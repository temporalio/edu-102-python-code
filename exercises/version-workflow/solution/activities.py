import logging
from temporalio import activity
from shared import ChargeInput, CustomerInfo

logging.basicConfig(level=logging.INFO)

class LoanProcessingActivities:

    @activity.defn
    async def charge_customer(self, input: ChargeInput) -> str:
        logging.info(
            f"*** Charging customer***: CustomerID: {input.customer_id}, Amount {input.amount}, Number of Periods: {input.number_of_periods}"
        )

        # Pretend we charge them

        return f"Charged {input.amount} to customer {input.customer_id}"

    @activity.defn
    async def send_thank_you_to_customer(self, input: CustomerInfo) -> str:
        logging.info(
            f"*** Sending thank you message to Customer ***: CustomerID: {input.customer_id}, Email {input.email_address}"
        )

        # Pretend we send a thank you

        return f"Sent thank you message to customer {input.customer_id}"
