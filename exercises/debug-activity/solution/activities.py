import logging
from temporalio import activity
from temporalio.exceptions import ApplicationError
from time import time
import aiohttp
from shared import OrderConfirmation, Address, Distance, Bill


class PizzaOrderActivities:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    @activity.defn
    async def get_distance(self, address: Address) -> Distance:
        logging.info("get_distance invoked; determining distance to customer address")

        # This is a simulation, which calculates a fake (but consistent)
        # distance for a customer address based on its length. The value
        # will therefore be different when called with different addresses,
        # but will be the same across all invocations with the same address.

        kilometers = len(address.line1) + len(address.line2) - 10
        if kilometers < 1:
            kilometers = 5

        distance = Distance(kilometers=kilometers)

        logging.info(f"get_distance complete: {distance}")
        return distance

    @activity.defn
    async def send_bill(self, bill: Bill) -> OrderConfirmation:
        logging.info(
            f"send_bill invoked: customer: {bill.customer_id} amount: {bill.amount}"
        )

        charge_amount = bill.amount

        if charge_amount > 3000:
            logging.info("Applying discount")

            charge_amount -= 500

        if charge_amount < 0:
            error_message = f"invalid charge amount: {charge_amount}"
            logging.error(error_message)

            raise ApplicationError(error_message)

        confirmation = OrderConfirmation(
            order_number=bill.order_number,
            status="SUCCESS",
            confirmation_number="P24601",
            billing_timestamp=time(),
            amount=charge_amount,
        )

        return confirmation
